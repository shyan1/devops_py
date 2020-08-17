# Numba just-in-time (JIT) compiler
from numba import jit

def timing(f):
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec")
        return result
    return wrap

@timing
@jit(nopython=True)
def expmean_jit(rea):
    value = rea.mean() ** 2
    return value

