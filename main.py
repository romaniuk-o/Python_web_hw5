import logging
from multiprocessing import Pool, cpu_count, Process
from time import time


def factorize(number):
    result = []
    for _ in range(1, number + 1):
        if number % _ == 0:
            result.append(_)
    print(result)
    return result




if __name__ == '__main__':
    time_ = time()
    a = factorize(128)
    b = factorize(255)
    c = factorize(99999)
    d = factorize(10651060)
    print(f'Час при синхронній версії - {time() - time_}')
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    list_numbers = [128, 255, 99999, 10651060]
    time_ = time()
    with Pool(cpu_count()) as pool:
        pool.map_async(factorize, list_numbers)
        pool.close()
        pool.join()
    print(f'Час при паралельній версії - {time() - time_}')