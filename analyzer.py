from jaz_parser import Parser, JazInstruction
from stack import Stack
from file_handler import Read

datastack = Stack()
Push = datastack.Push
Pop = datastack.Pop

class Scope:
       def __init__(self,isMainScope):
               self.variables = {}
               self.isPassingParameters = True
               self.isAfterCall = False
               self.inCall = False
               self.beforeCall = True
               self.returnLine = 0
               self.isMainScope = isMainScope

def operation(function):
    op2 = int(Pop())
    op1 = int(Pop())
    res = function(op1, op2)
    Push(int(res))

def jazNot():
    op1 = Pop()
    Push(int(bool(op1)))

def CallAnalyzer(filename):
        scopes = []

        lines = Read(filename)
        jazParser = Parser()
        jazParser.ParseJazFile(lines)

        currentline = 0

        scopes.insert(0, Scope(True))

        while currentline < len(lines):
                instruction = jazParser.GetInstruction(currentline)
                arguments = instruction.arguments
                instructionName = instruction.name

                scopeVars = scopes[0].variables
                scopeLevels = len(scopes)

                if instruction.name == "show":
                        #argStr = ' '.join(arguments)
                        print(arguments)
                elif instruction.name == "push":
                        Push(arguments[0])
                elif instruction.name == "rvalue":
                        variableName = arguments[0]
                        if scopes[0].isMainScope or scopes[0].inCall or scopes[0].isAfterCall:
                                Push(scopes[0].variables.get(variableName, 0))
                        else:
                                Push(scopes[1].variables.get(variableName, 0))
                elif instruction.name == "lvalue":
                        Push(arguments[0])
                elif instruction.name == "gofalse":
                        poppedVal = Pop()
                        if bool(poppedVal) == False:
                                currentline = instruction.jumplocation
                                continue
                elif instruction.name == "gotrue":
                        if bool(Pop()) == True:
                                currentline = instruction.jumplocation
                                continue
                elif instruction.name == "goto":
                        currentline = instruction.jumplocation
                        continue
                elif instruction.name == "pop":
                        Pop()
                elif instruction.name == ":=":
                        rval = Pop()
                        lval = Pop()
                        if scopes[0].isMainScope or scopes[0].beforeCall or scopes[0].inCall:
                                scopes[0].variables[lval] = rval
                        else:
                                scopes[1].variables[lval] = rval
                elif instruction.name == "copy":
                        copyVal = Pop()
                        Push(copyVal)
                        Push(copyVal)
                elif instruction.name == "print":
                        printVal = Pop()
                        Push(printVal)
                        print(printVal)
                elif instruction.name == "begin":
                        scopes.insert(0, Scope(False))
                elif instruction.name == "end":
                        scopes.pop(0)
                elif instruction.name == "return":
                        currentline = scopes[0].returnLine
                        scopes[0].isAfterCall = True
                        scopes[0].inCall = False
                        continue
                elif instruction.name == "call":
                        scopes[0].returnLine = currentline + 1
                        scopes[0].beforeCall = False
                        scopes[0].inCall = True
                        currentline = instruction.jumplocation
                        continue
                elif instruction.name == "+":
                        operation(lambda x, y: x + y)
                elif instruction.name == "-":
                        operation(lambda x, y: x - y)
                elif instruction.name == "*":
                        operation(lambda x, y: x * y)
                elif instruction.name == "/":
                        operation(lambda x, y: x / y)
                elif instruction.name == "div":
                        operation(lambda x, y: x % y)
                elif instruction.name == "&":
                        operation(lambda x, y: x and y)
                elif instruction.name == "!":
                        jazNot()
                elif instruction.name == "|":
                        operation(lambda x, y: x or y)
                elif instruction.name == "<>":
                        operation(lambda x, y: x != y)
                elif instruction.name == "<=":
                        operation(lambda x, y: x <= y)
                elif instruction.name == ">=":
                        operation(lambda x, y: x >= y)
                elif instruction.name == "<":
                        operation(lambda x, y: x < y)
                elif instruction.name == ">":
                        operation(lambda x, y: x > y)
                elif instruction.name == "=":
                        operation(lambda x, y: x == y)
                elif instruction.name == "halt":
                        quit()
                else:
                        currentline += 1
                        continue
                currentline += 1
