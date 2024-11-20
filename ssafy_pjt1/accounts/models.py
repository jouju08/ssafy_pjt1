from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from finlife.models import DepositProducts

from allauth.account.adapter import DefaultAccountAdapter

    
class User(AbstractUser):
    subscribed_products = models.ManyToManyField(DepositProducts, blank=True)  # 가입한 상품 목록
    income=models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    job=models.TextField(blank=True, null=True)
    birth = models.DateField(null=True, blank=True)
    phone=PhoneNumberField(region='KR', unique=True, null=True)
    main_bank=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        phone = data.get("phone")
        birth = data.get("birth")
        income = data.get("income")
        job = data.get("job")
        main_bank = data.get("main_bank")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if phone:
            user_field(user, "phone", phone)
        if birth:
            user_field(user, "birth", birth)
        if income:
            user_field(user, "nickname", income)
        if job:
            user_field(user, "job", job)
        if main_bank:
            user_field(user, "main_bank", main_bank)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user