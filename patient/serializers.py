from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = PatientModel
        fields = '__all__'

class PatientRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        if password != password2:
            raise serializers.ValidationError({'error': 'Password doesnt matched'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password)
        print(account)
        account.save()
        return account
    