# in this file we check what is an expected output for the temperature conversion performed in R
def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')

if __name__ == '__main__':
    print(convert(50), convert(70), convert(90))