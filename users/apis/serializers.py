from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from ..models import User
from rest_framework.validators import ValidationError

class Tokens :

    @property
    def tokens (self):
        user = self.user
        tokens = RefreshToken.for_user(user=user)
        return {
            'token' : str(tokens.access_token)
        }


class LoginSerializer (serializers.Serializer, Tokens):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid email"
            })
        
        if not user.check_password(password) : 
            raise ValidationError({
                'message' : "invalid password"
            })
        
        self.user = user
        return attrs
    

class RegisterSerializer (serializers.ModelSerializer, Tokens):
    
    class Meta:
        model = User
        fields = ('full_name','email','password',)

    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        return self.user