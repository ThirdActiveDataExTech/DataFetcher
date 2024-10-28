import os
import sys
import logging.handlers
from extract_blog import config

log_format = "[%(asctime)s] %(levelname)s, %(filename)s %(funcName)s %(lineno)d, %(message)s"
formatter = logging.Formatter(log_format, '%Y/%m/%d %H:%M:%S')

log = logging.getLogger(__name__)

# if 'APP_NAME' not in os.environ:
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
log.addHandler(handler)

if 'APP_NAME' in os.environ:
    log_dir = config.LOG_DIR
    log_name = f"{config.APP_NAME}.log"
    log_path = os.path.join(log_dir, log_name)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=10000000, backupCount=10)
    # handler = logging.handlers.TimedRotatingFileHandler(
    #     filename=log_path, when='midnight', interval=30, encoding='utf-8'
    # )

    handler.setFormatter(formatter)
    log.addHandler(handler)

log.setLevel(logging.INFO)