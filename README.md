# SpeedPay-BE-Test
A mini-prototype mock api with limited functionalities which facilitates user wallet creations, 

## API DOCUMENTATION LINK
https://documenter.getpostman.com/view/15065406/2s8Yeixvw2




## installation
install required packages:
  -> Django==4.1.3
    django-cors-headers==3.13.0
    djangorestframework==3.14.0
    djangorestframework-simplejwt==5.2.2
    PyJWT==2.6.0
    requests==2.28.1

 
to run server
    -> python3 manage.py runserver

to sync database
    -> python3 manage.py migrate --run-syncdb   

## Endpoints
EndPoints                     -         Method 

1 /api/signup/                - POST 
2 /api/authentication/login/  - POST
3 /api/authentication/logout/ - GET
4 /api/userdeposit/           - POST 
5 /api/withdrawal/            - POST
6 /api/accountdetails/        - GET
