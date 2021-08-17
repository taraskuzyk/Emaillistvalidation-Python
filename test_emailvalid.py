import pytest
from emaillistvalidation_api import EmailListValidation as ELV, is_email_format_valid
import os
import pytest

API_KEY = os.environ['EMAIL_VALIDATOR_API_KEY']
email_validator = ELV(API_KEY)


class TestEmailValidator:

    def test_email_format_with_invalid_format(self):
        assert not is_email_format_valid("leadstheory.com")

    def test_email_format_with_valid_format(self):
        assert is_email_format_valid("taras@leadstheory.com")

    def test_taras_leadstheory(self):
        assert email_validator.check_email("taras@leadstheory.com") == ELV.OK

    def test_nottaras_leadstheory(self):
        assert email_validator.check_email("nottaras@leadstheory.com") == ELV.BAD_EMAIL

    def test_bad_domain(self):
        assert email_validator.check_email("f@xxdxdxdxdxdxdxdxdxd.com") == ELV.UNKNOWN

    @pytest.mark.skip("Need to find stable catch all email for test case")
    def test_catch_all(self):
        assert email_validator.check_email("f@strokersdallas.com") == ELV.CATCH_ALL


