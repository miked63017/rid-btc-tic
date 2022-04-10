from flask import Flask
from google.cloud import secretmanager
import json
client = secretmanager.SecretManagerServiceClient()
name = f"projects/newagent-8596d/secrets/b-api-key/versions/3"
request = secretmanager.AccessSecretVersionRequest(name=name)
response = client.access_secret_version(request=request)
api_key = response.payload.data.decode('UTF-8')

name = f"projects/newagent-8596d/secrets/b-secret/versions/1"
request = secretmanager.AccessSecretVersionRequest(name=name)
response = client.access_secret_version(request=request)
api_secret = response.payload.data.decode('UTF-8')

from binance.client import Client
client = Client(api_key, api_secret)

app = Flask(__name__)


@app.route('/')
def btc():
    return json.dumps(client.get_avg_price(symbol='BTCUSDT'))


if __name__ == '__main__':
    # Local dev, appengine will run gunicorn to serve
    app.run(host='127.0.0.1', port=8080, debug=True)
