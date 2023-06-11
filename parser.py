from funktionenAlgebra import *

def parse1(string: str):
    operators = ["+", "-", "*", "/"]
    symbols = ["0","1","2","3","4","5","6","7","8","9","x","a"]
    for x in range(0, len(string)):
        sym = string[x]
        if sym in symbols:
            return Constant(sym)
        elif sym in operators:
            nn = 2                                #nn: Numbers needed. Trifft man auf einen Operator braucht es 2 Zeichen. Bei jeden Zusätzlichen Operator: nn += 1
            i = 2
            for y in range(2, len(string)):
                if y in operators:
                    nn += 1
                elif y in symbols:
                    nn -= 1
                i += 1
                if nn == 0:
                    if sym == "+":
                        return AddFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "-":
                        return SubFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "*":
                        return MulFunction(parse1(string[1:i]), parse1(string[i:]))
                    if sym == "/":
                        return DivFunction(parse1(string[1:i]), parse1(string[i:]))
                    break



test = "+96"

print(parse1(test))