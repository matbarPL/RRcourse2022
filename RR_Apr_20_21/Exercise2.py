def reverse_integer(numeric:int)->int:
    """
    For a given numeric value it returns it in a reversed order.
    :param numeric: given number
    """
    return int(str(numeric)[::-1])

if __name__ == '__main__':
    print(reverse_integer(4656))
    print(reverse_integer(5460))
#%%
