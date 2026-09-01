from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.three_dsreq_prior_auth_method import ThreeDsreqPriorAuthMethodOrStr


class ThreeDsrequestorPriorAuthenticationInfo(SdkBaseModel):
    """Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction."""

    three_ds_req_prior_auth_data: Optional[str] = Field(default=UNSET, alias="threeDSReqPriorAuthData")
    """Data that documents and supports a specific authentication process. Maximum length: 2048 bytes."""

    three_ds_req_prior_auth_method: Optional[ThreeDsreqPriorAuthMethodOrStr] = Field(
        default=UNSET, alias="threeDSReqPriorAuthMethod"
    )
    """Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values:
    * **01** — Frictionless authentication occurred by ACS.
    * **02** — Cardholder challenge occurred by ACS.
    * **03** — AVS verified.
    * **04** — Other issuer methods."""

    three_ds_req_prior_auth_timestamp: Optional[str] = Field(default=UNSET, alias="threeDSReqPriorAuthTimestamp")
    """Date and time in UTC of the prior cardholder authentication. Format: YYYYMMDDHHMM"""

    three_ds_req_prior_ref: Optional[str] = Field(default=UNSET, alias="threeDSReqPriorRef")
    """This data element provides additional information to the ACS to determine the best approach for handing a
    request. This data element contains an ACS Transaction ID for a prior authenticated transaction. For example, the
    first recurring transaction that was authenticated with the cardholder. Length: 30 characters."""


class ThreeDsrequestorPriorAuthenticationInfoDict(TypedDict):
    three_ds_req_prior_auth_data: NotRequired[str]
    three_ds_req_prior_auth_method: NotRequired[ThreeDsreqPriorAuthMethodOrStr]
    three_ds_req_prior_auth_timestamp: NotRequired[str]
    three_ds_req_prior_ref: NotRequired[str]
