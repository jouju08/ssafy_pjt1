from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from openai import OpenAI
import logging

# 로깅 설정
logger = logging.getLogger(__name__)

client = OpenAI(api_key='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')

from openai import AuthenticationError, RateLimitError, OpenAIError

@api_view(['POST'])
def chat(request):
    if request.method == "POST":
        try:
            # 요청 데이터 가져오기
            data = request.data
            user_message = data.get("message", "").strip()
            messages = data.get("messages", [])

            if not user_message:
                return JsonResponse({"error": "메시지가 비어 있습니다."}, status=400)
            if not isinstance(messages, list):
                return JsonResponse({"error": "'messages'는 리스트여야 합니다."}, status=400)

            # 사용자 메시지를 추가
            messages.append({"role": "user", "content": user_message})

            completion = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=messages
            )

            assistant_content = completion.choices[0].message.content.strip()
            messages.append({"role": "assistant", "content": assistant_content})

            return JsonResponse({"response": assistant_content, "messages": messages})

        
        except AuthenticationError:
            # 인증 실패 처리
            logger.error("OpenAI 인증 실패: API 키를 확인하세요.")
            return JsonResponse({"error": "OpenAI 인증 실패. API 키를 확인하세요."}, status=401)
        except OpenAIError as e:
            # 기타 OpenAI API 에러 처리
            logger.error(f"OpenAI API 에러 발생: {str(e)}")
            return JsonResponse({"error": f"OpenAI API 에러: {str(e)}"}, status=500)
        except RateLimitError:
            # 쿼터 초과 에러 처리
            logger.error("OpenAI API 요청 제한 초과.")
            return JsonResponse(
                {"error": "OpenAI API 요청 한도를 초과했습니다. 플랜을 확인하거나 결제 정보를 업데이트하세요."},
                status=429
            )
        except Exception as e:
            # 서버 내부 에러 처리
            logger.error(f"서버 에러 발생: {str(e)}")
            return JsonResponse({"error": f"서버 에러: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

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