from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def ip():
    return request.remote_addr, 200
