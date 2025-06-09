import datetime

# 💡 Decorator: To log function execution time
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Finished function: {func.__name__}")
        return result
    return wrapper

# 💡 Closure: Greeting generator
def greeting_creator(greeting):
    def greeter(name):
        return f"{greeting}, {name}! Welcome to the system."
    return greeter  # This is a closure
        

# 🎯 Function using closure + decorator
@logger_decorator
def generate_and_display_greeting(greeting, name):
    greeter_func = greeting_creator(greeting)  # Closure used here
    message = greeter_func(name)
    print(message)

# 📌 Example calls
if __name__ == "__main__":
    generate_and_display_greeting("Hello", "Pooja")
    generate_and_display_greeting("Namaste", "Sapana")
    generate_and_display_greeting("Hi", "Anusha")
