from .models import Member
from django.contrib.auth.hashers import check_password


# 自定義的認證函式
def authenticate_member(username, password):
    try:
        member = Member.objects.get(username=username)
        if member.check_password(password):  # 使用 check_password 來驗證密碼
            return member
        return None
    except Member.DoesNotExist:
        return None