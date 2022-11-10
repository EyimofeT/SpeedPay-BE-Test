from rest_framework.response import Response
from rest_framework.decorators import api_view

# from ..api.serializers import UserSerializer, UserLoginSerializer, UserCreatedSerializer, UserDepositSerializer
# from ..api.models import User
# from ..api.serializers import UserSerializer
# from ..api import helpers
# from ..api.serializers import UserSerializer
import sys
sys.path.append("..")
from api.serializers import UserSerializer
from api.models import User
# import api.serializers.UserSerializer 
import re
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
import json
import jwt
import datetime


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

    username_input = request.data['username'].lower()
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
