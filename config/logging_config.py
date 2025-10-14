import logging

# 콘솔 핸들러 설정
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s'
)
console_handler.setFormatter(console_format)

# 로거 설정
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)