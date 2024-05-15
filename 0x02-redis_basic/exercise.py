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
        '''Store a random key in database'''
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        '''Get converted value'''
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        '''Parameterized to str'''
        return Cache.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        '''Parameterized to int'''
        return int(Cache.get(key))
