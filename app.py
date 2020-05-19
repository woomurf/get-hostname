import os

from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

hostname = os.environ.get('HOSTNAME', '--no-hostname--')
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def main():
    return f"Hello {request.base_url} from {hostname} (Hi I'm Develop)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
