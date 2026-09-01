from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthenticationMethod1(str, Enum):
    BYPASS = "Bypass"
    MANUAL_VERIFICATION = "ManualVerification"
    MERCHANT_AUTHENTICATION = "MerchantAuthentication"
    OFFLINE_PIN = "OfflinePIN"
    ONLINE_PIN = "OnlinePIN"
    PAPER_SIGNATURE = "PaperSignature"
    SECURED_CHANNEL = "SecuredChannel"
    SECURE_CERTIFICATE = "SecureCertificate"
    SECURE_NO_CERTIFICATE = "SecureNoCertificate"
    SIGNATURE_CAPTURE = "SignatureCapture"
    UNKNOWN_METHOD = "UnknownMethod"

    __str__ = str.__str__


AuthenticationMethod1OrStr: TypeAlias = Annotated[
    AuthenticationMethod1 | str, open_enum_validator(AuthenticationMethod1)
]
