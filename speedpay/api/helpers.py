import math
import random
# from .serializers import UserSerializer, UserLoginSerializer
from .models import User
from .serializers import UserSerializer

def checkUsernameInput(input_username):
    try: 
        username_check = User.objects.get(username=input_username)
        # username_serializer = UserSerializer(instance=username_check,many=False)
        # if username_serializer is not None:
        #     return False
        if username_check:
            return False
        
    except:
        # response= {"An Error Has Occured"}
            return True

def checkEmailInput(input_email):
    try:
            email_check = User.objects.get(email=input_email)
            # username_check = User.objects.get(username=uname)
            # email_serializer = UserSerializer(instance=email_check,many=False)
            # if email_serializer is not None:
            #     return False
            if email_check:
                return False
            # elif email_check==username_check:
            #     print("Here")
            #     return True
    except:
            return True
        
        
def generate_account_number():
        # importing modules


    ## storing strings in a list
        digits = [i for i in range(0, 10)]

# initializing a string
        random_str = ""

# we can generate any lenght of string we want
        for i in range(10):
    ## generating a random index
    ## if we multiply with 10 it will generate a number between 0 and 10 not including 10
    ## multiply the random.random() with length of your base list or str
            index = math.floor(random.random() * 10)

            random_str += str(digits[index])

# displaying the random string
        # print(random_str)
        try:
            account_check = User.objects.get(account_number=random_str)
            #     return False
            if account_check:
                generate_account_number()
         
        except:
            return random_str
        
        