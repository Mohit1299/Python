def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper
def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper
def underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@bold
@italic
@underline
def print_String():
    str1 = input("Please Enter String : ")
    return str1
print(print_String())   
