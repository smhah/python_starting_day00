def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake"
    }
    object_type = type(object)
    res = type_names.get(object_type, "Type not Found")
    if object is None:
        res = type_names.get(None)
    if res != "Type not Found":
        if (object_type == int or object_type == bool) and object != 0:
            res = "Type not Found"
        if object_type == str and object != "":
            res = "Type not Found"
        if object_type == float and object == object:
            res = "Type not Found"
    if res == "Type not Found":
        print(res)
        return 1
    else:
        print(f"{res}: {object} {object_type}")
    return 0