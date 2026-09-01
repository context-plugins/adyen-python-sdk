from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class GenericPmWithTdiUpdateInfo3(SdkBaseModel):
    """Details to provide if ``type`` is **diners**. For merchants operating in Japan, Diners payments are processed
    through the JCB network. This means that you must include `JCB-specific fields
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-jcb)
    in this object."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class GenericPmWithTdiUpdateInfo3Dict(TypedDict):
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
