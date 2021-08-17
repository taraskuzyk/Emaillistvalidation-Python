#!/usr/bin/python
# _*_ coding:utf-8 _*_


import requests
import re

API_ENDPOINT = "https://app.emaillistvalidation.com/api/verifEmail"


def is_email_format_valid(email: str) -> bool:

    return bool(re.match(r'^(\w|\.|_|-)+[@](\w|_|-|\.)+[.]\w{2,3}$', email))


class EmailListValidation:
    # explanation for codes https://help.emaillistvalidation.com/en/articles/3971158-result-codes-and-terminology
    OK = 0
    OK_RESPONSES = ["ok"]

    CATCH_ALL = 1
    CATCH_ALL_RESPONSES = ["ok_for_all", "accept_all"]

    BAD_EMAIL = 2
    BAD_EMAIL_RESPONSES = ["error", "unknown_email", "email_disabled", "syntax_error", "disposable",
                           "spam_traps"]

    BAD_SERVER = 3
    BAD_SERVER_RESPONSES = ["smtp_error", "domain_error"]

    UNKNOWN = 4
    UNKNOWN_RESPONSES = ["smtp_protocol", "attempt_rejected", "relay_error", "antispam_system",
                         "unknown", "invalid_vendor"]

    def __init__(self, key):
        self._key = key

    def check_email(self, email: str) -> int:
        status_from_server = self._get_status_from_server(email)
        return self._translate_server_response(status_from_server)

    def _get_status_from_server(self, email: str) -> str:
        params = {
            "secret": self._key,
            "email": email
        }
        response = requests.get(API_ENDPOINT, params=params)
        return str(response.text)

    def _translate_server_response(self, server_response: str) -> int:
        if server_response in self.OK_RESPONSES:
            return self.OK
        elif server_response in self.CATCH_ALL_RESPONSES:
            return self.CATCH_ALL
        elif server_response in self.BAD_EMAIL_RESPONSES:
            return self.BAD_EMAIL
        elif server_response in self.BAD_SERVER_RESPONSES:
            return self.BAD_SERVER
        else:
            return self.UNKNOWN

