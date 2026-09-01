from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ThreeDs2ResponseData1(SdkBaseModel):
    """Response of the 3D Secure 2 authentication."""

    acs_challenge_mandated: Optional[str] = Field(default=UNSET, alias="acsChallengeMandated")
    acs_operator_id: Optional[str] = Field(default=UNSET, alias="acsOperatorID")
    acs_reference_number: Optional[str] = Field(default=UNSET, alias="acsReferenceNumber")
    acs_signed_content: Optional[str] = Field(default=UNSET, alias="acsSignedContent")
    acs_trans_id: Optional[str] = Field(default=UNSET, alias="acsTransID")
    acs_url: Optional[str] = Field(default=UNSET, alias="acsURL")
    authentication_type: Optional[str] = Field(default=UNSET, alias="authenticationType")
    card_holder_info: Optional[str] = Field(default=UNSET, alias="cardHolderInfo")
    cavv_algorithm: Optional[str] = Field(default=UNSET, alias="cavvAlgorithm")
    challenge_indicator: Optional[str] = Field(default=UNSET, alias="challengeIndicator")
    ds_reference_number: Optional[str] = Field(default=UNSET, alias="dsReferenceNumber")
    ds_trans_id: Optional[str] = Field(default=UNSET, alias="dsTransID")
    exemption_indicator: Optional[str] = Field(default=UNSET, alias="exemptionIndicator")
    message_version: Optional[str] = Field(default=UNSET, alias="messageVersion")
    risk_score: Optional[str] = Field(default=UNSET, alias="riskScore")
    sdk_ephem_pub_key: Optional[str] = Field(default=UNSET, alias="sdkEphemPubKey")
    three_ds_server_trans_id: Optional[str] = Field(default=UNSET, alias="threeDSServerTransID")
    trans_status: Optional[str] = Field(default=UNSET, alias="transStatus")
    trans_status_reason: Optional[str] = Field(default=UNSET, alias="transStatusReason")


class ThreeDs2ResponseData1Dict(TypedDict):
    acs_challenge_mandated: NotRequired[str]
    acs_operator_id: NotRequired[str]
    acs_reference_number: NotRequired[str]
    acs_signed_content: NotRequired[str]
    acs_trans_id: NotRequired[str]
    acs_url: NotRequired[str]
    authentication_type: NotRequired[str]
    card_holder_info: NotRequired[str]
    cavv_algorithm: NotRequired[str]
    challenge_indicator: NotRequired[str]
    ds_reference_number: NotRequired[str]
    ds_trans_id: NotRequired[str]
    exemption_indicator: NotRequired[str]
    message_version: NotRequired[str]
    risk_score: NotRequired[str]
    sdk_ephem_pub_key: NotRequired[str]
    three_ds_server_trans_id: NotRequired[str]
    trans_status: NotRequired[str]
    trans_status_reason: NotRequired[str]
