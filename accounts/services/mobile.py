import random
import string

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q
from accounts.models import UserAuthToken

User = get_user_model()


def user_login(username: str, password: str):
    res = {}
    user = check_user(username, password)
    auth_token = generate_auth_token(user)
    with transaction.atomic():
        login_info_save(user, auth_token)

    res["auth_token"] = auth_token
    res["username"] = user.username
    res["name"] = user.get_full_name()
    res["type"] = user.type
    return res


def check_user(username: str, password: str):
    try:
        user = User.objects.get(username=username)
        if user.is_disabled:
            raise ValidationError(
                "Account has been deactivated.Please contact admin for any resolution"
            )
        success = user.check_password(password)
        if not success:
            raise User.DoesNotExist
        return user
    except User.DoesNotExist:
        raise ValidationError("Invalid Username or Password")


def generate_auth_token(user):
    string_chars = string.ascii_lowercase + string.digits
    token = "".join(random.choice(string_chars) for _ in range(15))
    while UserAuthToken.objects.filter(key=token).exists():
        token = "".join(random.choice(string_chars) for _ in range(15))
    UserAuthToken.objects.filter(user=user).update(is_expired=True)
    return token


def login_info_save(user, auth_token):
    user_auth_token = UserAuthToken.objects.filter(user=user)
    if user_auth_token.exists():
        user_auth_token = user_auth_token[0]
        user_auth_token.key = auth_token
        user_auth_token.is_expired = False
    else:
        user_auth_token = UserAuthToken(
            user=user, key=auth_token, created_by=user, modified_by=user
        )
    user_auth_token.save()