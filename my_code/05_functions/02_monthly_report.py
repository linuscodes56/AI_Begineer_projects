

def print_fx_name(func):
    def wrapper(*args, **kwargs):
        print(f"called function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_fx_name
def fetch_sales():
    pass 

@print_fx_name
def filter_valid_orders():
    pass 

@print_fx_name
def summarize_data():
    pass 

@print_fx_name
def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()

generate_report()
