from rest_framework import serializers
from .models import Posts
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Password')
    password2 = serializers.CharField(label='Repeat password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise serializers.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'img', 'name', 'desc', 'slug')


