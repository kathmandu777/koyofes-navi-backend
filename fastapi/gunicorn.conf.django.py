# config
wsgi_app = "config.asgi:application"
worker_class = "config.worker.RestartableUvicornWorker"
bind = "0.0.0.0:8001"
workers = 1
reload = True
daemon = False  # FIXME not to finish process
