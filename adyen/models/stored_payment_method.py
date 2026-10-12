from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type16 import Type16, Type16OrStr


class StoredPaymentMethod(SdkBaseModel):
    cashtag: Optional[str] = UNSET
    """Cash App issued cashtag for recurring payment"""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    customer_id: Optional[str] = Field(default=UNSET, alias="customerId")
    """Cash App issued customerId for recurring payment"""

    grant_id: Optional[str] = Field(default=UNSET, alias="grantId")
    """Cash App issued grantId for one time payment"""

    on_file_grant_id: Optional[str] = Field(default=UNSET, alias="onFileGrantId")
    """Cash App issued onFileGrantId for recurring payment"""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """Cash App request id"""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the ``recurringDetailReference`` returned in the response when you created the token."""

    subtype: Optional[str] = UNSET
    """The payment method subtype."""

    type_: Type16OrStr = Field(default=Type16.CASHAPP, alias="type")
    """cashapp"""


class StoredPaymentMethodDict(TypedDict):
    cashtag: NotRequired[str]
    checkout_attempt_id: NotRequired[str]
    customer_id: NotRequired[str]
    grant_id: NotRequired[str]
    on_file_grant_id: NotRequired[str]
    recurring_detail_reference: NotRequired[str]
    request_id: NotRequired[str]
    sdk_data: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
    subtype: NotRequired[str]
    type_: NotRequired[Type16OrStr]
