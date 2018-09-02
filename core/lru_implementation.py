"""
LRU Implementation

Developer: Dev Team
Last Modified Date:
"""


def LRUCache(max_size=100):
    """
    A simple dict-based LRU cache
    The cached function must:
     - Have no kwargs
     - Have only hashable args
       - If the decorated function is passed an unhashable arg, a TypeError
         will be raised
    Usage:
        @LRUCache(max_size=50)
        def to_be_cached(foo, bar):
            ... some computation ...
            return val
    """
    cache = {}
    cache_keys = []

    def lrucache_dec(fn):
        def cached_fn(*args):
            # args is a tuple, so it can be used as a dict key
            if args in cache:
                # Set args as most-recently-used
                del cache_keys[cache_keys.index(args)]
                cache_keys.append(args)
                return cache[args]

            retval = fn(*args)

            # Add to the cache and set as most-recently-used
            cache[args] = retval
            cache_keys.append(args)

            # Prune the cache if necessary
            if len(cache_keys) > max_size:
                del cache[cache_keys[0]]
                del cache_keys[0]
            return retval
        return cached_fn

    return lrucache_dec

@LRUCache(max_size=5)
def to_be_cached(foo, bar):
    print "Computing for %r, %r" % (foo, bar)
    return foo * 1000 + bar * 100

if __name__ == '__main__':
    print to_be_cached(3, 5)
    print to_be_cached(4, 5)
    print to_be_cached(5, 5)
    print to_be_cached(6, 5)
    print "== (3, 5) cached, so no computation =="
    print to_be_cached(3, 5)
    print to_be_cached(7, 5)
    print "== Evicts (4, 5) =="
    print to_be_cached(8, 5)
    print to_be_cached(4, 5)
