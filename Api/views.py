from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User, Chat , Token
from django.contrib.auth import authenticate, login, logout
from .utils import *
import uuid

# Create your views here.

# Redirect to user registration page
def home(request):
    return redirect('user-register')

# User Registration Class View Function
class UserRegistration(APIView):
    def post(self, request):
        try:
            # pass icnoming data to serializer from API request
            serializer = UserSerializer(data=request.data)
            
            # checks if the data is unique/valid
            if serializer.is_valid(): 
                
                # calls the create function in serializer script to create user using the data provided in Json
                serializer.save()
                
                # Return feedback for successful registration 
                return Response(
                    {"message" : f"{serializer.data['username']} registered successfully!"}, 
                    status=status.HTTP_200_OK)
                
            # Feedback for invalid input  
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Handles error exception 
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
# UserLogin Class View Function
class UserLogin(APIView):
    def post(self, request):
        try:
            # pass icnoming data to variable data from client side
            data = request.data
            print(data)
            # Feedback if no data is inputted from client side
            if not data:
                return Response({"username" : "This field is required", "password" : "This field is required"},
                    status=status.HTTP_401_UNAUTHORIZED)
              
            # Get user details from client side if data exists
            username = data.get('username')
            password = data.get('password')

            # Feedback if one of the inputs is invalid 
            if not username or not password:
                return Response({"error" : "Make sure you have username and password in your request"}, 
                    status=status.HTTP_401_UNAUTHORIZED)
                
            # Ratify user input to keep the user logged in
            user = authenticate(request, username=username, password=password)

            try:
                # Proceeds with if after user is successfully authenticated
                if user.is_authenticated:
                        login(request, user)
                        auth_token = str(uuid.uuid4())
                        user = request.user
                        user_instance = User.objects.get(username=username)
                        token_instance = Token.objects.filter(user__username=user_instance.username)
                        
                        # Rotate user token if the logged in user already has a token
                        if token_instance.exists():
                            token = Token.objects.get(user__username=user.username)
                            token.token = auth_token
                            token.save()
                            return Response({"Token": auth_token}, status=status.HTTP_200_OK)
                        
                        # Create a new token for user if they are just logging in for the first time
                        else:
                            Token.objects.create(token=auth_token, user=user)
                            
                            # Feedback after token creation
                            return Response({"Token": auth_token}, status=status.HTTP_200_OK)
                        
                else:
                    return Response({"error" : "Invalid login details"},
                                status=status.HTTP_400_BAD_REQUEST) 
                    
            except:
                return Response({"error" : "Invalid login details"},
                                status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(
              {"error": f"An unexpected error occurred: {str(e)}"},
              status=status.HTTP_500_INTERNAL_SERVER_ERROR
           )
          
# Chat API Class View Function
class ChatAPI(APIView):
    def post(self, request):
        try:
            # pass incoming data to variable data from client side
            data = request.data

            #Feedback if no data is inputted from client side
            if not data:
                return Response({"token" : "This field is required",
                                "message" : "This field is required"},
                    status=status.HTTP_400_BAD_REQUEST)
              
            # Get input details from client side if data exists
            token = data.get('token')
            message = data['message']
            
            # Feedback if one of the input is invalid
            if not token or not message:
                return Response({"error" : "Make sure you have message and token in your request"}, 
                    status=status.HTTP_400_BAD_REQUEST)
            
            # Get user instance 
            try:
                user = request.user
                if user:
                    
                    # Check if user has enough token to ask a question
                    if user.tokens < 100:
                        return Response({"error" : "Insufficient token, you need at least 100 tokens to ask a question"}, 
                            status=status.HTTP_400_BAD_REQUEST)
                        
                    else:
                        # Verify if token exists from DB
                        try:
                            token = Token.objects.get(token=token)
                            # Proceeds with if statement if user exists
                            if token:
                                response = get_ai_response(message)
                                user.tokens -= 100
                                user.save()
                                
                                # Checks if user has asked the same question
                                duplicate_message_check = Chat.objects.filter(message=message)
                                
                                # If user has asked, response will be generated from database 
                                if duplicate_message_check.exists():
                                    duplicate_instance = Chat.objects.get(message=message)
                                    return Response({"Message": duplicate_instance.message, 
                                                    "Response": duplicate_instance.response}, status=status.HTTP_200_OK)
                                
                                # Generate new response if the question is new from the user
                                Chat.objects.create(user=user, message= message, response=response)
                        
                                # Outputs new response to user
                                return Response({"Message": message, 
                                        "Response": response}, status=status.HTTP_201_CREATED)
                            
                            else:
                                return Response({"error" : "Invalid token"}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                        except:
                            return Response({"error" : "Invalid token, input your last generated token on login"}, 
                                status=status.HTTP_400_BAD_REQUEST)
                            
            except Exception as e:
                return Response(
                    {"error": f"pls login before making a chat request"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        except Exception as e:
            return Response(
                {"error": f"Make sure you have message and token in your request"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    
# Balance Class View Function
class Balance(APIView):
    def post(self, request):
        try:
            # pass incoming data to variable data from client side
            data  = request.data

            # Feedback if no data is inputted from client side
            if not data:
                return Response({"token" : "This field is required"},
                    status=status.HTTP_400_BAD_REQUEST)
                
            # Get user details from client side if data exists
            token = data['token']
            
            # Feedback if none of the input is invalid
            if not token:
                return Response({"error" : "Token is required"}, 
                    status=status.HTTP_400_BAD_REQUEST)
            
            user = request.user
            
            # if user is not logged in, it will return an error
            if user in list(User.objects.all()):
                    token = Token.objects.get(token=token)
                    token_balance = token.user.tokens
                    return Response({"User" : user.username , "Balance" : token_balance }, status=status.HTTP_200_OK)
            else: 
                return Response({"error" : "login before checking balance"},        
                status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )