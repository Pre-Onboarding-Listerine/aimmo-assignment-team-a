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

- 가상환경 생성(conda사용을 가정) conda create -n (가상환경 이름)
- conda activate (생성한 가상환경 이름) 가상환경 실행
- git remote add origin https://github.com/Gouache-studio/Wanted.git
- git clone https://github.com/Gouache-studio/Wanted.git

### 구현 방법
## endpoint 호출 및 실행

POST : /users/sign-up : name, email, password, check_password : 회원가입 <br>
POST : /users/sign-in	: email, password	                      : 로그인<br>
POST : /poststing	    : title, content	                      : 게시물 작성<br>
GET	 : /posts         : id 		                                : 게시물 조회<br>

## api 명세
### 1. 회원가입

- Method : POST
- EndpointURL : /users/signup
- Remark : (email : @와 . 형식이 아닐 시 오류반환), (password : 숫자,문자,특수문자, 대문자가 포함이 된 8자 이상)
- ## Request

```
POST "http://127.0.0.1:8000/users/signup HTTP/1.1" \
--data-raw '{
    "name"  : "주종민",
    "email" : "wanted@naver.com",
    "password": "chlvkfksqufslaWKd@!1"
}'
```

- Response

```
{
    "MESSAGE": "SUCCESS"
}
```
### 2. 로그인
- Method : POST
- EndpointURL : /users/signin
- Remark : (email : @와 . 형식이 아닐 시 오류반환), (password : 숫자,문자,특수문자, 대문자가 포함이 된 8자 이상), 토큰발급

- ## Request
```
POST "http://127.0.0.1:8000/users/signin HTTP/1.1" \
--data-raw '{
    "email" : "wanted@naver.com",
    "password": "chlvkfksqufslaWKd@!1"
}'
```

- ## Response
```
{
    "MESSAGE": "SUCCESS",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjM1NTc4NDA1fQ.yTAZHkPpGhsITwDWJOQG2ztc365z4LVWrJWZEowblds",
    "user_name": "주종민"
}
```

### 3. 포스트생성 
- Method : POST
- EndpointURL : /posting
- Remark : 헤더에 Authorization : 인증토큰 사용해야함
```
POST "http://127.0.0.1:8000/posting/post HTTP/1.1" \
--data-raw '{
    "title"   : "선발과제",
    "content" : "기업협업프로젝트가 너무 할게 많다."
}'
```

- ## Response
```
{
    "MESSAGE": "Posting Success",
    "RESULT": {
        "author": "주종민",
        "title": "선발과제",
        "content": "기업협업프로젝트가 너무 할게 많다.",
        "created_at": "10/27/2021, 07:50:00"
    }
}
```

### 4. 포스트 수정 
- Method : PUT
- EndpointURL : /posting/edit
- Remark : 헤더에 Authorization : 인증토큰 사용해야함

- ## Request
```
POST "http://127.0.0.1:8000/posting/edit HTTP/1.1" \
--data-raw '{
    "post_id" : "1",
    "title"   : "페이지네이션되라얍!!!",
    "content" : "10분남았습니다"
}'
```

- ## Response
```
{
    "MESSAGE": "EDIT SUCCESS"
}
```

### 5. 포스트 삭제 
- Method : DELETE
- EndpointURL : /posting/delete
- Remark : 헤더에 Authorization : 인증토큰 사용해야함

- ## Request
```
POST "http://127.0.0.1:8000/posting/delete HTTP/1.1" \
--data-raw '{
    "post_id" : "10"
}'
```

- ## Response
```
{
    "MESSAGE": "SUCCESS DELETE POST_ID : 10"
}
```

### 6. 포스트 조회 
- Method : GET
- EndpointURL : /posting
- Remark : offset, limit 으로 페이지네이션 구현, limit = 7

- ## Request
```
POST "http://127.0.0.1:8000/posting HTTP/1.1" \


- ## Response
```{
    "results": {
        "count": 10,
        "data": [
            {
                "author": "주종민",
                "title": "페이지네이션되라얍!!!",
                "content": "10분남았습니다",
                "created_at": "10/27/2021, 07:50:00"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍1",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:50:58"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍2",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:02"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍3",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:05"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍4",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:08"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍5",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:12"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍6",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:14"
            },
            {
                "author": "주종민",
                "title": "페이지네이션되라얍7",
                "content": "15분남았습니다",
                "created_at": "10/27/2021, 07:51:18"
            }
        ]
    }
}
```
