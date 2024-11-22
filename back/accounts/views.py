from django.shortcuts import render
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.http import JsonResponse
from django.contrib.auth import get_user_model

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def check_username(request):
    try:
        username = request.GET.get('username')
        User = get_user_model()
        if username is None:
            return JsonResponse({'error': 'Username is required'}, status=400)

        # 사용자 이름이 이미 존재하는지 체크
        if User.objects.filter(username=username).exists():
            return JsonResponse({'isAvailable': False})
        return JsonResponse({'isAvailable': True})
    except Exception as e:
        # 예외가 발생하면 로깅하고 500 에러를 반환
        print(f"Error in check_username view: {str(e)}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)