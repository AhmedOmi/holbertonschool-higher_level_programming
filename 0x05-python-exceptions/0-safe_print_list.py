def safe_print_list(my_list=[], x=0):
    for x in my_list:
        try:
            print(x)
        except IndexError:
            pass

