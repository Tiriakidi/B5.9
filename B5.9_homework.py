import time

def time_this(num_runs):
    def decorator(func):
        def func_wrapper():
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return func_wrapper
    return decorator

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

f()

##задание со звездочками

class Timer:
    def __init__(self, num_runs=0):
        self.num_runs = num_runs

    def __enter__(self):
        self.avg_time = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        self.avg_time = time.time() - self.avg_time
        print("Выполнение заняло %.5f секунд" % self.avg_time)
        return self

    def __call__(self, func):
        def func_wrapper():
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return func_wrapper

#запуск декоратора в качестве объекта класса-секундомера
@Timer(num_runs=10)
def f():
    for j in range(1000000):
        pass

f()

#запуск класса-секундомера, как контекстного менеджера
with Timer():
    for j in range(1000000):
        pass