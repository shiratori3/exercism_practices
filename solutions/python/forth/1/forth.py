from typing import List


builtin_op = ("+", "-", "*", "/", "dup", "drop", "swap", "over", )


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data: List[str]) -> List[int]:
    user_op = {}
    res = []
    if len(input_data) > 1:
        for index in range(len(input_data) - 1):
            temp = input_data[index].split()
            _, opname, *args, _ = temp
            if opname.isnumeric():
                raise ValueError("illegal operation")
            # take care of user_op in args
            if user_op.keys():
                opvalue = " ".join([
                    user_op.get(arg)
                    if arg in user_op.keys()
                    else arg
                    for arg in args
                ])
            else:
                opvalue = " ".join(args)
            user_op[opname.lower()] = opvalue.lower()

    value_data = input_data[-1].lower()
    if user_op.values():
        for k, v in user_op.items():
            value_data = value_data.replace(k, v)
    if not check_eval_vaild(value_data):
        return None
    for v in value_data.split():
        if is_int(v):
            res.append(int(v))
        if v in builtin_op:
            if v in ("+", "-", "*", "/"):
                num1 = res.pop()
                num2 = res.pop()
                s_eval = " ".join([str(num2), v, str(num1)])
                res.append(int(eval(s_eval)))
            if v == "dup":
                num1 = res.pop()
                res.extend([num1] * 2)
            if v == "drop":
                num1 = res.pop()
            if v == "swap":
                num1 = res.pop()
                num2 = res.pop()
                res.extend([num1, num2])
            if v == "over":
                num1 = res.pop()
                num2 = res.pop()
                res.extend([num2, num1, num2])
    return res


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def check_eval_vaild(value_data: str) -> bool:
    temp = value_data.split()
    if len(temp) == 1:
        v = temp[0]
        if v in builtin_op:
            raise StackUnderflowError("Insufficient number of items in stack")
        try:
            _ = int(v)
            return True
        except:
            raise ValueError("undefined operation")
    else:
        if temp[0] == ":":
            raise ValueError("illegal operation")
        if temp[-1] == "/":
            if temp[-2] == "0":
                raise ZeroDivisionError("divide by zero")
        if temp[-1] in ("+", "-", "*", "/", "swap", "over"):
            if len(temp) == 2:
                raise StackUnderflowError("Insufficient number of items in stack")
        return True
        
