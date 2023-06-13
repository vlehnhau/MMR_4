from funktionenAlgebra import *

def parse1(string: str):
    operators = ["+", "-", "*", "/"]
    symbols = ["0","1","2","3","4","5","6","7","8","9","x","a"]
    sym = string[0]
    if sym in symbols:
        return Constant(sym)
    elif sym in operators:
        if string[1] not in operators:
            if sym == "+":
                return AddFunction(parser([string[1]]), parser(string[2:]))
            if sym == "-":
                return SubFunction(parser([string[1]]), parser(string[2:]))
            if sym == "*":
                return MulFunction(parser([string[1]]), parser(string[2:]))
            if sym == "/":
                return DivFunction(parser([string[1]]), parser(string[2:]))
        else:
            nn = 2                                #nn: Numbers needed. Trifft man auf einen Operator braucht es 2 Zeichen. Bei jeden Zusätzlichen Operator: nn += 1
            i = 1                                 # +(+(1, 1), 1)  +(+11)1
            for y in range(2, len(string)):
                if string[y] in operators:
                    nn += 1
                elif string[y] in symbols:
                    nn -= 1
                if nn == 0:
                    if sym == "+":
                        return AddFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "-":
                        return SubFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "*":
                        return MulFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "/":
                        return DivFunction(parse1(string[1:i]), parse1(string[i:]))
                i += 1


def lexAn(string: str) -> list:
    tokens = ["sin", "cos", "exp", "ln", "x", "-", "*", "/", "+"]
    tList = string.split()
    for t in range(0, len(tList)):                      #Wenn es kein Token ist, ist es eine Zahl
        if tList[t] not in tokens:
            tList[t] = float(tList[t])                  #Zahl wird zum Float gemacht
    return tList


# print(lexAn("+ 1 + 1 - 2.3 * 2 x"))
# print(lexAn("+1 + 1 - 2.3 * 2 x"))
# print(lexAn("+ 1 + sin 1 - 2.3 * 2 x"))

def parser(tList: list):
    tokens = ["sin", "cos", "exp", "ln", "x", "-", "*", "/", "+"]
    operators = ["+", "-", "*", "/"]
    functions = ["sin", "cos", "exp", "ln"]
    ft = tList[0]                                                   #ft =first token
    if ft not in tokens:
        return float(ft)  #ft ist eine Zahl
    elif ft == "x":
        return "x"
    else:  #ft ist ein token
        if ft == "sin":
            return MatmulFunction(Sin(), parser(tList[1:]))
        elif ft == "cos":
            return MatmulFunction(Cos(), parser(tList[1:]))
        elif ft == "exp":
            return MatmulFunction(Exp(), parser(tList[1:]))
        elif ft == "ln":
            return MatmulFunction(Ln(), parser(tList[1:]))
        else:                                                           #ft ist ein Operator
            if tList[1] not in operators:
                if ft == "+":
                    return AddFunction(parser([tList[1]]), parser(tList[2:]))
                if ft == "-":
                    return SubFunction(parser([tList[1]]), parser(tList[2:]))
                if ft == "*":
                    return MulFunction(parser([tList[1]]), parser(tList[2:]))
                if ft == "/":
                    return DivFunction(parser([tList[1]]), parser(tList[2:]))
            else:
                nn = 2                              # nn: Numbers needed. Trifft man auf einen Operator braucht es 2 Zeichen. Bei jeden Zusätzlichen Operator: nn += 1
                i = 1
                for y in range(1, len(tList)):
                    if tList[y] in operators:
                        nn += 1
                    elif tList[y] not in functions:
                        nn -= 1
                    if nn == 0:
                        if ft == "+":
                            print(tList[1:i])
                            print(tList[i:])
                            return AddFunction(parser(tList[1:i]), parser(tList[i:]))
                        if ft == "-":
                            return SubFunction(parser(tList[1:i]), parser(tList[i:]))
                        if ft == "*":
                            return MulFunction(parser(tList[1:i]), parser(tList[i:]))
                        if ft == "/":
                            return DivFunction(parser(tList[1:i]), parser(tList[i:]))
                    i += 1


if __name__ == '__main__':
    expression = "+ 1 + 1 - 2.3 * 2 x"
    tokens = lexAn(expression)
    print(parse1("+1+1-2*2x"))
    print(parse1("++111"))
    print(tokens)
    print(parser(tokens))