import urllib.request
# urllib 모듈은 URL 파싱, HTTP 요청과 응답 관련 작업을 할 수 있다.
# request : URL을 열고 읽는 모듈 
# error : request 모듈에서 발생하는 에러를 포함하는 모듈 
# parse : URL을 파싱하는 모듈 (URL을 해석 및 조작)
# robotparser : robots.txt 파일을 파싱


url = 'https://www.naver.com'
request = urllib.request.Request(url)
# print(request)
# print(request.full_url) # 전체 URL 정보
# print(request.type) # 프로토콜 정보
# print(request.host) # 호스트 정보

response1 = urllib.request.urlopen(request)
# print(response1)
# print(dir(response1))
# print(response1.getheaders()) # 헤더 정보를 튜플의 리스트 형식으로 반환 

# read() : urlopen()으로 연 객체를 읽고, 인자로 전달하는 숫자 만큼 
# 데이터를 읽는다 
response2 = urllib.request.urlopen(url)
data = response2.read(20)
# print(data)

# decode() : 바이트 형식의 데이터를 원하는 형식으로 변환(기본 utf-8)
text_data = data.decode()
# print(text_data)

# urlretrieve() : 웹 상의 이미지를 다운로드 
img_src = 'https://image.utoimage.com/preview/cp872722/2022/12/202212008462_500.jpg'
new_name = 'img.jpeg'
urllib.request.urlretrieve(img_src, new_name)

import urllib.parse
url = 'https://n.news.naver.com/mnews/article/015/0004939977?sid=105&param=1234'
parse = urllib.parse.urlparse(url)
# urlparse() : URL을 6개로 분리하여 반환 
# scheme : 프로토콜 
# netloc : 호스트 
# path : 경로 
# params : 사용하지 않음 
# query : 쿼리파라미터
# fragment : #, 프래그먼트 식별자 
# print(parse)

# urlsplit() : URL을 5개로 분리하여 튜플로 반환 
parse2 = urllib.parse.urlsplit(url)
# print(parse2)

# urlunparse(), urlunsplit() : 분리된 URL을 다시 합친다.
unparse = urllib.parse.urlunparse(parse)
unsplit = urllib.parse.urlunsplit(parse2)
# print(unparse)
# print(unsplit)

# print(parse.query)
# print(type(parse.query))

# query를 파싱하여 딕셔너리 형태로 반환
qs = urllib.parse.parse_qs(parse.query)
print(qs)

# query를 파싱하여 튜플의 리스트 형태로 반환
qsl = urllib.parse.parse_qsl(parse.query)
print(qsl)

# urljoin(a,b) : a와 b URL을 합쳐주는 기능
url = 'https://www.naver.com/a/b/'
# print(urllib.parse.urljoin(url, 'c')) # 상대경로 방식으로 붙음 
# print(urllib.parse.urljoin(url, '/c')) # 절대경로 방식으로 붙음
url = 'https://search.naver.com/search.naver?query=아이폰'
# response = urllib.request.urlopen(url)
# byte_data = response.read()
# text_data = byte_data.decode()
# print(text_data)
print(urllib.parse.quote('아이폰'))

