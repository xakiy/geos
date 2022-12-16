import multiprocessing
import meinheld.server


# In rootless container this will acquire all CPUS
# otherwise you can limit the number, like:
# workers = 2
workers = int(multiprocessing.cpu_count() * 1.5)

bind = "0.0.0.0:8080"
keepalive = 30
errorlog = '-'
pidfile = 'gunicorn.pid'
worker_class = 'meinheld.gmeinheld.MeinheldWorker'
meinheld.server.set_access_logger(None)
