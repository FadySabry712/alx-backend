#!/usr/bin/env python3
"""Basic caching task0
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dict.
    """
    def put(self, key, item):
        """Adds item in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key.
        """
        return self.cache_data.get(key, None)
