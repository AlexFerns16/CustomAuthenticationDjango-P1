from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from custom_auth.models import CustomUser


class CustomAuthBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            usercode = kwargs.get(UserModel.USERNAME_FIELD)
        var = input("enter '1' and press 'enter key' for authentication: ")
        if var == 1:
            user = CustomUser.objects.get(usercode=usercode)
            if user.check_password(password):
                return user
        else:
            return None
        return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
