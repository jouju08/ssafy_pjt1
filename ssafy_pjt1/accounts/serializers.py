from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer

from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField(required=True)  # 생년월일
    phone = serializers.CharField(required=True)  # 전화번호
    email = serializers.EmailField(required=True)
    income = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)  # 소득
    job = serializers.CharField(required=False)  # 직업
    main_bank = serializers.CharField(required=False)  # 주 은행
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)

    def get_cleaned_data(self):
        print("Validated Data:", self.validated_data)
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'birth': self.validated_data.get('birth', ''),
            'income': self.validated_data.get('income', ''),
            'job': self.validated_data.get('job', ''),
            'phone': self.validated_data.get('phone', ''),
            'main_bank': self.validated_data.get('main_bank', ''),
        }
    def save(self, request):
        user_data = self.get_cleaned_data()

        # 사용자 모델에 저장
        user = UserModel.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password1'],
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            phone=user_data['phone'],
            birth=user_data['birth'],
            income=user_data.get('income', None),
            job=user_data.get('job', ''),
            main_bank=user_data.get('main_bank', '')
        )
        
        return user
    
UserModel = get_user_model()

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'phone'):
            extra_fields.append('phone')
        if hasattr(UserModel, 'birth'):
            extra_fields.append('birth')
        if hasattr(UserModel, 'income'):
            extra_fields.append('income')
        if hasattr(UserModel, 'job'):
            extra_fields.append('job')
        if hasattr(UserModel, 'main_bank'):
            extra_fields.append('main_bank')
        # 추가된 필드
        if hasattr(UserModel, 'is_active'):
            extra_fields.append('is_active')
        if hasattr(UserModel, 'is_staff'):
            extra_fields.append('is_staff')
        if hasattr(UserModel, 'last_login'):
            extra_fields.append('last_login')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('username', 'email')