from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.entity_type2 import EntityType2OrStr
from .name import Name, NameDict
from .recurring import Recurring, RecurringDict


class SubmitRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular request."""

    amount: Amount
    """A container object for the payable amount information of the transaction."""

    date_of_birth: Optional[Date] = Field(default=UNSET, alias="dateOfBirth")
    """The date of birth. Format: ISO-8601; example: YYYY-MM-DD

    For Paysafecard it must be the same as used when registering the Paysafecard account.

    > This field is mandatory for natural persons.
    > This field is required to update the existing ``dateOfBirth`` that is associated with this recurring contract."""

    entity_type: Optional[EntityType2OrStr] = Field(default=UNSET, alias="entityType")
    """The type of the entity the payout is processed for.

    Allowed values:
    * NaturalPerson
    * Company
    > This field is required to update the existing ``entityType`` that is associated with this recurring contract."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier you want to process the transaction request with."""

    nationality: Optional[str] = UNSET
    """The shopper's nationality.

    A valid value is an ISO 2-character country code (e.g. 'NL').

    > This field is required to update the existing nationality that is associated with this recurring contract."""

    recurring: Recurring
    """A container for the type of recurring contract to be retrieved.

    The ``recurring.contract`` must be set to "PAYOUT"."""

    reference: str
    """The merchant reference for this payout. This reference will be used in all communication to the merchant about
    the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement."""

    selected_recurring_detail_reference: str = Field(alias="selectedRecurringDetailReference")
    """This is the ``recurringDetailReference`` you want to use for this payout.

    You can use the value LATEST to select the most recently used recurring detail."""

    shopper_email: str = Field(alias="shopperEmail")
    """The shopper's email address."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """The shopper's name.

    In case the ``entityType`` is ``Company``, the ``shopperName.lastName`` must contain the company name.

    > This field is required to update the existing ``shopperName`` associated with a recurring contract."""

    shopper_reference: str = Field(alias="shopperReference")
    """The shopper's reference for the payout transaction."""

    shopper_statement: Optional[str] = Field(default=UNSET, alias="shopperStatement")
    """The description of this payout. This description is shown on the bank statement of the shopper (if this is
    supported by the chosen payment method)."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""


class SubmitRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    amount: AmountDict
    date_of_birth: NotRequired[Date]
    entity_type: NotRequired[EntityType2OrStr]
    fraud_offset: NotRequired[int]
    merchant_account: str
    nationality: NotRequired[str]
    recurring: RecurringDict
    reference: str
    selected_recurring_detail_reference: str
    shopper_email: str
    shopper_name: NotRequired[NameDict]
    shopper_reference: str
    shopper_statement: NotRequired[str]
    social_security_number: NotRequired[str]
