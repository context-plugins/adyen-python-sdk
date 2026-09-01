from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .localized_information2 import LocalizedInformation2, LocalizedInformation2Dict
from .store_location1 import StoreLocation1, StoreLocation1Dict
from .store_split_configuration1 import StoreSplitConfiguration1, StoreSplitConfiguration1Dict
from .sub_merchant_data1 import SubMerchantData1, SubMerchantData1Dict


class StoreCreationRequest(SdkBaseModel):
    address: StoreLocation1
    """The address of the store."""

    business_line_ids: Optional[list[str]] = Field(default=UNSET, alias="businessLineIds")
    """The unique identifiers of the `business lines
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/businessLines#responses-200-id>`__ that the store is
    associated with. If not specified, the business line of the merchant account is used. Required when there are
    multiple business lines under the merchant account."""

    description: str
    """Your description of the store."""

    external_reference_id: Optional[str] = Field(default=UNSET, alias="externalReferenceId")
    """The unique identifier of the store, used by certain payment methods and tax authorities.

    Required for CNPJ in Brazil, in the format 00.000.000/0000-00 separated by dots, slashes, hyphens, or without
    separators.

    Optional for SIRET in France, up to 14 digits.

    Optional for Zip in Australia, up to 50 digits."""

    localized_information: Optional[LocalizedInformation2] = Field(default=UNSET, alias="localizedInformation")
    """Localized information about the store."""

    phone_number: str = Field(alias="phoneNumber")
    """The phone number of the store, including '+' and country code in the `E.164
    <https://en.wikipedia.org/wiki/E.164>`__ format. If passed in a different format, we convert and validate the phone
    number against E.164."""

    reference: Optional[str] = UNSET
    """Your reference to recognize the store by. Also known as the store code.
     Allowed characters: lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and
        underscore (_).

    If you do not provide a reference in your POST request, it is populated with the Adyen-generated `id
    <https://docs.adyen.com/api-explorer/Management/latest/post/stores#responses-200-id>`__."""

    shopper_statement: str = Field(alias="shopperStatement")
    """The store name to be shown on the shopper's bank or credit card statement and on the shopper receipt. Maximum
    length: 22 characters; can't be all numbers."""

    split_configuration: Optional[StoreSplitConfiguration1] = Field(default=UNSET, alias="splitConfiguration")
    """Rules for Adyen for Platforms merchants to split the transaction amount and fees."""

    sub_merchant_data: Optional[SubMerchantData1] = Field(default=UNSET, alias="subMerchantData")
    """The sub-merchant data relevant for registered payment facilitators transacting on standalone terminals."""


class StoreCreationRequestDict(TypedDict):
    address: StoreLocation1 | StoreLocation1Dict
    business_line_ids: NotRequired[list[str]]
    description: str
    external_reference_id: NotRequired[str]
    localized_information: NotRequired[LocalizedInformation2 | LocalizedInformation2Dict]
    phone_number: str
    reference: NotRequired[str]
    shopper_statement: str
    split_configuration: NotRequired[StoreSplitConfiguration1 | StoreSplitConfiguration1Dict]
    sub_merchant_data: NotRequired[SubMerchantData1 | SubMerchantData1Dict]
