#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(0, list_length):
        try:
            e1 = my_list_1[i]
            e2 = my_list_2[i]
            result = e1 / e2
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
