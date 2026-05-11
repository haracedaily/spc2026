# OpenSource Python Pypi
import requests
# requests 모듈을 사용하여 HTTP 요청을 보내고 응답을 처리할 수 있다.
# response = requests.get('https://www.google.com')
# print(response.status_code)
# print(response.text)

#외부에 HTTP 요청을 대신해주는 라이브러리
# resp = requests.get("http://www.naver.com") #: HTTP GET 요청을 보낸다.
# print(resp) #: HTTP 응답 객체를 출력한다. < Response [200] > : HTTP 응답 상태 코드가 200인 응답 객체를 출력한다.
# print(resp.status_code) #: HTTP 응답 상태 코드를 출력한다.
# print(resp.headers) #: HTTP 응답 헤더를 출력한다. {'Content-Type': 'text/html; charset=UTF-8', 'Content-Length': '12345', ...}
# resp = requests.get("http://www.example.com") #: HTTP GET 요청을 보낸다.
# print("웹페이지 내용 : ",resp.text) #: HTTP 응답 본문을 출력한다. 정적 문서인 HTML 문서가 출력된다.
# print(resp.text) #: HTTP 응답 본문을 출력한다. 정적 문서인 HTML 문서가 출력된다.
# requests.post("http://www.naver.com") #: HTTP POST 요청을 보낸다.
# requests.put("http://www.naver.com") #: HTTP PUT 요청을 보낸다.
# requests.delete("http://www.naver.com") #: HTTP DELETE 요청을 보낸다.

resp = requests.get("https://api.github.com") #: HTTP GET 요청을 보낸다.

print(resp.status_code) #: HTTP 응답 상태 코드를 출력한다. 200
"""
if(resp.status_code == 200): #: HTTP 응답 상태 코드가 200인 경우
    print(resp.text)
else :
    print("HTTP 요청 실패 : ", resp.status_code) #: HTTP 요청 실패 메시지와 상태 코드를 출력한다.
"""
# curr_user_url = resp.text["current_user_url"] #: HTTP 응답 본문에서 current_user_url 값을 가져온다. text로 가져와서 dict로 안되서 변환해야함.
# print(curr_user_url) #: current_user_url 값을 출력한다. https://api.github.com/user
#외부 모듈은 pip install requests로 설치한다.
# 그러면 pypi.prg로부터 requests 모듈이 다운로드되고 설치된다.

#readthedocs.org에서 requests 모듈의 공식 문서를 확인할 수 있다. https://requests.readthedocs.io/en/latest/