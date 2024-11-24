from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
import openai
from openai.error import OpenAIError #꼭 버전 0.28.0으로 해야됨
import logging
from rest_framework.permissions import IsAuthenticated
from .models import Portfolio
from accounts.models import User

# 로깅 설정


openai.api_key = settings.CHATBOT_API_KEY

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def chat(request):
    if request.method == "POST":
        data = request.data
        user_content = data.get("message")
        
        # 메시지 데이터 검증
        if not user_content:
            return JsonResponse({"error": "메시지 내용이 없습니다."}, status=400)
        
        messages = data.get("messages", [])
        messages.append({"role": "user", "content": f"{user_content}"})
        
        try:
            completion = openai.ChatCompletion.create(model="gpt-4-turbo", messages=messages)
            assistant_content = completion.choices[0].message["content"].strip()
            messages.append({"role": "assistant", "content": assistant_content})
            return JsonResponse({"response": assistant_content, "messages": messages})
        
        # OpenAIError를 직접 임포트한 경우를 대비해 수정
        except OpenAIError as e:
            logging.Logger.error(f"OpenAIError 발생: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def make_portfolio(request):
    if request.method == "GET":
        # portfolio=Portfolio.objects.get(user=request.user)
        # user_info=request.user
        # type_of=portfolio.type_of
        # income=user_info.income
        type_of='안정형'
        income=2000
        # 메시지 데이터 검증
        if not income:
            return JsonResponse({"error": "자산 정보가 필요합니다."}, status=400)
        if not type_of:
            return JsonResponse({"error": "투자 성향 정보가 필요합니다."}, status=400)
        
        messages =[
            {"role": "user", 
                "content":(
                    f"투자 성향이 '{type_of}'이야. "
                    f"연수입은 {income}만원이고, "
                    "이럴 때 너가 추천해줄만한 투자 종류가 있을까? "
                    "그리고 그 상품 중에서 수익이 좋은 상품들을 5가지 정도 추천해줄래? "
                    "또한 투자 비율을 알려줘. 대신 범위를 설정하지 말고 명확히 알려줘야 해."
                    "대답 형식은"
                    "투자 종류"
                    "(넘버링 하여 하나씩 나열)"
                    "수익 좋은 상품 5가지"
                    "(넘버링 하여 하나씩 나열)"
                    "투자 비율"
                    "(투자 종류 이름): ~%"
                    "이런식으로 해볼래?"
                )}
        ]
        
        
        try:
            completion = openai.ChatCompletion.create(model="gpt-4-turbo", messages=messages)
            assistant_content = completion.choices[0].message["content"].strip()
            messages.append({"role": "assistant", "content": assistant_content})
            return JsonResponse({"response": assistant_content, "messages": messages})
        
        # OpenAIError를 직접 임포트한 경우를 대비해 수정
        except OpenAIError as e:
            logging.Logger.error(f"OpenAIError 발생: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)