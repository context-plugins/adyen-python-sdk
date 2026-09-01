from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataDomesticError(SdkBaseModel):
    domestic_refusal_reason_raw: Optional[str] = Field(default=UNSET, alias="domesticRefusalReasonRaw")
    """The reason the transaction was declined, given by the local issuer. Currently available for merchants in
    Japan."""

    domestic_shopper_advice: Optional[str] = Field(default=UNSET, alias="domesticShopperAdvice")
    """The action the shopper should take, in a local language. Currently available in Japanese, for merchants in
    Japan."""


class ResponseAdditionalDataDomesticErrorDict(TypedDict):
    domestic_refusal_reason_raw: NotRequired[str]
    domestic_shopper_advice: NotRequired[str]
