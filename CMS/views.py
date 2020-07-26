# import pyrebase
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib import auth
# import AuthPage
#
# firebaseConfig = {
#     'apiKey': "AIzaSyDKeAyog5zIDCqunVx_UBQbYWaqUEhGHT4",
#     'authDomain': "test-project-bcd07.firebaseapp.com",
#     'databaseURL': "https://test-project-bcd07.firebaseio.com",
#     'projectId': "test-project-bcd07",
#     'storageBucket': "test-project-bcd07.appspot.com",
#     'messagingSenderId': "411890268348",
#     'appId': "1:411890268348:web:b293eab1d31f5ccbaf78b9",
#     'measurementId': "G-9HZC5PJ3Y9"
# }
#
# firebase = pyrebase.initialize_app(firebaseConfig)
#
# authen = firebase.auth()
# database = firebase.database()
#
#
# def cms(request):
#     return render(request, 'addDecision.html')
#
#
# def post_decision(request):
#     token = AuthPage.views.login.uid
#     print(token)
#     return render(request, 'addDecision.html')
