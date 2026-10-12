from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_level1 import ServiceLevel1OrStr
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class DinersInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **diners**. For merchants operating in Japan, Diners payments are processed
    through the JCB network. This means that you must include `JCB-specific fields
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-jcb)
    in this object."""

    mid_number: Optional[str] = Field(default=UNSET, alias="midNumber")
    """MID (Merchant ID) number. Required for merchants operating in Japan. Format: 14 numeric characters."""

    reuse_mid_number: bool = Field(default=False, alias="reuseMidNumber")
    """Indicates whether the JCB Merchant ID is reused from a previously configured JCB payment method. The default
    value is **false**. For merchants operating in Japan, this field is required and must be set to **true**."""

    service_level: Optional[ServiceLevel1OrStr] = Field(default=UNSET, alias="serviceLevel")
    """Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan.
    Possible values:
     * **noContract**: Adyen holds the contract with JCB.
     * **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant
            directly."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class DinersInfo1Dict(TypedDict):
    mid_number: NotRequired[str]
    reuse_mid_number: bool
    service_level: NotRequired[ServiceLevel1OrStr]
    transaction_description: NotRequired[TransactionDescriptionInfo1Dict]
