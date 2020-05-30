#!/usr/bin/env python3
version = "v1"

def hello_world(version):   
    return "Hello World {}".format(version)

if __name__ == "__main__":
    while True:
        print(hello_world(version))
