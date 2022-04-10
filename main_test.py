import main
import json


def test():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert json.loads(r.data.decode('utf-8'))["mins"] == 5
