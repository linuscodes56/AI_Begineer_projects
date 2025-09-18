
# EG1: hide the implementation details of fx

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Called fx: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def get_input():
    pass 

@my_decorator
def validate_input():
    pass 

@my_decorator
def save_to_db():
    pass 

@my_decorator
def register_user():
    get_input()
    validate_input()
    save_to_db() 

register_user() # Only the process is exposed, not internal details
