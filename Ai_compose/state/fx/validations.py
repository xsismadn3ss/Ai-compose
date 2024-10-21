import re


def validate_email(email):
    regex = r"^[A-Za-z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$"
    # regex=r'mail'

    result = re.match(regex, email)

    if result:
        return True

    return False


def validate_password(password):
    validations = (
        re.compile(r".{8,}"),
        re.compile(r"\d+"),
        re.compile(r"[A-Z]+"),
        re.compile(r"[a-z]+"),
        re.compile(r"[$@#]+"),
    )

    for validation in validations:
        if not validation.search(password):
            return False
    
    return True