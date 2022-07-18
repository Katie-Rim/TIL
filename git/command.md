### 1. 설정과 초기화

**전역 사용자명/이메일 구성**

$ git config - -global user.name “Your name”

$ git config - -global user.email “Your email address”



**저장소별 사용자명/이메일 구성하기**

$ git config user.name “Your name”

$ git config user.email “Your email address”




### 2. 기본적인 사용법

새로운 파일을 추가하거나 존재하는 파일 스테이징하고 커밋하기

$ git add <파일>

$ git commit -m “<메시지>”

폴더 생성

$ mkdir [폴더명]

파일 생성

$ touch [파일명]

파일 저장하고 나가기

$ :wq



### 3. 원격 저장소

저장소 복제하기

$ git clone <저장소 url>

새로운 원격 저장소 추가하기

$ git remote add <원격저장소> <저장소url>
