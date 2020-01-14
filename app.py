from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def ip():
    return request.remote_addr, 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
