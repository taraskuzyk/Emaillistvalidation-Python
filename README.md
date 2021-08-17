# Emaillistvalidation-Python (except it doesn't suck)
Python API for emaillistvalidation.com

Create verifier object:
```python
from emailvalid import EmailValidator
email_validator = EmailValidator(key="YOUR_KEY")
```
To check single email:
```python
email_validator.check_email("taras@salesmeetings.ai")
```