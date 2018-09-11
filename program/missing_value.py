
def find_number(y):
    missing = []
    if not isinstance(y, list):
        raise TypeError('invalid input')
    else:
        for i in range(1, 10):
            if i not in y:
                missing.append(i)
        return missing


print(find_number([1, 2, 3, 5, 6, 7, 9]))
