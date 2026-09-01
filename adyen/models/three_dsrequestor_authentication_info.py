from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.three_dsreq_auth_method import ThreeDsreqAuthMethodOrStr


class ThreeDsrequestorAuthenticationInfo(SdkBaseModel):
    """Information about how the 3DS Requestor authenticated the cardholder before or during the transaction"""

    three_ds_req_auth_data: Optional[str] = Field(default=UNSET, alias="threeDSReqAuthData")
    """Data that documents and supports a specific authentication process. Maximum length: 2048 bytes."""

    three_ds_req_auth_method: Optional[ThreeDsreqAuthMethodOrStr] = Field(default=UNSET, alias="threeDSReqAuthMethod")
    """Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values:
    * **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest).
    * **02** — Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials.
    * **03** — Login to the cardholder account at the 3DS Requestor system using federated ID.
    * **04** — Login to the cardholder account at the 3DS Requestor system using issuer credentials.
    * **05** — Login to the cardholder account at the 3DS Requestor system using third-party authentication.
    * **06** — Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator."""

    three_ds_req_auth_timestamp: Optional[str] = Field(default=UNSET, alias="threeDSReqAuthTimestamp")
    """Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM"""


class ThreeDsrequestorAuthenticationInfoDict(TypedDict):
    three_ds_req_auth_data: NotRequired[str]
    three_ds_req_auth_method: NotRequired[ThreeDsreqAuthMethodOrStr]
    three_ds_req_auth_timestamp: NotRequired[str]
