from error_handler import GenerateError

class JazInstruction:
        def __init__(self, name, arguments, jumplocation):
                self.name = name
                self.arguments = arguments
                self.jumplocation = jumplocation

class Parser:
        def __init__(self):
                self.Instructions = []
                self.Arguments = []
                self.Labels = {}

        def ParseJazFile(self, lines):
                validCommands = ["push", "rvalue", "lvalue", "pop", ":=", "copy",
                "label", "goto", "gofalse", "gotrue", "halt", "+", "-", "*", "/",
                "div", "&", "!", "|", "<>", "<=", ">=", "<", ">", "=", "print",
                "show", "begin", "end", "return", "call", "//"]

                inMultilineComment = False
                index = 0

                for line in lines:
                        split_line = line.split()
                        if line == "\n" or len(split_line) == 0:
                                self.Instructions.append("\n")
                                self.Arguments.append("\n");
                                index += 1
                                continue
                        jaz_command = split_line[0]

                        if jaz_command == "/*":
                            inMultilineComment = True
                        elif jaz_command == "*/":
                            inMultilineComment = False
                        elif (jaz_command not in validCommands) and (not inMultilineComment):
                            GenerateError("Invalid Command", split_line[0])
                         
                        if jaz_command == "label":
                                self.Labels[split_line[1]] = int(index)
                        self.Instructions.append(jaz_command)
                        
                        if jaz_command == "show":
                                command_start_pos = line.find(jaz_command)
                                command_end_pos = command_start_pos + len(jaz_command)
                                line_end_without_newline = len(line) - 1
                                
                                argument = line[command_end_pos + 1:line_end_without_newline]
                        else:
                                argument = []
                                for i in range(1,len(split_line)):
                                        argument.append(split_line[i])
                        self.Arguments.append(argument)
                        index += 1

        def GetInstruction(self, index):
                jumpToLine = index + 1
                if self.Instructions[index] == "goto" or self.Instructions[index] == "call" or self.Instructions[index] == "gotrue" or self.Instructions[index] == "gofalse":
                        labelname = self.Arguments[index][0]
                        jumpToLine = self.Labels[labelname] + 1
                return JazInstruction(self.Instructions[index], self.Arguments[index], jumpToLine)
