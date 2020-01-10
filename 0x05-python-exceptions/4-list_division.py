def list_division(my_list_1, my_list_2, list_length):
    count = 0
    newlist = []
    for i in range(list_length):
        try:
            count = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            count = 0
        except ZeroDivisionError:
            print("division by 0")
            count = 0
        except IndexError:
            print("out of range")
            count = 0
        finally:
            newlist.append(count)
    return newlist
