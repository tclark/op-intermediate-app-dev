# Mocking is mainly used for testing, but it has other uses as well. 
# Sometimes we are developing a module that depends on other parts
# of the project that are not availbale yet. In cases like this we can 
# use mocks to provide substitutes for the real objects we will add
# later. A MagicMock is particularly good for this. 
# (https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock)


# Since the User class isn't ready, you'll need to use a Mock
# from nonexistent_user import User 
# A User should have
#   uid : int
#   username : str
#   roles: a list of str
#   a __str__ method that give a string in the format "id_: username"
#   to_json : a method that returns JSON string with the above fields

from unittest.mock import MagicMock

if __name__ == '__main__':

    user = MagicMock()
    # configure your mock User here


    # Your mock User should work with the code below:
    
    print(user)
    
    if 'admin' in user.roles:
        print(f'{user.username} is an admin')
    else:
        print(f'{user.username} is not an admin')
    
    next_id = user.uid + 1
    print(next_id)

    print(user.to_json())

