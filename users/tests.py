import json
import bcrypt

from django.test import TestCase, Client

from unittest.mock import MagicMock, patch
from .models       import User


class SignUpTest(TestCase):
    def setUp(self):
        User.objects.bulk_create(
            [
                User(
                    id       = 1,
                    name     = "jongmin1",
                    email    = "zoobell@naver.com",
                    password = "@!zxcZvzcxv",
                ),
                User(
                    id       = 2,
                    name     = "jonmin2",
                    email    = "bbdf1da@google.com",
                    password = "@!rkdvncnReindenhd"
                ),
                User(
                    id       = 3,
                    name     = "jongmin3",
                    email    = "klende1@kakao.com",
                    password = "Wdfasbbcfdgg$!"
                )
            ]
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_view_create_success(self):
        user = {
            "name"           : "jongmin1",
            "email"          : "zoobell@naver.com",
            "password"       : "@!zxcZvzcxv",
            "check_password" : "@!zxcZvzcxv"
        }

        client   = Client()
        response = client.post(
            "/users/signup", json.dumps(user), content_type = "application/json"
            )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"MESSAGE" : "SUCCESS"})
        