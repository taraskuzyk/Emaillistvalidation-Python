# EmailListValidation-API
Python API for emaillistvalidation.com

To install run
```shell
pip install git+https://github.com/taraskuzyk/Emaillistvalidation-Python
```

Create verifier object:
```python
from emaillistvalidation_api import EmailListValidation as Validator
email_validator = Validator(key="YOUR_KEY")
```
To check single email:
```python
status = email_validator.check_email("taras@salesmeetings.ai")
```

Possible outcomes are
```
constant             |  value
------------------------------
Validator.OK         |  0
Validator.CATCH_ALL  |  1
Validator.BAD_EMAIL  |  2
Vaildator.BAD_SERVER |  3
Validator.UNKNOWN    |  4
```
