def comma_code(a_list):
    """
    Turns a list into a string of elements separated by commas
    :param a_list: a list of strings
    :return: a string separated by commas
    """
    a_list[-1] = 'and ' + a_list[-1]
    stringified = ", ".join(a_list)
    return stringified


res = comma_code(['apples', 'bananas', 'tofu', 'cats'])
print(res)
