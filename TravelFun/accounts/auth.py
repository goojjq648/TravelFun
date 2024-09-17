from .models import Member
from django.contrib.auth.hashers import check_password


# 自定義的認證函式
def authenticate_member(username, password):
    try:
        member = Member.objects.get(username=username)
        if check_password(password, member.password):
            return member
    except Member.DoesNotExist:
        return None
    return None