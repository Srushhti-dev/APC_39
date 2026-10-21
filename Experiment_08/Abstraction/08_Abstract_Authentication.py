from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, password):
        self.password = password

    def authenticate(self):
        return self.password == "1234"


class OTPAuthentication(Authentication):
    def __init__(self, otp):
        self.otp = otp

    def authenticate(self):
        return self.otp == "567890"


class BiometricAuthentication(Authentication):
    def __init__(self, biometric_match):
        self.biometric_match = biometric_match

    def authenticate(self):
        return self.biometric_match


methods = [
    PasswordAuthentication("1234"),
    OTPAuthentication("567890"),
    BiometricAuthentication(True)
]

for method in methods:
    print("Authentication successful:", method.authenticate())
