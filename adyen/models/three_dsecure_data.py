from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.authentication_response import AuthenticationResponseOrStr
from .enums.challenge_cancel import ChallengeCancelOrStr
from .enums.directory_response import DirectoryResponseOrStr


class ThreeDsecureData(SdkBaseModel):
    """Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires)."""

    authentication_response: Optional[AuthenticationResponseOrStr] = Field(
        default=UNSET, alias="authenticationResponse"
    )
    """In 3D Secure 2, this is the ``transStatus`` from the challenge result. If the transaction was frictionless, omit
    this parameter."""

    cavv: Optional[str] = UNSET
    """The cardholder authentication value (base64 encoded, 20 bytes in a decoded form)."""

    cavv_algorithm: Optional[str] = Field(default=UNSET, alias="cavvAlgorithm")
    """The CAVV algorithm used. Include this only for 3D Secure 1."""

    challenge_cancel: Optional[ChallengeCancelOrStr] = Field(default=UNSET, alias="challengeCancel")
    """Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has
    been cancelled. For possible values, refer to `3D Secure API reference
    <https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata>`__."""

    directory_response: Optional[DirectoryResponseOrStr] = Field(default=UNSET, alias="directoryResponse")
    """In 3D Secure 2, this is the ``transStatus`` from the ``ARes``."""

    ds_trans_id: Optional[str] = Field(default=UNSET, alias="dsTransID")
    """Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a
    single transaction."""

    eci: Optional[str] = UNSET
    """The electronic commerce indicator."""

    risk_score: Optional[str] = Field(default=UNSET, alias="riskScore")
    """Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations."""

    three_ds_version: Optional[str] = Field(default=UNSET, alias="threeDSVersion")
    """The version of the 3D Secure protocol."""

    token_authentication_verification_value: Optional[str] = Field(
        default=UNSET, alias="tokenAuthenticationVerificationValue"
    )
    """Network token authentication verification value (TAVV). The network token cryptogram."""

    trans_status_reason: Optional[str] = Field(default=UNSET, alias="transStatusReason")
    """Provides information on why the ``transStatus`` field has the specified value. For possible values, refer to `our
    docs <https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values>`__."""

    xid: Optional[str] = UNSET
    """Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form)."""


class ThreeDsecureDataDict(TypedDict):
    authentication_response: NotRequired[AuthenticationResponseOrStr]
    cavv: NotRequired[str]
    cavv_algorithm: NotRequired[str]
    challenge_cancel: NotRequired[ChallengeCancelOrStr]
    directory_response: NotRequired[DirectoryResponseOrStr]
    ds_trans_id: NotRequired[str]
    eci: NotRequired[str]
    risk_score: NotRequired[str]
    three_ds_version: NotRequired[str]
    token_authentication_verification_value: NotRequired[str]
    trans_status_reason: NotRequired[str]
    xid: NotRequired[str]
