if __name__ == '__main__':
    import sys
    def add_t_arg():
        sys.argv[0] = '-t'
        print("I'm an argument!")

    def add_p_arg():
        sys.argv[0] = '-p'
        print("I'm an argument too!")

    for x in sys.argv:
        if x == '-t':
            add_t_arg()
        elif x == '-p':
            add_p_arg()
        print("Argument: ", x)