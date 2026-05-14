"""Base service class providing a logger for derived services.

The logger is configured with a simple stream handler that outputs to stdout.
Derived services can call ``self.log(message)`` to emit informational logs.
"""

import logging
from typing import Optional


class BaseService:
    """Base class for services with built‑in logging.

    Parameters
    ----------
    name: str, optional
        Name of the logger. Defaults to ``"BaseService"``.
    level: int, optional
        Logging level. Defaults to ``logging.INFO``.
    """

    def __init__(self, name: str = "BaseService", level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log(self, message: str, level: int = logging.INFO) -> None:
        """Log *message* at the given *level*.

        Parameters
        ----------
        message: str
            The log message.
        level: int, optional
            Logging level, e.g., ``logging.DEBUG``. Defaults to INFO.
        """
        self.logger.log(level, message)
