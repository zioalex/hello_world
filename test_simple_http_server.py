#!/usr/bin/env python3

import requests
from simple_http_server import runone
import threading


def test_my_client(httpserver): # httpserver is a pytest fixture which starts the server
    # set up the server to serve /foobar with the json
    httpserver.expect_request("/").respond_with_json({"Id": "1",  "message": "Hello world"})
    assert requests.get(httpserver.url_for("/")).json() == {"Id": "1",  "message": "Hello world"}


def test_my_client_new(httpserver): # httpserver is a pytest fixture which starts the server
    # set up the server to serve /foobar with the json
    #httpserver.expect_request("/").respond_with_json({"Id": "1",  "message": "Hello world"})
    #assert requests.get(httpserver.url_for("localhost:8000")).json() == {"Id": "1",  "message": "Hello world"}
    # Try to answer only one request
    print("Start test")
    #runone()
    #thread = threading.Thread(runone())
    #thread.start()
    # check that the request is served
    #print(requests.get("http://localhost:8000").json())
    assert requests.get("http://localhost:8000").json() == {'id': '1',  'message': 'Hello world'}
    print("End test")

