def serialize(obj):
    if type(obj) == int:
        return serialize_int(obj)
    if type(obj) == str:
        return serialize_str(obj)
    if type(obj) == list:
        return serialize_list(obj)
    if type(obj) == dict:
        return serialize_dict(obj)

def serialize_int(num):
    return "i"+str(num)+"e"

def serialize_str(string):
    return str(len(string))+":"+string

def serialize_list(l):
    result = "l"
    for el in l:
        result += serialize(el)
    return result + "e"

def serialize_dict(d):
    result = "d"
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        result += serialize(key)+serialize(d[key])
    return result + "e"

print(serialize(10))
print(serialize("abc"))
print(serialize(["ab","cd","ef"]))
print(serialize([[1,2,3],[4,5,6],[7,8,9]]))
print(serialize({"a":[1,2,3], "c":[4,5,6], "b":[7,8,9]}))
print(serialize({"six":[6,6],"seven":[7,7]}))
