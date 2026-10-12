from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_detail import BankAccountDetail, BankAccountDetailDict
from .business_details3 import BusinessDetails3, BusinessDetails3Dict
from .individual_details3 import IndividualDetails3, IndividualDetails3Dict
from .legal_arrangement_detail import LegalArrangementDetail, LegalArrangementDetailDict
from .payout_method import PayoutMethod, PayoutMethodDict
from .store_detail import StoreDetail, StoreDetailDict
from .vias_address6 import ViasAddress6, ViasAddress6Dict
from .vias_address9 import ViasAddress9, ViasAddress9Dict
from .vias_phone_number3 import ViasPhoneNumber3, ViasPhoneNumber3Dict


class AccountHolderDetails3(SdkBaseModel):
    """Details of the account holder."""

    address: ViasAddress9
    """The address of the account holder."""

    bank_account_details: Optional[list[BankAccountDetail]] = Field(default=UNSET, alias="bankAccountDetails")
    """Array of bank accounts associated with the account holder. For details about the required ``bankAccountDetail``
    fields, see `Required information
    <https://docs.adyen.com/classic-platforms/verification-process/required-information>`__."""

    bank_aggregator_data_reference: Optional[str] = Field(default=UNSET, alias="bankAggregatorDataReference")
    """The opaque reference value returned by the Adyen API during bank account login."""

    business_details: Optional[BusinessDetails3] = Field(default=UNSET, alias="businessDetails")
    """Details about the business or nonprofit account holder. Required when creating an account holder with
    ``legalEntity`` **Business** or **NonProfit**."""

    email: Optional[str] = UNSET
    """The email address of the account holder."""

    full_phone_number: Optional[str] = Field(default=UNSET, alias="fullPhoneNumber")
    """The phone number of the account holder provided as a single string. It will be handled as a landline phone.
    **Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
    """

    individual_details: Optional[IndividualDetails3] = Field(default=UNSET, alias="individualDetails")
    """Details about the individual account holder. Required when creating an account holder with ``legalEntity``
    **Individual**."""

    last_review_date: Optional[str] = Field(default=UNSET, alias="lastReviewDate")
    """Date when you last reviewed the account holder's information, in ISO-8601 YYYY-MM-DD format. For example,
    **2020-01-31**."""

    legal_arrangements: Optional[list[LegalArrangementDetail]] = Field(default=UNSET, alias="legalArrangements")
    """An array containing information about the account holder's `legal arrangements
    <https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements>`__."""

    merchant_category_code: Optional[str] = Field(default=UNSET, alias="merchantCategoryCode")
    """The Merchant Category Code of the account holder.
    > If not specified in the request, this will be derived from the platform account (which is configured by Adyen)."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use by the account holder or merchant. The keys do not have specific
    names and may be used for storing miscellaneous data as desired.
    > The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    payout_methods: Optional[list[PayoutMethod]] = Field(default=UNSET, alias="payoutMethods")
    """Array of tokenized card details associated with the account holder. For details about how you can use the tokens
    to pay out, refer to `Pay out to cards <https://docs.adyen.com/classic-platforms/payout-to-cards>`__."""

    phone_number: Optional[ViasPhoneNumber3] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the account holder.
    > Required if a ``fullPhoneNumber`` is not provided."""

    principal_business_address: Optional[ViasAddress6] = Field(default=UNSET, alias="principalBusinessAddress")
    """The principal business address of the account holder."""

    store_details: Optional[list[StoreDetail]] = Field(default=UNSET, alias="storeDetails")
    """Array of stores associated with the account holder. Required when onboarding account holders that have an Adyen
    `point of sale <https://docs.adyen.com/classic-platforms/platforms-for-pos>`__."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the website of the account holder."""


class AccountHolderDetails3Dict(TypedDict):
    address: ViasAddress9Dict
    bank_account_details: NotRequired[list[BankAccountDetailDict]]
    bank_aggregator_data_reference: NotRequired[str]
    business_details: NotRequired[BusinessDetails3Dict]
    email: NotRequired[str]
    full_phone_number: NotRequired[str]
    individual_details: NotRequired[IndividualDetails3Dict]
    last_review_date: NotRequired[str]
    legal_arrangements: NotRequired[list[LegalArrangementDetailDict]]
    merchant_category_code: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    payout_methods: NotRequired[list[PayoutMethodDict]]
    phone_number: NotRequired[ViasPhoneNumber3Dict]
    principal_business_address: NotRequired[ViasAddress6Dict]
    store_details: NotRequired[list[StoreDetailDict]]
    web_address: NotRequired[str]
