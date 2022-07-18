# 임성아새

2022-07-14 스타트업

git에 대해서 알아보자 😃

git: 분산 버전 관리 “프로그램”  

- 서버 터져도 복구가 가능하다.
- Sever computer: Git 기반의 저장소 서비스를 제공하는 서비스

git 기반 서비스

- github <MS>
- gitlab <저장 server 마음대로 구축 가능>
- bi해tbucket

**github**

- gib 기반 저장소 “서비스” 제공
- MS
- git \neq github
- [장점1]  git을 이용한 버전 관리
- 전세계 모든 사람들에게 나를 표현하는 수단
- 열정, 성실함, 홍보 능력을 나타난다는 장점!! (예시: insta)
- [장점2] github을 이용한 포트폴리오
- 잔디밭 관리하기 (최소 하루 한 개-1일1커밋-해야 구멍이 없음)
- “””성실함”””+”””커뮤니케이션”””

←→중앙 집중식 버전 관리 (ex. 은행 서버) 

- 코드가 하나의 서버에 버전관리 히스토리가 저장되어 있음
- 서버 터지면 망한다.

ㅎCLI: command line

GUI와 CLI

- command-line interface (CLI) ←mostly, developers: “명령어”를 통해 사용자와 컴퓨터가 상호 작용하는 방식
- graphical user interface (GUI) ←users : “그래픽”을 통해 사용자와 컴퓨터가 상호 작용하는 방식
- 둘이 하는 건 똑같음 (컴퓨터한테 명령)

Why CLI

- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
- 수 많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공

CLI

기본적인 명령어

- touch: 파일 생성
- rm: 파일 삭제
- Mkdir: 새 폴더 생성
- -r 옵션을 주면 폴더 삭제가능
- Is: 디렉토리의 폴더/파일 목록을 보여주는 명령어
- cd: 현재 작업 중인 디렉토리를 변경하는 명령어
- start, open: 폴더/파일을 여는 명령어(windown —> start, mac —> open)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47e49b48-e6f9-478c-8e4c-a81d1f54c872/Untitled.png)

현재 작업 위치 ex) C:\Users\multicampus = ‘~’

‘home directory’

바탕화면도 결국 폴더

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b17086a3-75a8-4d97-ab1a-79382614ce7a/Untitled.png)

desktop.ini ←숨김처리됨

**절대 경로 vs 상대 경로**

> 절대 경로

- 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
- 윈도우 바탕 화면의 절대 경로 -C:/Users/ssafy/Desktop

>상대경로

- 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
- 현재 작업하고 있는 디렉토리가 C:/Users 일 때, 윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop
- ./ :  현재 작업하고 있는 폴더
- ../ : 현재 작업하고 있는 폴더의 부모 폴더

## 마크다운

- 텍스트 기반의 가벼운 마크업 언어 (마크다운 이름 유래설: 마크업 사용함을 보여주기 위해서….)
- 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
- cf) 마크업: tag를 이용하여 문서의 구조를 나타내는 것
- ex) TeX - LaTex
- 마크다운의 문법= 태그 ex) #, **
- 노션도 마크다운 문법 지원함

Github 문서의 시작과 끝!

- [READ.md](http://READ.md) 파일을 통해 오픈 소스의 공식 문서 작성
- 개인 프로젝트의 소개 문서 작성
- 매일 학습한 내용 정리
- 마크다운을 이용한 블로그 운영
- = 개발문서의 시작과 끝
- 대부분의 웹 에디터에서 지원 (각종 블로그 사이트 등)
- Jupyter Notebook, Notion, 다양한 메모장 프로그램 등

# Typora

- 실시간 마크다운 변환 (미리보기) 제공
- 이미지 또는 표 삽입시 매우 편한 UI 제공
- VS code 등의 프로그램도 마크다운을 지원하지만 전용 프로그램을 사용하면 더 편하게 사용가능

헤딩 heading

- 문서의 제목이나 소제목
- 샵의 개수에 따라 (h1~h6)
- 문서 구조의 기본
- 글자크기를 키우기 위해서는 사용하면 안됨!!!!

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a674eddf-b13b-42da-a7c6-47dcd117e6e7/Untitled.png)

리스트 

* - (별표 하이픈 똑같음)

1.2.3.

- 순서가 있는 리스트와 순서가 없는 리스트
- 목록을 표시하기 위해
- 많이 사용하는 태그 중 하나
- 순서 없애려면 엔터엔터
- 탭 들여쓰기
- 시프티탭 내여쓰기

코드 블록 

- 일반 텍스트와 다르게 코드를 이쁘게 출력해요
- 사용하는 프로그램에 따라 특정 언어를 명시하면 구문 강조 (Syntax highlighting) 지원
- “”“code block”””
- back-tip

ex) 

‘’’ python 

print(’hello’)

‘’’

링크

[string] (url)

- string은 보여지는 부분, url은 연결한 부분
- 다른 페이지로 이동하는 링크를 삽입
- 필요하다면 파일의 경로를 넣어 다운로드 가능한 링크로 만들 수 있어야0

![string](img_url)

**Bold ←- 언더바 4개나 눈송이 2개** 

*italic ←- 언더바 2개나 눈송이 1개 양옆*

~~strickout~~ ←-  왜 안되지

수평선 눈송이 3개 언더바3개 하이픈 

가로로 긴 수평선 작성

대개 단락 구분할 때 사용

3개 이상만 적으면 똑같이 적용

---

# Git 기본기

README.md

- 개발자들에게 “특별”
- 프로젝트에 대한 설명 문서

Repository

### 특정 디렉토리를 버전 관리하는 저장소

- git init 명령어로 로컬 저장소를 생성 (c.f. 로컬 저장소 ←→ 리모트 저장소)
- .git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

특정 버전ㅊ으로 남긴다 = “커밋(commit)한다” (3가지 영역을 바탕으로 동작!)

- working directory: 작업하고 있는 실제 디렉토리
- Staging area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
- repository: 커밋들이 저장되는 곳

---

7월 15일 (금)

- working directory에서 작업한 파일(untracked)에 대한 “변경”사항을 staging area에 저장할 때는 git add, 상태는 staged로. git commit

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/79b549c2-bd76-4192-98eb-31671bd1c535/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d64f6c8b-014c-475c-83f4-6d1bfe1fae0f/Untitled.png)

git status:  현재 git으로 관리되고 있는 파일들의 상태를 알 수 있다.

- desktop에서 (master) 사인 뜰 때

user —> SSAFY  —> 보기(숨긴 항목) —>  git 저장소 삭제 

git diff A B (A-기준-가 B에 비해서 뭐가 달라졌는지)

---

### Remote Repository

Github 이용 github repository 생성

- get remote add origin {[remote_repo](https://github.com/Katie-Rim/first_repo)}
- git push -u origin master

origin —> <repo_name> 별명

master —> local branch

SSAFY@DESKTOP MINGW64 ~/Desktop/del (master)
$ add add .
bash: add: command not found

SSAFY@DESKTOP MINGW64 ~/Desktop/del (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/del (master)
$ git commit -m
error: switch `m' requires a value

SSAFY@DESKTOP MINGW64 ~/Desktop/del (master)
$ r
[master f189246] 수정
1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/del (master)
$ git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 381 bytes | 381.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To [https://github.com/Katie-Rim/first_repo.git](https://github.com/Katie-Rim/first_repo.git)
8b9fa98..f189246  master -> master

$ git push --set-upstream origin master
Everything up-to-date
branch 'master' set up to track 'origin/master'.

---

add, commit, push, pull, clone

SSAFY@DESKTOP MINGW64 ~
$ cd desktop

SSAFY@DESKTOP MINGW64 ~/desktop
$ git clone [https://github.com/Katie-Rim/clone_test.git](https://github.com/Katie-Rim/clone_test.git)

SSAFY@DESKTOP MINGW64 ~/desktop
$ start .

SSAFY@DESKTOP MINGW64 ~/desktop
$ ^C

SSAFY@DESKTOP MINGW64 ~/desktop
$ cd clone_test/

SSAFY@DESKTOP MINGW64 ~/desktop/clone_test (master)
$

컨트롤 케이 에프

$ cd ..

SSAFY@DESKTOP MINGW64 ~/desktop/clone_test (master)
$ code .

SSAFY@DESKTOP MINGW64 ~/Desktop/clone_test (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/clone_test (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified:   [hello.py](http://hello.py/)

SSAFY@DESKTOP MINGW64 ~/Desktop/clone_test (master)
$ git commit -m "update"
[master 0cfa586] update
1 file changed, 1 insertion(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/clone_test (master)
$ git push

---

 TIL (Today I Learned)

- 매일 배운 거 마크다운으로 정리해서 문서화
- 1일 1커밋