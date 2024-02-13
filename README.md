# Help-with-Python-script-Redis-and-eventlet-
We have a Python script that utilizes Flask, Redis with TLS (rediss), and the Eventlet library. The current implementation encounters connection issues when using Eventlet with Redis TLS. We are seeking an expert Python developer to provide a solution to this problem.


- Please note that disabling certificate verification (ssl_cert_reqs=None) is generally not recommended for production environments due to security risks. It should only be used for testing purposes or in trusted networks.

- Regarding the versions of the libraries, you should use the latest stable versions unless you have specific compatibility requirements. As of now, the latest stable version of eventlet is 0.34.1, and for redis, it's 7.2.0. However, always check the official documentation or repository for the most up-to-date information on compatibility and supported features.
