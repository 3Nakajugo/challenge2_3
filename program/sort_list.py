

def list_sort(list_A):
    evens = []
    odds = []
    chars = []
    if isinstance(list_A, int):
        return ('Invalid Input')

    if isinstance(list_A, str):
        return ('Invalid Input')

    if list_A:

        for x in list_A:
            if isinstance(x, int):
                if (x % 2 == 0):
                    evens.append(x)
                else:
                    odds.append(x)
            else:
                chars.append(x)

        return dict(chars=sorted(chars), evens=sorted(evens), odds=sorted(odds))
    return dict(evens=[], odds=[], chars=[])
