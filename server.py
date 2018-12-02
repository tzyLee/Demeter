from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context=('/etc/nginx/ssl/cert.pem', '/etc/nginx/ssl/cert.key'), port = 8081)
