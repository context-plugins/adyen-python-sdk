from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.account_age_indicator import AccountAgeIndicatorOrStr
from .enums.account_change_indicator import AccountChangeIndicatorOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.delivery_address_usage_indicator import DeliveryAddressUsageIndicatorOrStr
from .enums.password_change_indicator import PasswordChangeIndicatorOrStr
from .enums.payment_account_indicator import PaymentAccountIndicatorOrStr


class AccountInfo(SdkBaseModel):
    """Shopper account information for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    account_age_indicator: Optional[AccountAgeIndicatorOrStr] = Field(default=UNSET, alias="accountAgeIndicator")
    """Indicator for the length of time since this shopper account was created in the merchant's environment. Allowed
    values:
    * notApplicable
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    account_change_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="accountChangeDate")
    """Date when the shopper's account was last changed."""

    account_change_indicator: Optional[AccountChangeIndicatorOrStr] = Field(
        default=UNSET, alias="accountChangeIndicator"
    )
    """Indicator for the length of time since the shopper's account was last updated. Allowed values:
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    account_creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="accountCreationDate")
    """Date when the shopper's account was created."""

    account_type: Optional[AccountTypeOrStr] = Field(default=UNSET, alias="accountType")
    """Indicates the type of account. For example, for a multi-account card product. Allowed values:
    * notApplicable
    * credit
    * debit"""

    add_card_attempts_day: Optional[int] = Field(default=UNSET, alias="addCardAttemptsDay")
    """Number of attempts the shopper tried to add a card to their account in the last day."""

    delivery_address_usage_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveryAddressUsageDate")
    """Date the selected delivery address was first used."""

    delivery_address_usage_indicator: Optional[DeliveryAddressUsageIndicatorOrStr] = Field(
        default=UNSET, alias="deliveryAddressUsageIndicator"
    )
    """Indicator for the length of time since this delivery address was first used. Allowed values:
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    home_phone: Optional[str] = Field(default=UNSET, alias="homePhone")
    """Shopper's home phone number (including the country code)."""

    mobile_phone: Optional[str] = Field(default=UNSET, alias="mobilePhone")
    """Shopper's mobile phone number (including the country code)."""

    password_change_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="passwordChangeDate")
    """Date when the shopper last changed their password."""

    password_change_indicator: Optional[PasswordChangeIndicatorOrStr] = Field(
        default=UNSET, alias="passwordChangeIndicator"
    )
    """Indicator when the shopper has changed their password. Allowed values:
    * notApplicable
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    past_transactions_day: Optional[int] = Field(default=UNSET, alias="pastTransactionsDay")
    """Number of all transactions (successful and abandoned) from this shopper in the past 24 hours."""

    past_transactions_year: Optional[int] = Field(default=UNSET, alias="pastTransactionsYear")
    """Number of all transactions (successful and abandoned) from this shopper in the past year."""

    payment_account_age: Optional[RFC3339DateTime] = Field(default=UNSET, alias="paymentAccountAge")
    """Date this payment method was added to the shopper's account."""

    payment_account_indicator: Optional[PaymentAccountIndicatorOrStr] = Field(
        default=UNSET, alias="paymentAccountIndicator"
    )
    """Indicator for the length of time since this payment method was added to this shopper's account. Allowed values:
    * notApplicable
    * thisTransaction
    * lessThan30Days
    * from30To60Days
    * moreThan60Days"""

    purchases_last6_months: Optional[int] = Field(default=UNSET, alias="purchasesLast6Months")
    """Number of successful purchases in the last six months."""

    suspicious_activity: Optional[bool] = Field(default=UNSET, alias="suspiciousActivity")
    """Whether suspicious activity was recorded on this account."""

    work_phone: Optional[str] = Field(default=UNSET, alias="workPhone")
    """Shopper's work phone number (including the country code)."""


class AccountInfoDict(TypedDict):
    account_age_indicator: NotRequired[AccountAgeIndicatorOrStr]
    account_change_date: NotRequired[RFC3339DateTime]
    account_change_indicator: NotRequired[AccountChangeIndicatorOrStr]
    account_creation_date: NotRequired[RFC3339DateTime]
    account_type: NotRequired[AccountTypeOrStr]
    add_card_attempts_day: NotRequired[int]
    delivery_address_usage_date: NotRequired[RFC3339DateTime]
    delivery_address_usage_indicator: NotRequired[DeliveryAddressUsageIndicatorOrStr]
    home_phone: NotRequired[str]
    mobile_phone: NotRequired[str]
    password_change_date: NotRequired[RFC3339DateTime]
    password_change_indicator: NotRequired[PasswordChangeIndicatorOrStr]
    past_transactions_day: NotRequired[int]
    past_transactions_year: NotRequired[int]
    payment_account_age: NotRequired[RFC3339DateTime]
    payment_account_indicator: NotRequired[PaymentAccountIndicatorOrStr]
    purchases_last6_months: NotRequired[int]
    suspicious_activity: NotRequired[bool]
    work_phone: NotRequired[str]
