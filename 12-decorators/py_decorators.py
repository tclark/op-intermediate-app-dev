# These are just some examples for you to experiment with.


import functools

def shouty(wrapped_fn):
    @functools.wraps(wrapped_fn)
    def wrapper(*args, **kwargs):
        msg = wrapped_fn(*args, **kwargs)
        return msg.upper()
    return wrapper


@shouty
def hello():
    return 'hello'  

def shouty_or_not(choice):
    def maybe(wrapped_fn):
        @functools.wraps(wrapped_fn)
        def wrapper(*args, **kwargs):
            msg = wrapped_fn(*args, **kwargs)
            if choice:
                return msg.upper()
            else:
                return msg  
        return wrapper
    return maybe

@shouty_or_not(True)
def we_will_see():
    return 'might be shouty'




def shouty_or_backwards(choice):
    
    if choice == 'shouty':
        def shouty(wrapped_fn):
            @functools.wraps(wrapped_fn)
            def wrapper(*args, **kwargs):
                msg = wrapped_fn(*args, **kwargs)
                return msg.upper()
            return wrapper
        return shouty   
    elif choice == 'backwards':       
        def backwards(wrapped_fn):
            @functools.wraps(wrapped_fn)
            def wrapper(*args, **kwargs):
                msg = wrapped_fn(*args, **kwargs)
                return msg[::-1]
            return wrapper
        return backwards
    else:       
        def unchanged(wrapped_fn):
            return wrapped_fn
        return unchanged
            

@shouty_or_backwards('shouty')
def ex1():
    return 'shouty'  

@shouty_or_backwards('backwards')
def ex2():
    return 'sdrawkcab'  

@shouty_or_backwards('neither')
def ex3():
    return 'neither shouty nor backwards'  


if __name__ == '__main__':
    
    print(hello())    

    print(we_will_see())    

    print(ex1())
    print(ex2())
    print(ex3())
