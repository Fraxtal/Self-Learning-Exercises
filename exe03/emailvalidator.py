import re

class EmailValidator:
    def __init__(self, email):
            self.__email = email

    def validate(self):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.__email):
            return True
        else:
            return False

gmail = EmailValidator("fongkarlgmailcom")
if gmail.validate():
     print("Valid")
else:
     print("Invalid")