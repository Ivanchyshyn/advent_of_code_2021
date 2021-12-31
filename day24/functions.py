def get_value(text, variables):
    if text in variables:
        return variables[text]
    return int(text)


def inp(code, variables, value):
    variables[code.strip()] = int(value)


def add(code, variables):
    a, b = code.strip().split()
    variables[a] += get_value(b, variables)


def mul(code, variables):
    a, b = code.strip().split()
    variables[a] *= get_value(b, variables)


def div(code, variables):
    a, b = code.strip().split()
    variables[a] //= get_value(b, variables)


def mod(code, variables):
    a, b = code.strip().split()
    variables[a] %= get_value(b, variables)


def eql(code, variables):
    a, b = code.strip().split()
    variables[a] = int(variables[a] == get_value(b, variables))
