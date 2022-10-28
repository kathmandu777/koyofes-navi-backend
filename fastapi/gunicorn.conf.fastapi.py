# config
wsgi_app = "config.asgi:fastapp"
worker_class = "config.worker.RestartableUvicornWorker"
bind = "0.0.0.0:8000"
workers = 20
reload = True
daemon = True
