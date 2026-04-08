try:
    x = int("float") 
    inv = 1 / 4
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")