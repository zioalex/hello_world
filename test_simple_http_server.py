#!/usr/bin/env python3

import requests
import simple_http_server 

def test_my_client(httpserver): # httpserver is a pytest fixture which starts the server
    # set up the server to serve /foobar with the json
    httpserver.expect_request("/").respond_with_json({"Id": "1",  "message": "Hello world"})
    #simple_http_server.run()
    # check that the request is served
    assert requests.get(httpserver.url_for("/")).json() == {"Id": "1",  "message": "Hello world"}

