import logging
from typing import Optional


def get_logger(name: str = "app", level: int = logging.INFO, fmt: Optional[str] = None) -> logging.Logger:
    """Create and return a logger.

    Args:
        name: Logger name.
        level: Logging level, default INFO.
        fmt: Optional log format string.
    Returns:
        Configured ``logging.Logger`` instance.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        # Logger already configured, avoid duplicate handlers
        return logger
    logger.setLevel(level)
    handler = logging.StreamHandler()
    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    return logger
