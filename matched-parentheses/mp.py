def match(s):
    d = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for i in s:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            last_item = stack.pop()
            if i != d.get(last_item):
                return False
    if len(stack):
        return True
    else:
        return False