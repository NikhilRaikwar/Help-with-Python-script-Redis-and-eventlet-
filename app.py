import eventlet
from eventlet.green import socket
from eventlet.green import ssl

eventlet.monkey_patch()

import datetime
import redis
import numpy as np
from urllib.parse import urlparse
from flask import Flask

# Wrap the standard library's socket module with eventlet's green version
socket.socket = eventlet.green.socket.socket

# Wrap the standard library's ssl module with eventlet's green version
ssl.wrap_socket = eventlet.green.ssl.wrap_socket

my_application = Flask(__name__)

REDIS_URL = "***********************"
print("REDIS_URL: ", REDIS_URL)

host = urlparse(REDIS_URL).hostname
port = urlparse(REDIS_URL).port
password = urlparse(REDIS_URL).password

try:
    # Create an SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False  # Disable hostname checking
    ssl_context.verify_mode = ssl.CERT_NONE  # Disable certificate verification

    my_application.redis = redis.Redis(
        host=host,
        port=port,
        password=password,
        ssl=True,
        ssl_cert_reqs=None,
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_ca_certs=None,
        ssl_cert_reqs='required',
        socket_connect_timeout=5,
        socket_keepalive=True,
        socket_keepalive_options={'tcp_keepidle':  60},
        connection_pool=None,
        unix_socket_path=None,
        encoding='utf-8',
        encoding_errors='strict',
        charset='utf-8',
        errors='strict',
        decode_responses=False,
        retry_on_timeout=False,
        ssl_context=ssl_context,  # Pass the SSL context here
    )

    my_application.redis.set("redis", "ready")
except Exception as e:
    print(f"Error: {e}")

@my_application.route("/")
def index():
    # Set a value in Redis
    my_application.redis.set("hello", str(datetime.datetime.now()))
    return "Hello, World!"

if __name__ == "__main__":
    my_application.run(debug=True)
