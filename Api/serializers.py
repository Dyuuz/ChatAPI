from rest_framework import serializers
from .models import User, Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # 
        model = User
        fields = ['id', 'username','password','tokens']
        extra_kwargs = { 'password' : {'write_only' : True }}
    
    def create(self, validated_data):
        try:
            # Create a new user and use user variable as the instance of the username
            user = User.objects.create(username = validated_data['username'])
            
            # hash the password
            user.set_password(validated_data['password']) 
            
            # save to database
            user.save() 
            
            # return the created user
            return user 
        
        # 
        except Exception as e:
            return f"Error: {str(e)}"