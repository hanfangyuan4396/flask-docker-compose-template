import json
import os
import logging
from logging.handlers import RotatingFileHandler

def load_config():
    if os.path.exists("config.json"):
        with open("config.json") as f:
            return json.load(f)

    with open("config-example.json") as f:
        return json.load(f)

config = load_config()

def reload_conf():
    global config
    config = load_config()

def conf() -> dict:
    return config

def setup_logging():
    # 设置日志格式
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]'
    )

    # 设置文件日志，日志文件名为 app.log，最大文件大小为 10MB，最多保留 5 个文件
    file_handler = RotatingFileHandler('app.log', maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 设置控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 获取根日志记录器，添加文件日志和控制台日志
    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])
