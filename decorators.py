def timer(f):
    from time import time
    def wrapper(*args, **kvargs):
        before = time()
        result = f(*args, **kvargs)
        after = time()
        print("elapsed time", after - before)
        return result
    return wrapper

def times(n):
    def times_impl(f):
        def wrapper(*args, **kvargs):
            for x in range(n):
                f(*args, **kvargs)
        return wrapper
    return times_impl
        
@timer
def add(x, y):
  return x + y

@times(5)
def core(x):
  print(x)  

print(add(10, 10))
print(core(5))