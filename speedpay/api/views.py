from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, UserLoginSerializer, UserCreatedSerializer, UserDepositSerializer
from .models import User
from .serializers import UserSerializer
from . import helpers
import re
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
import json
import jwt
import datetime


@api_view(['GET'])
def apiOverview(request):
    list = {
        "User SignUp": "/api/signup/",
        "User LogIn": '/api/login/',
         "User LogOut": '/api/logout/',
        "User Deposit": "/api/userdeposit/",
        "Users Withdrawal": '/api/withdrawal/',
        "Users Account Details": '/api/accountdetails/',

    }
    return Response(list)


@api_view(['POST'])
def userCreate(request):
    try:

        # request.data['first_name']=request.data['first_name'].capitalize()
        # request.data['last_name']=request.data['last_name'].capitalize()
        request.data['username'] = request.data['username'].lower()
        request.data['email'] = request.data['email'].lower()
        request.data
        # print(request.data)
        serializer = UserSerializer(data=request.data)
        request.data['balance'] = float(0)
        request.data['account_number'] = helpers.generate_account_number()
        uname = str(request.data['username'])
        email = str(request.data['email'])
        uniqueUsernameStatus = helpers.checkUsernameInput(uname)
        uniqueEmailStatus = helpers.checkEmailInput(email)
        # print("here")
        # print(uniqueEmailStatus)
        if uniqueUsernameStatus == True and uniqueEmailStatus == True:

            if serializer.is_valid():
                serializer.save()

                user = User.objects.all().last()
                serializer = UserCreatedSerializer(user)

                response = {
                    "Status": "200",
                    "data": [
                       serializer.data
                    ]
                }
            else:
                response = {
                    "Error: User Not Created : Check Input"
                }
        elif uniqueUsernameStatus == False and uniqueEmailStatus == True:
            response = {
                "Error: Username Already Exists"
            }
        elif uniqueUsernameStatus == True and uniqueEmailStatus == False:
            response = {
                "Error: Email Already Exists"
            }
        elif uniqueUsernameStatus == False and uniqueEmailStatus == False:
            response = {
                "Error: Username and Email Already Exists"
            }

    except Exception as e:  # work on python 2.x
        # logger.error('Failed to upload to ftp: '+ str(e))
        response = {
            "Error Occured": str(e)
        }

    return Response(response)


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
         "status": 200,
        'Message': 'Logout Successful'
    }
    return response


@api_view(['POST'])
def userLogin(request):

    username_input = request.data['username']
    password_input = request.data['password']
    user = User.objects.filter(username=username_input).first()
    user_serializer = UserSerializer(user, many=False)

    if user is None:
        raise AuthenticationFailed("User not Found!")

    if not user.check_password(password_input):
        raise AuthenticationFailed("Incorrect Password!")

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
        "is_superuser": user.is_superuser,

    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    # .decode('utf-8')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        "Message": "Login Successful",
        "Status": 200,
        'jwt': token
    }

    # return Response(user_serializer.data)
    return response


@api_view(['GET'])
def accountdetails(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')

    user = User.objects.filter(id=payload['id']).first()
    # user = User.objects.get(id=payload['id'])
    serializer = UserCreatedSerializer(user)

    return Response(serializer.data)
    # return Response(token)


@api_view(['POST'])
def deposit(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        user = User.objects.get(id=payload["id"])
        if(float(request.data['amount'])>0):
            current_balance = user.balance
            new_balance = current_balance + float(request.data['amount'])
            user.balance = new_balance

            user.save()
            response = {
                "status": 200,
                "message": "Deposit Successful"
            }
        else:
             response = {
                 
                "status": 400,
                "message": "Invalid Amount "
            }
        
    except KeyError:
          response ={
            "status": 400,
            "message" : "Missing Amount"
          }
    except ValueError:
         response ={
            "status": 400,
            "message" : "Invalid Amount"
          }

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')

    # users = User.objects.get(id=pk)
    return Response(response)


@api_view(['POST'])
def withdrawal(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try:
        
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
      
        user = User.objects.get(id=payload["id"])
        current_balance=user.balance
        if(current_balance >= float(request.data['amount'])):
            new_balance=current_balance -  float(request.data['amount'])
            user.balance=new_balance
        
            user.save()
            response={
                "status": "200",
                "message" : "Withdrawal Successful"
        }
        else:
            response={
                "status": "400",
                "message" : "Insufficient Funds"
            }
    
    except KeyError:
          response ={
            "status": "400",
            "message" : "Missing Amount"
          }
    except ValueError:
         response ={
            "status": "400",
            "message" : "Invalid Amount"
          }

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthorized')
    
    # users = User.objects.get(id=pk)
    return Response(response)