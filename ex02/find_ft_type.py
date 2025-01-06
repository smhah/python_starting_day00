def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }
    object_type = type(object)
    res = type_names.get(object_type, "Type not found")
    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif res != "Type not found":
        print(f"{res} : {object_type}")
    else:
        print(res)
    return 42