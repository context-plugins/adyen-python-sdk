from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankAccount(SdkBaseModel):
    """A container for bank account data., A container for bank account data.
    > This field is mandatory if ``card`` is not provided."""

    bank_account_number: Optional[str] = Field(default=UNSET, alias="bankAccountNumber")
    """The bank account number (without separators)."""

    bank_city: Optional[str] = Field(default=UNSET, alias="bankCity")
    """The bank city."""

    bank_location_id: Optional[str] = Field(default=UNSET, alias="bankLocationId")
    """The location id of the bank. The field value is ``nil`` in most cases."""

    bank_name: Optional[str] = Field(default=UNSET, alias="bankName")
    """The name of the bank."""

    bic: Optional[str] = UNSET
    """The `Business Identifier Code <https://en.wikipedia.org/wiki/ISO_9362>`__ (BIC) is the SWIFT address assigned to
    a bank. The field value is ``nil`` in most cases."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """Country code where the bank is located.

    A valid value is an ISO two-character country code (e.g. 'NL')."""

    iban: Optional[str] = UNSET
    """The `International Bank Account Number <https://en.wikipedia.org/wiki/International_Bank_Account_Number>`__
    (IBAN)."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The name of the bank account holder. If you submit a name with non-Latin characters, we automatically replace
    some of them with corresponding Latin characters to meet the FATF recommendations. For example:
    * χ12 is converted to ch12.
    * üA is converted to euA.
    * Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.
    After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one
    of them must be a valid Latin character (A-Z, a-z). For example:
    * John17 - allowed.
    * J17 - allowed.
    * 171 - not allowed.
    * John-7 - allowed.
    > If provided details don't match the required format, the response returns the error message: 203 'Invalid bank
        account holder name'."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The bank account holder's tax ID."""


class BankAccountDict(TypedDict):
    bank_account_number: NotRequired[str]
    bank_city: NotRequired[str]
    bank_location_id: NotRequired[str]
    bank_name: NotRequired[str]
    bic: NotRequired[str]
    country_code: NotRequired[str]
    iban: NotRequired[str]
    owner_name: NotRequired[str]
    tax_id: NotRequired[str]
