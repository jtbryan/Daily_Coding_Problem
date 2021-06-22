def car(pair):
    ''' Return first element of pair '''
    def return_first(a, b):
        return a
    return pair(return_first)

def cdr(pair):
    ''' Return last element of pair '''
    def return_last(a, b):
        return b
    return pair(return_last)

def cons(a, b):
    ''' Constructs a pair '''
    def pair(f):
        return f(a, b)
    return pair

def main():
    print(f"First: {car(cons(3,4))}")
    print(f"Last: {cdr(cons(3,4))}")
    pass

if __name__ == "__main__":
    main()