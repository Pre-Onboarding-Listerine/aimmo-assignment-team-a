# Wanted 프리온보딩 선발과제 

<br>

### 유저인증, 인가
### 게시물 조회, 생성, 수정, 삭제 CRUD 구현 <br>

<br>

## 구현한 방법과 이유.

### User
- 정규 표현식을 통해 email, password 오류 방지 
- 로그인 시 jwt 토큰을 발행하고 사용

<br>

### Posting
- PostingListView는 인증이 필요없이 누구나 볼 수 있게 설계 
- 로그인 한 회원만 글을 작성, 수정, 삭제 할 수 있도록 로그인데코레이터 기능 구현

## 자세한 실행방법

<br>

- 가상환경 생성(conda사용을 가정) conda create -n (가상환경 이름)
- conda activate (생성한 가상환경 이름) 가상환경 실행
- git remote add origin "레퍼지토리주소" 

## endpoint 호출 및 실행

POST : /users/sign-up : name, email, password, check_password : 회원가입 <br>
POST : /users/sign-in	: email, password	                      : 로그인<br>
POST : /poststing	    : title, content	                      : 게시물 작성<br>
GET	 : /posts         : id 		                                : 게시물 조회


### 구현 방법

(endpoint 호출방법)

## api 명세

(request/response 서술)


