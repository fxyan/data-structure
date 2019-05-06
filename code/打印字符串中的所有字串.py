def main():
    test = 'abc'
    print_all_sub(test)

def print_all_sub(test):
    f(test, 0, '')

def f(test, i, pre):
    if i == len(test):
        if pre != '':
            print(pre)
        return
    f(test, i+1, pre+test[i])
    f(test, i+1, pre)

main()
