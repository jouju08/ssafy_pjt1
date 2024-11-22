from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer
from finlife.models import DepositProducts  
from django.contrib.auth import get_user_model

#추가 필드 처리: 커스텀 직렬화
class CustomRegisterSerializer(RegisterSerializer):
    profile_image=serializers.ImageField(use_url=True)
    subscribed_products = serializers.PrimaryKeyRelatedField(queryset=DepositProducts.objects.all(), many=True, required=False)
    birth = serializers.DateField(required=True)  # 생년월일
    phone = serializers.CharField(required=True)  # 전화번호
    email = serializers.EmailField(required=True)
    income = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)  # 소득
    job = serializers.CharField(required=False)  # 직업
    main_bank = serializers.CharField(required=False)  # 주 은행
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)

    def get_cleaned_data(self):#데이터 검증 후 출력
        print("Validated Data:", self.validated_data)
        return {
            'profile_image':self.validated_data.get('profile_image', None),
            'subscribed_products':self.validated_data.get('subscribed_products', []),
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
        user_data = self.get_cleaned_data()#검증된 데이터 가져오기
        
        user = UserModel.objects.create_user(#가져온 데이터로 create user
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password1'],
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            profile_image=user_data.get('profile_image',None),
            phone=user_data['phone'],
            birth=user_data['birth'],
            income=user_data.get('income', None),
            job=user_data.get('job', ''),
            main_bank=user_data.get('main_bank', ''),
        )
        subscribed_products = user_data['subscribed_products']
        user.subscribed_products.set(subscribed_products)
        return user#생성된 사용자 객체 반환
    
UserModel = get_user_model()#현재 사용자 모델 변수로 저장

class CustomUserDetailsSerializer(UserDetailsSerializer):#사용자 세부 정보 반환 직렬화
    class Meta:
        extra_fields = []#기본 UserDetailSerializer를 확장하기 위한 배열
        if hasattr(UserModel, 'USERNAME_FIELD'):#속성이 존재하면 true를 반환하는 함수
            extra_fields.append(UserModel.USERNAME_FIELD)#존재하면 추가 필드에 값 append
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel,'profile_image'):
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
        if hasattr(UserModel, 'subscribed_products'):
            extra_fields.append('subscribed_products')
            
        # 추가된 필드
        if hasattr(UserModel, 'is_active'):
            extra_fields.append('is_active')
        if hasattr(UserModel, 'is_staff'):
            extra_fields.append('is_staff')
        if hasattr(UserModel, 'last_login'):
            extra_fields.append('last_login')
        model = UserModel#직렬화에 사용할 모델 지정
        fields = ('pk', *extra_fields)#직렬화에 포함할 필드 지정
        read_only_fields = ('email',)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('username', 'email')