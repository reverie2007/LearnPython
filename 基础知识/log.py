"""
    log模块使用
"""
import logging


logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug("debug log!")
logging.info("info log")
logging.error("error log")
logging.warning("warning log")
