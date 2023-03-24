import logging

# 创建一个全局的 logger 对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器，将日志写入到文件中
handler = logging.FileHandler('./log/spider.log')
handler.setLevel(logging.DEBUG)

# 终端
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# 创建一个格式化器，定义日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将文件处理器添加到 logger 对象中
logger.addHandler(handler)
logger.addHandler(stream_handler)