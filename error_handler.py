def GenerateError(errorType, arg=""):
    if errorType == "Invalid Command":
        print("Parse Error: " + str(arg) + " is not a valid command.")
    elif errorType == "File Not Found":
        print("File Error: File was not found. Check the path to file.")
    elif errorType == "Stack Underflow":
        print("Stack Undeflow Error: Tried to pop from an empty stack.")
    else:
        print("Unknown error occured.")

    quit()
