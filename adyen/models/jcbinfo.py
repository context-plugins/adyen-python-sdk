from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_level2 import ServiceLevel2OrStr
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class Jcbinfo(SdkBaseModel):
    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """MID (Merchant ID) number. Required for merchants operating in Japan or merchants operating in Canada, Australia
    and New Zealand when requesting ``gatewayContract`` or ``paymentDesignatorContract`` service levels.Format: 14
    numeric characters for Japan, 10 numeric characters for Canada, Australia and New Zealand."""

    reuse_mid_number: Optional[bool] = Field(default=UNSET, alias="reuseMidNumber")
    """Indicates whether the JCB Merchant ID is reused from a previously setup JCB payment method. The default value is
    **false**.For merchants operating in Japan, this field is required and must be set to **true**."""

    service_level: Optional[ServiceLevel2OrStr] = Field(default=UNSET, alias="serviceLevel")
    """Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan.
    Possible values:
    * **noContract**: Adyen holds the contract with JCB for merchants operating in Japan or American Express for
        merchants operating in Canada, Australia and New Zealand.
    * **gatewayContract**: JCB or American Express receives the settlement and handles disputes, then pays out to you or
        your sub-merchant directly.
    * **paymentDesignatorContract**: Available only for merchants operating in Canada, Australia and New Zealand. Adyen
        receives the settlement, and handles disputes and payouts."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class JcbinfoDict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: NotRequired[bool]
    service_level: NotRequired[ServiceLevel2OrStr]
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
