from datetime import datetime

def count_time(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        func(*args, **kwargs)
        then = datetime.now()
        time_count = then - now 
        print(f"time_taked ---> {time_count.seconds}")
    
    return wrapper