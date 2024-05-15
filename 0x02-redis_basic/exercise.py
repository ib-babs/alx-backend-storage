#!/usr/bin/env python3
'''Class Module'''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    '''A class that stores data on database'''

    def __init__(self) -> None:
        '''Instantiate a class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable]) -> None:
        return self._redis.get(key)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
