from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests,datetime
from .models import DepositProducts, DepositOptions,Change
from .serializer import DepositOptionsSerializer, DepositProductsSerializer,ChangeSerializer
from django.http import JsonResponse
from django.conf import settings
API_KEY='8606577955382312a042df530b801d13'
BASE_URL='http://finlife.fss.or.kr/finlifeapi/'
from datetime import datetime
# Create your views here.

@api_view(['GET']) #정기예금 상품 목록과 옵션 목록 DB에 저장
def save_deposit_product(request):
    URL=BASE_URL+'depositProductsSearch.json'
    params={
        'auth':API_KEY,
        'topFinGrpNo':'020000',
        'pageNo':'1',
    }
    response=requests.get(URL, params=params).json()
    
    for li in response.get('result').get('baseList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        kor_co_nm=li.get('kor_co_nm')
        fin_prdt_nm=li.get('fin_prdt_nm')
        etc_note=li.get('etc_note')
        join_deny=li.get('join_deny')
        join_member=li.get('join_member')
        join_way=li.get('join_way')
        spcl_cnd=li.get('spcl_cnd')
        if not all([fin_prdt_cd, kor_co_nm, fin_prdt_nm]):
            continue  # 필수 데이터가 없는 경우 건너뜁니다.

        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm,etc_note=etc_note,
                                           join_deny=join_deny, join_member=join_member, join_way=join_way, spcl_cnd=spcl_cnd).exists():
            continue
        
        save_data={
            # 'product':product.id,
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        serializer=DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    

    for li in response.get('result').get('optionList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        intr_rate_type_nm=li.get('intr_rate_type_nm')
        intr_rate=li.get('intr_rate') or -1
        
        intr_rate2=li.get('intr_rate2')
        save_trm=li.get('save_trm')
       
        if not fin_prdt_cd:
            continue  # 필수 데이터가 없는 경우 건너뜁니다.
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        if DepositOptions.objects.filter(product=product,fin_prdt_cd=fin_prdt_cd, save_trm=save_trm, intr_rate=intr_rate,intr_rate2=intr_rate2,
                                           intr_rate_type_nm=intr_rate_type_nm).exists():
            continue
        
        save_data={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer=DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    print(response)
    return JsonResponse(serializer.data)

@api_view(['GET','POST'])#get: 전체 정기 예금 상품 목록 반환, post: 상품 데이터 저장
def deposit_product(request):
    products=DepositProducts.objects.all()
    if request.method=='GET':
        serializer=DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
     
#특정 상품의 옵션 리스트 반환
@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):
    option_list=DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer=DepositProductsSerializer(option_list, many=True)
    return Response(serializer.data)


#가입 기간 상관없이 금리 가장 높은 상품과 해당 상품 옵션 리스트 출력
@api_view(['GET'])
def top_rate(request):
    intrs=DepositOptions.objects.all()
    MAX=0
    top_intr_cd=''
    for intr in intrs:
        if intr.intr_rate2>MAX:
            MAX=intr.intr_rate2
            top_product=intr.fin_prdt_cd
    product=DepositProducts.objects.get(fin_prdt_cd=top_product)
    options=get_list_or_404(DepositOptions,fin_prdt_cd=top_product)
    
    product_serializer=DepositProductsSerializer(product)
    options_serializer=DepositOptionsSerializer(options, many=True)
    context={
        'deposit_products':product_serializer.data,
        'options':options_serializer.data
    }
    return Response(context)



@api_view(['GET'])
def save_change(request):
    today=datetime.now()
    if today.weekday()>=5:
        diff = today.weekday()-4
        today = today - datetime.timedelta(days=diff)#주말엔 정보가 없으니 금요일로 바꿔주기
    today=today.strftime('%Y%m%d')
    API_KEYY='CVkBJTzbrnQkcYoUhhxeKEJughCIro3U'
    URL2='https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url=URL2.format(API_KEYY, today)
    response=requests.get(url,verify=False).json()#오류나면 verify 값 바꿔주기
    print(response)
    for li in response:
        cur_unit=li.get('cur_unit')
        cur_nm=li.get('cur_nm')
        ttb=li.get('ttb')
        tts=li.get('tts')
        deal_bas_r=li.get('deal_bas_r')

        save_data={
            'cur_unit':cur_unit,
            'cur_nm':cur_nm,
            'ttb':ttb,
            'tts':tts,
            'deal_bas_r':deal_bas_r
        }
        serializer=ChangeSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)
  
@api_view(['GET'])
def get_change(request,cur_unit):

    changes=get_list_or_404(Change, cur_unit=cur_unit)
    serializer=ChangeSerializer(changes, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_bankname(request):
    products = DepositProducts.objects.values('kor_co_nm').distinct().order_by('kor_co_nm')
    bank_names = [product['kor_co_nm'] for product in products]
    
    return Response(bank_names)