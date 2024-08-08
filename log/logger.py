import os
from sys import stdout
from loguru import logger
from core import settings


__all__ = ["setup_logger"]


def setup_logger():
    # Удаляем все предустановленные обработчики (если они есть)
    logger.remove()

    # Создаём директорию для логов, если она не существует
    log_dir = settings.BASE_DIR + "/log/logs"
    os.makedirs(log_dir, exist_ok=True)

    # Настраиваем обработчик для вывода логов в консоль с цветами
    logger.add(
        sink=stdout,
        format="<green>{level}</green> <cyan>{time:DD.MM.YYYY - HH:mm:ss}</cyan> <level>{message}</level>",
        level="INFO",
        colorize=True
    )

    # Настраиваем обработчик для записи логов уровня ERROR и выше в файл
    logger.add(
        sink=os.path.join(log_dir, "errors.log"),
        backtrace=True,
        format="{level} {time:DD.MM.YYYY - HH:mm:ss} File: {module} Funk: {function} Line: {line} - Message: {message}\n{exception}",
        diagnose=True,
        level="ERROR",
        rotation="1 month",
        compression="zip"
    )

    # Настраиваем обработчик для записи логов уровня WARNING в отдельный файл
    logger.add(
        sink=os.path.join(log_dir, "warnings.log"),
        format="{level} {time:DD.MM.YYYY - HH:mm:ss} File: {module} Funk: {function} Line: {line} - Message: {message}",
        level="WARNING",
        rotation="1 month",
        compression="zip"
    )

    # Настраиваем обработчик для записи логов уровня DEBUG в отдельный файл
    logger.add(
        sink=os.path.join(log_dir, "debug.log"),
        format="{level} {time:DD.MM.YYYY - HH:mm:ss} File: {module} Funk: {function} Line: {line} - Message: {message}",
        level="DEBUG",
        rotation="1 week",
        compression="zip"
    )
