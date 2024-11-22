from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from finlife.models import DepositProducts
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from allauth.account.adapter import DefaultAccountAdapter

    
class User(AbstractUser):
    profile_image=ProcessedImageField(
        blank=True,
        upload_to='profile_image/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality':70},
    )
    subscribed_products = models.ManyToManyField(DepositProducts, blank=True)  # 가입한 상품 목록
    income=models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    job=models.TextField(blank=True, null=True)
    birth = models.DateField(null=False, blank=False)
    phone=PhoneNumberField(region='KR', unique=True, null=False, blank=False)
    main_bank=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        profile_image=data.get('profile_image', '')
        subscribed_products=data.get("subscribed_products",[])
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
        if profile_image:
            user_field(user, "profile_image", profile_image)
        if subscribed_products:
            user.subscribed_products.set(subscribed_products)
        if phone:
            user_field(user, "phone", phone)
        if birth:
            user_field(user, "birth", birth)
        if income:
            user_field(user, "income", income)
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