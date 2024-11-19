from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from finlife.models import DepositProducts

    
class User(AbstractUser):
    subscribed_products = models.ManyToManyField(DepositProducts, blank=True)  # 가입한 상품 목록
    income=models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    job=models.TextField(blank=True, null=True)
    birth=models.DateField(auto_now=False, auto_now_add=False)
    phone=PhoneNumberField(region='KR', unique=True)
    main_bank=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
