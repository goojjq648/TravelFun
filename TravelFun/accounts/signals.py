from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Member

# 當 User 實例創建時，創建對應的 Member 實例
@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email
        )

# 當 User 實例保存時，也保存對應的 Member 實例
@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    if hasattr(instance, 'member'):
        instance.member.save()
    else:
        Member.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email
        )
