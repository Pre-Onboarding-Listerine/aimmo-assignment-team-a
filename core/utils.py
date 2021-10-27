from jwt import exceptions, decode

from django.http import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from users.models import User

def authentication(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            if not access_token:
                return JsonResponse( {'MESSAGE' : 'NO TOKEN'}, status = 403)

            payload = decode(access_token, SECRET_KEY, ALGORITHM)
            user_id = payload['id']

            user = User.objects.get(id = user_id)
            request.user = user

        except exceptions.DecodeError:
            return JsonResponse( {'MESSAGE' : 'INVALID TOKEN'}, status = 403)

        except User.DoesNotExist:
            return JsonResponse( {'MESSAGE' : 'INVALID USER'}, status = 403)

        except exceptions.ExpiredSignatureError:
            return JsonResponse( {'MESSAGE' : 'TOKEN EXPIRED'}, status = 400)

        return func(self, request, *args, **kwargs)

    return wrapper