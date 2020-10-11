from flask import Flask, Request
from flask import Blueprint, request
from urllib.parse import urlparse
app = Flask(__name__)
import socket


@app.route('/')
def hello_world():
    url_data = urlparse(request.url)
    print("request",request.url)
    print("---",url_data.port)
    return 'Hello, World! ' + str(url_data.port)