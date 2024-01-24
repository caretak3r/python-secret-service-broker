import threading
import time
import random
from functools import wraps

class Lock:
    """
    A simple lock mechanism to ensure atomic operations for create, update or modify secrets.
    """
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self):
        """
        Acquires the lock if possible. If the lock is in use, waits until the lock is released.
        """
        self.lock.acquire()

    def release(self):
        """
        Releases the lock.
        """
        self.lock.release()



def exponential_backoff(max_retries=5):
    """
    A decorator for implementing exponential backoff. If the decorated function fails, it will be retried
    with an exponentially increasing wait time until the maximum number of retries is reached.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    wait_time = (2 ** i) + (random.randint(0, 1000) / 1000)
                    time.sleep(wait_time)
            return None  # or raise an exception, or a specific return value indicating failure
        return wrapper
    return decorator
