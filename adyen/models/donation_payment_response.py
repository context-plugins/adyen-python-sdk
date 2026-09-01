from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount26 import Amount26, Amount26Dict
from .enums.status1 import Status1OrStr
from .payment_response9 import PaymentResponse9, PaymentResponse9Dict


class DonationPaymentResponse(SdkBaseModel):
    amount: Optional[Amount26] = UNSET
    """Authorised amount in the transaction."""

    donation_account: Optional[str] = Field(default=UNSET, alias="donationAccount")
    """The Adyen account name of your charity. We will provide you with this account name once your chosen charity has
    been `onboarded <https://docs.adyen.com/online-payments/donations#onboarding>`__."""

    id: Optional[str] = UNSET
    """Your unique resource identifier."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    payment: Optional[PaymentResponse9] = UNSET
    """Action to be taken for completing the payment."""

    reference: Optional[str] = UNSET
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to
    provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters."""

    status: Optional[Status1OrStr] = UNSET
    """The status of the donation transaction.

    Possible values:
    * **completed**
    * **pending**
    * **refused**"""


class DonationPaymentResponseDict(TypedDict):
    amount: NotRequired[Amount26 | Amount26Dict]
    donation_account: NotRequired[str]
    id: NotRequired[str]
    merchant_account: NotRequired[str]
    payment: NotRequired[PaymentResponse9 | PaymentResponse9Dict]
    reference: NotRequired[str]
    status: NotRequired[Status1OrStr]
