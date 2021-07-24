def SherlockValidString(s):
    char_list = []

    for char in s:
        if char not in char_list:
            char_list.append(char)
    if len(char_list) == 1:
        return True

    char_count = []
    for char in char_list:
        char_count.append(s.count(char))

    dig_list = []
    for dig in char_count:
        if dig not in dig_list:
            dig_list.append(dig)

    if len(dig_list) == 1:
        return True

    if len(dig_list) > 2:
        return False

    if char_count.count(dig_list[0]) > 1 and char_count.count(dig_list[1]) > 1:
        return False

    if char_count.count(dig_list[0]) == 1:
        min_count = dig_list[0]
        max_count = dig_list[1]
    else:
        min_count = dig_list[1]
        max_count = dig_list[0]

    if min_count == 1:
        return True

    if -1 <= max_count - min_count <= 1:
        return True

    return False
