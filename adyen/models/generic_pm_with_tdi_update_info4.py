from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class GenericPmWithTdiUpdateInfo4(SdkBaseModel):
    """Details to provide if ``type`` is **discover**. For merchants operating in Japan, request `Diners
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-diners)
    payment method instead. Discover is automatically requested, together with Diners."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class GenericPmWithTdiUpdateInfo4Dict(TypedDict):
    transaction_description: NotRequired[TransactionDescriptionInfo1Dict]
