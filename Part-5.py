def variableConst(variable, pattern):
    for equality in pattern:
        if " != " in equality:
            items = equality.split(" != ")
            if variable[int(items[0][1:])] == variable[int(items[1][1:])]:
                return False
        else:
            items = equality.split(" = ")
            if variable[int(items[0][1:])] != variable[int(items[1][1:])]:
                return False
    return True

variable = [2,3,3,3,1]
constraints = ["x1 = x2","x2 = x3","x0 != x4"]
print(variableConst(variable,constraints))
variable = [5,2,5,7]
constraints = ["x1 = x2","x2 = x3","x0 = x4"]
print(variableConst(variable,constraints))
