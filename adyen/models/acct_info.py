from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.ch_acc_age_ind import ChAccAgeIndOrStr
from .enums.ch_acc_change_ind import ChAccChangeIndOrStr
from .enums.ch_acc_pw_change_ind import ChAccPwChangeIndOrStr
from .enums.payment_acc_ind import PaymentAccIndOrStr
from .enums.ship_address_usage_ind import ShipAddressUsageIndOrStr
from .enums.ship_name_indicator import ShipNameIndicatorOrStr
from .enums.suspicious_acc_activity import SuspiciousAccActivityOrStr


class AcctInfo(SdkBaseModel):
    """Additional information about the cardholder’s account provided by the 3DS Requestor."""

    ch_acc_age_ind: Optional[ChAccAgeIndOrStr] = Field(default=UNSET, alias="chAccAgeInd")
    """Length of time that the cardholder has had the account with the 3DS Requestor. Allowed values:
    * **01** — No account
    * **02** — Created during this transaction
    * **03** — Less than 30 days
    * **04** — 30–60 days
    * **05** — More than 60 days"""

    ch_acc_change: Optional[str] = Field(default=UNSET, alias="chAccChange")
    """Date that the cardholder’s account with the 3DS Requestor was last changed, including Billing or Shipping
    address, new payment account, or new user(s) added. Format: **YYYYMMDD**"""

    ch_acc_change_ind: Optional[ChAccChangeIndOrStr] = Field(default=UNSET, alias="chAccChangeInd")
    """Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including
    Billing or Shipping address, new payment account, or new user(s) added. Allowed values:
    * **01** — Changed during this transaction
    * **02** — Less than 30 days
    * **03** — 30–60 days
    * **04** — More than 60 days"""

    ch_acc_pw_change: Optional[str] = Field(default=UNSET, alias="chAccPwChange")
    """Date that cardholder’s account with the 3DS Requestor had a password change or account reset. Format:
    **YYYYMMDD**"""

    ch_acc_pw_change_ind: Optional[ChAccPwChangeIndOrStr] = Field(default=UNSET, alias="chAccPwChangeInd")
    """Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or
    account reset. Allowed values:
    * **01** — No change
    * **02** — Changed during this transaction
    * **03** — Less than 30 days
    * **04** — 30–60 days
    * **05** — More than 60 days"""

    ch_acc_string: Optional[str] = Field(default=UNSET, alias="chAccString")
    """Date that the cardholder opened the account with the 3DS Requestor. Format: **YYYYMMDD**"""

    nb_purchase_account: Optional[str] = Field(default=UNSET, alias="nbPurchaseAccount")
    """Number of purchases with this cardholder account during the previous six months. Max length: 4 characters."""

    payment_acc_age: Optional[str] = Field(default=UNSET, alias="paymentAccAge")
    """String that the payment account was enrolled in the cardholder’s account with the 3DS Requestor. Format:
    **YYYYMMDD**"""

    payment_acc_ind: Optional[PaymentAccIndOrStr] = Field(default=UNSET, alias="paymentAccInd")
    """Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS
    Requestor. Allowed values:
    * **01** — No account (guest checkout)
    * **02** — During this transaction
    * **03** — Less than 30 days
    * **04** — 30–60 days
    * **05** — More than 60 days"""

    provision_attempts_day: Optional[str] = Field(default=UNSET, alias="provisionAttemptsDay")
    """Number of Add Card attempts in the last 24 hours. Max length: 3 characters."""

    ship_address_usage: Optional[str] = Field(default=UNSET, alias="shipAddressUsage")
    """String when the shipping address used for this transaction was first used with the 3DS Requestor. Format:
    **YYYYMMDD**"""

    ship_address_usage_ind: Optional[ShipAddressUsageIndOrStr] = Field(default=UNSET, alias="shipAddressUsageInd")
    """Indicates when the shipping address used for this transaction was first used with the 3DS Requestor. Allowed
    values:
    * **01** — This transaction
    * **02** — Less than 30 days
    * **03** — 30–60 days
    * **04** — More than 60 days"""

    ship_name_indicator: Optional[ShipNameIndicatorOrStr] = Field(default=UNSET, alias="shipNameIndicator")
    """Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction.
    Allowed values:
    * **01** — Account Name identical to shipping Name
    * **02** — Account Name different to shipping Name"""

    suspicious_acc_activity: Optional[SuspiciousAccActivityOrStr] = Field(default=UNSET, alias="suspiciousAccActivity")
    """Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the
    cardholder account. Allowed values:
    * **01** — No suspicious activity has been observed
    * **02** — Suspicious activity has been observed"""

    txn_activity_day: Optional[str] = Field(default=UNSET, alias="txnActivityDay")
    """Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all
    payment accounts in the previous 24 hours. Max length: 3 characters."""

    txn_activity_year: Optional[str] = Field(default=UNSET, alias="txnActivityYear")
    """Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all
    payment accounts in the previous year. Max length: 3 characters."""


class AcctInfoDict(TypedDict):
    ch_acc_age_ind: NotRequired[ChAccAgeIndOrStr]
    ch_acc_change: NotRequired[str]
    ch_acc_change_ind: NotRequired[ChAccChangeIndOrStr]
    ch_acc_pw_change: NotRequired[str]
    ch_acc_pw_change_ind: NotRequired[ChAccPwChangeIndOrStr]
    ch_acc_string: NotRequired[str]
    nb_purchase_account: NotRequired[str]
    payment_acc_age: NotRequired[str]
    payment_acc_ind: NotRequired[PaymentAccIndOrStr]
    provision_attempts_day: NotRequired[str]
    ship_address_usage: NotRequired[str]
    ship_address_usage_ind: NotRequired[ShipAddressUsageIndOrStr]
    ship_name_indicator: NotRequired[ShipNameIndicatorOrStr]
    suspicious_acc_activity: NotRequired[SuspiciousAccActivityOrStr]
    txn_activity_day: NotRequired[str]
    txn_activity_year: NotRequired[str]
