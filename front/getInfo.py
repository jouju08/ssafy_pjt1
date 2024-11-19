from urllib import parse
from ast import literal_eval
import requests

def get_size():
    params = {
        # 'symbol': 'KOSPI',
        'symbol': 'KOSDAQ',
        'requestType': 1,
        'startTime': '20240402',
        'endTime': '20241120',
        'timeframe': 'day'
    }
    # URL 인코딩된 파라미터 생성
    query_string = parse.urlencode(params)
    # URL에 쿼리 문자열을 추가
    url = f"https://m.stock.naver.com/front-api/external/chart/domestic/info?{query_string}"
    response = requests.get(url)
    return literal_eval(response.text.strip())

print(get_size())
