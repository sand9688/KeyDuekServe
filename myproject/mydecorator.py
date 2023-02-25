def route(func):
    def wrapper():
        print("in wrapper")
        
        func()
        
    return wrapper

def hello_pybo():
    print("hello, Pybo!")

hello = route(hello_pybo)
# %%
@trace
def hello():
    print("hello")
    
# %%


class Trace:
    def __init__(self,func):
        self.func = func
        
        
    def __call__(self):
        print("in wrapper")
        self.func()
        
@Trace
def hello():
    print("hello")

hello = Trace(hello)

hello()
# %%
