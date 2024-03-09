# 모두 같은 행동을 하지만 더 높은 수준의 추상화가 된 코드일수록 가독성이 좋아진다.

# urllib을 사용해 검색하기
import json
from urllib.request import urlopen
from urllib.parse import urlencode

params = dict(q='Sausages', format='json')
handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params))
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)

results = parsed['RelatedTopics']
print('urllib Example')
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])


# requests를 사용해 검색하기
import requests

params = dict(q='Sausages', format='json')
parsed = requests.get('http://api.duckduckgo.com', params=params).json()

results = parsed['RelatedTopics']
print('requests Example')
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])


# duckduckgo 모둘을 사용해서 검사하기
import duckduckgo

print('duckduckgo Example')
for r in duckduckgo.query('Sausages').results:
    print(r.url + ' - ' + r.text)