from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def main():
    return f"Hello {request.base_url}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
