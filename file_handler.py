from error_handler import GenerateError

def Read(filename):
        try:
            file = open(filename, "r")
            lines = file.readlines()
        except FileNotFoundError:
            GenerateError("File Not Found")
        finally:
            file.close()

        return lines
