'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''


class CustomInputError(Exception):
    pass


class Typecastcheck(TypeError):
    def __init__(self):
        print("the data type of input is not valid!!!")


class ZeroException(ZeroDivisionError):
    def __init__(self):
        print("Divide by zero error!!!")
