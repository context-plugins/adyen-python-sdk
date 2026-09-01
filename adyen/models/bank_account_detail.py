from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankAccountDetail(SdkBaseModel):
    """The details of the bank account to where a payout was made."""

    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The bank account number (without separators). >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """The type of bank account. Only applicable to bank accounts held in the USA. The permitted values are:
    ``checking``, ``savings``.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    bank_account_name: Optional[str] = Field(default=UNSET, alias="bankAccountName")
    """The name of the bank account."""

    bank_account_reference: Optional[str] = Field(default=UNSET, alias="bankAccountReference")
    """Merchant reference to the bank account."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The unique identifier (UUID) of the Bank Account. >If, during an account holder create or update request, this
    field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated
    UUID.

    >If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while
    the creation of the account holder will continue.

    >If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is
    provided, the update of the account holder will fail.

    >If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided,
    the existing Bank Account will be updated."""

    bank_bic_swift: Optional[str] = Field(default=UNSET, alias="bankBicSwift")
    """The bank identifier code. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    bank_city: Optional[str] = Field(default=UNSET, alias="bankCity")
    """The city in which the bank branch is located.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    bank_code: Optional[str] = Field(default=UNSET, alias="bankCode")
    """The bank code of the banking institution with which the bank account is registered.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    bank_name: Optional[str] = Field(default=UNSET, alias="bankName")
    """The name of the banking institution with which the bank account is held.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    branch_code: Optional[str] = Field(default=UNSET, alias="branchCode")
    """The branch code of the branch under which the bank account is registered. The value to be specified in this
    parameter depends on the country of the bank account:
    * United States - Routing number
    * United Kingdom - Sort code
    * Germany - Bankleitzahl
    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    check_code: Optional[str] = Field(default=UNSET, alias="checkCode")
    """The check code of the bank account.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The two-letter country code in which the bank account is registered. >The permitted country codes are defined in
    ISO-3166-1 alpha-2 (e.g. 'NL').

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The currency in which the bank account deals. >The permitted currency codes are defined in ISO-4217 (e.g.
    'EUR')."""

    iban: Optional[str] = UNSET
    """The international bank account number. >The IBAN standard is defined in ISO-13616.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_city: Optional[str] = Field(default=UNSET, alias="ownerCity")
    """The city of residence of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_country_code: Optional[str] = Field(default=UNSET, alias="ownerCountryCode")
    """The country code of the country of residence of the bank account owner. >The permitted country codes are defined
    in ISO-3166-1 alpha-2 (e.g. 'NL').

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_date_of_birth: Optional[str] = Field(default=UNSET, alias="ownerDateOfBirth")
    """The date of birth of the bank account owner. The date should be in ISO-8601 format yyyy-mm-dd (e.g.
    2000-01-31)."""

    owner_house_number_or_name: Optional[str] = Field(default=UNSET, alias="ownerHouseNumberOrName")
    """The house name or number of the residence of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_name: Optional[str] = Field(default=UNSET, alias="ownerName")
    """The name of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_nationality: Optional[str] = Field(default=UNSET, alias="ownerNationality")
    """The country code of the country of nationality of the bank account owner. >The permitted country codes are
    defined in ISO-3166-1 alpha-2 (e.g. 'NL').

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_postal_code: Optional[str] = Field(default=UNSET, alias="ownerPostalCode")
    """The postal code of the residence of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_state: Optional[str] = Field(default=UNSET, alias="ownerState")
    """The state of residence of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    owner_street: Optional[str] = Field(default=UNSET, alias="ownerStreet")
    """The street name of the residence of the bank account owner. >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    primary_account: Optional[bool] = Field(default=UNSET, alias="primaryAccount")
    """If set to true, the bank account is a primary account."""

    tax_id: Optional[str] = Field(default=UNSET, alias="taxId")
    """The tax ID number.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""

    url_for_verification: Optional[str] = Field(default=UNSET, alias="urlForVerification")
    """The URL to be used for bank account verification. This may be generated on bank account creation.

    >Refer to `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__ for details on field
    requirements."""


class BankAccountDetailDict(TypedDict):
    account_number: NotRequired[str]
    account_type: NotRequired[str]
    bank_account_name: NotRequired[str]
    bank_account_reference: NotRequired[str]
    bank_account_uuid: NotRequired[str]
    bank_bic_swift: NotRequired[str]
    bank_city: NotRequired[str]
    bank_code: NotRequired[str]
    bank_name: NotRequired[str]
    branch_code: NotRequired[str]
    check_code: NotRequired[str]
    country_code: NotRequired[str]
    currency_code: NotRequired[str]
    iban: NotRequired[str]
    owner_city: NotRequired[str]
    owner_country_code: NotRequired[str]
    owner_date_of_birth: NotRequired[str]
    owner_house_number_or_name: NotRequired[str]
    owner_name: NotRequired[str]
    owner_nationality: NotRequired[str]
    owner_postal_code: NotRequired[str]
    owner_state: NotRequired[str]
    owner_street: NotRequired[str]
    primary_account: NotRequired[bool]
    tax_id: NotRequired[str]
    url_for_verification: NotRequired[str]
