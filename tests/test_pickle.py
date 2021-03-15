from time import sleep
from shutil import rmtree
from cache_decorator import Cache
from .utils import standard_test_array

@Cache(
    cache_dir="./test_cache",
    backup=False,
)
def cached_function(a):
    sleep(2)
    return [1, 2, 3]


def test_pickle():
    standard_test_array(cached_function)
    rmtree("./test_cache")