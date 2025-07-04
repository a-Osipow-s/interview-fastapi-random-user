import multiprocessing

bind = '0.0.0.0:8000'
reload = True

accesslog = '-'
errorlog = '-'

workers = 1
capture_output = True

timeout = 1800
graceful_timeout = 10

worker_class = 'gthread'
worker_class = 'uvicorn.workers.UvicornWorker'

threads = 8 * multiprocessing.cpu_count()