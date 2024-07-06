from loguru import logger

logger.add("app.log", level="INFO", format="{time} - {level} - {message}")
logger.add("app.log", level="WARNING", format="{time} - {level} - {message}")
logger.add("app.log", level="ERROR", format="{time} - {level} - {message}")
logger.add("app.log", level="DEBUG", format="{time} - {level} - {message}")

logger = logger.bind(name="sophons")
