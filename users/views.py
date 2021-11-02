import json, re, bcrypt, jwt

from django.views import View
from django.http import JsonResponse
from datetime import datetime, timedelta

from my_settings import SECRET_KEY, ALGORITHM
from utils import get_db_handle

db_handle, client = get_db_handle()

user_collection = db_handle['user']

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        REGEX_EMAIL = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        REGEX_PASSWORD = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$") 

        password = data["password"]

        if user_collection.find_one({"email": data["email"]}):
            return JsonResponse({"MESSAGE" : "DUPLICATED EMAIL"}, status = 400)

        if not REGEX_EMAIL.match(data["email"]):
            return JsonResponse({"MESSAGE":"WRONG EMAIL FOMAT"}, status = 400)

        if not REGEX_PASSWORD.match(data["password"]):
            return JsonResponse({"MESSAGE" : "WRONG PASSWORD FOMAT"}, status = 400)
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        decoded_password = hashed_password.decode("utf-8")

        new_user = {
            "name": data["name"],
            "email": data["email"],
            "password": decoded_password,
        }
        user_collection.insert_one(new_user)
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user = user_collection.find_one({"email": data["email"]})
            if not user:
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status = 401)

            if not bcrypt.checkpw(data["password"].encode("utf-8"), user["password"].encode("utf-8")):
                return JsonResponse({"MESSAGE": "INVALID_PASSWORD"}, status = 401)

            access_token = jwt.encode({"id": str(user["_id"]) , 'exp':datetime.utcnow() + timedelta(days=3)}, SECRET_KEY , algorithm=ALGORITHM)
            return JsonResponse({"MESSAGE": "SUCCESS", 'token' : access_token, "user_name" : user["name"]}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
