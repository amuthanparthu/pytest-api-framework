import time
import functools
from utils.logger import logger

def retry(attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, attempts + 1):
                try:
                    logger.info(
                        f"Attempt {attempt}/{attempts} for {func.__name__}"
                    )
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(
                        f"Failure on attempt {attempt}: {e}"
                    )
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator
