from typing import Union

def reverse_integer(numeric: int) -> int:
    """
    For a given numeric value it returns it in a reversed order.
    :param numeric: given number
    """
    return int(str(numeric)[::-1])


def fibo(n: int) -> int:
    """
    Function to generate nth Fibonacci number.
    :rtype: int
    """
    if n in (0, 1):
        return 1
    return fibo(n - 1) + fibo(n - 2)


def find_nearest_fibo(my_number: Union[int, float]) -> int:
    """
    A function which takes n (float or integer)
    as a parameter and returns the largest Fibonacci
    number smaller than n.
    :param my_number: number as a reference to returned Fibonacci number
    :return: int
    """
    success = False
    largest_fibo = fibo(1)
    n_fibo = 2
    while not success:
        largest_fibo = fibo(n_fibo)
        if largest_fibo > my_number:
            success = True
            largest_fibo = fibo(n_fibo - 1)
        n_fibo += 1
    return largest_fibo


if __name__ == '__main__':
    print(reverse_integer(4656))
    print(reverse_integer(5460))
    print(find_nearest_fibo(1000))
    print(find_nearest_fibo(454.4))
# %%
