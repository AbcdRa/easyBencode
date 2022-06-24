def deserialize(str, return_offset=False):
    if str[0] == 'i':
        el, offset = deserialize_int(str)
    if is_number(str[0]):
        el, offset = deserialize_str(str)
    if str[0] == 'l':
        el, offset = deserialize_list(str)
    if str[0] == 'd':
        el, offset = deserialize_dict(str)
    if str[0] == 'e':
        return False, False
    if return_offset:
        return el, offset
    else:
        return el



def deserialize_int(str):
    num_str = ""
    first_index = 1
    if str[1] == "-":
        num_str = "-"
        first_index = 2
    for char in str[first_index:]:
        if not is_number(char) :
            break;
        num_str += char
    #два символа это i и e
    return int(num_str), len(num_str) + 2


def deserialize_str(str):
    count_str = ""
    for char in str:
        if not is_number(char):
            break;
        count_str += char
    str_length = int(count_str)
    offset = len(count_str) + 1
    return str[offset:offset+str_length], str_length+offset


def deserialize_list(str):
    result = []
    i = 1
    while True:
        element, offset = deserialize(str[i:], return_offset=True)
        if element:
            result.append(element)
            i += offset
        else:
            break;
    return result, i+1


def deserialize_dict(str):
    result = {}
    i = 1
    while True:
        key, offset = deserialize(str[i:], return_offset=True)
        if key:
            i += offset
            value, offset = deserialize(str[i:], return_offset=True)
            result[key] = value
            i += offset
        else:
            break;
    return result, i


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


print(deserialize("i10e"))
print(deserialize("3:abc"))
print(deserialize("l2:ab2:cd2:efe"))
print(deserialize("lli1ei2ei3eeli4ei5ei6eeli7ei8ei9eee"))
print(deserialize("d1:ali1ei2ei3ee1:bli7ei8ei9ee1:cli4ei5ei6eee"))