from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status41 import Status41OrStr
from .store_split_configuration1 import StoreSplitConfiguration1, StoreSplitConfiguration1Dict
from .sub_merchant_data1 import SubMerchantData1, SubMerchantData1Dict
from .updatable_address1 import UpdatableAddress1, UpdatableAddress1Dict


class UpdateStoreRequest(SdkBaseModel):
    address: Optional[UpdatableAddress1] = UNSET
    """The address of the store. It is not possible to update the country of the store."""

    business_line_ids: Optional[list[str]] = Field(default=UNSET, alias="businessLineIds")
    """The unique identifiers of the `business lines
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__resParam_id>`__ that the store is
    associated with."""

    description: Optional[str] = UNSET
    """The description of the store."""

    external_reference_id: Optional[str] = Field(default=UNSET, alias="externalReferenceId")
    """The unique identifier of the store, used by certain payment methods and tax authorities.

    Required for CNPJ in Brazil, in the format 00.000.000/0000-00 separated by dots, slashes, hyphens, or without
    separators.

    Optional for SIRET in France, up to 14 digits.

    Optional for Zip in Australia, up to 50 digits."""

    phone_number: Optional[str] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the store, including '+' and country code in the `E.164
    <https://en.wikipedia.org/wiki/E.164>`__ format. If passed in a different format, we convert and validate the phone
    number against E.164."""

    split_configuration: Optional[StoreSplitConfiguration1] = Field(default=UNSET, alias="splitConfiguration")
    """Rules for Adyen for Platforms merchants to split the transaction amount and fees."""

    status: Optional[Status41OrStr] = UNSET
    """The status of the store. Possible values are:

    - **active**: This value is assigned automatically when a store is created.
    - **inactive**: The maximum `transaction limits and number of Store-and-Forward transactions
        <https://docs.adyen.com/point-of-sale/determine-account-structure/configure-features#payment-features>`__ for
        the store are set to 0. This blocks new transactions, but captures are still possible.
    - **closed**: The terminals of the store are reassigned to the merchant inventory, so they can't process payments.

    You can change the status from **active** to **inactive**, and from **inactive** to **active** or **closed**. Once
    **closed**, a store can't be reopened."""

    sub_merchant_data: Optional[SubMerchantData1] = Field(default=UNSET, alias="subMerchantData")
    """The sub-merchant data relevant for registered payment facilitators transacting on standalone terminals."""


class UpdateStoreRequestDict(TypedDict):
    address: NotRequired[UpdatableAddress1 | UpdatableAddress1Dict]
    business_line_ids: NotRequired[list[str]]
    description: NotRequired[str]
    external_reference_id: NotRequired[str]
    phone_number: NotRequired[str]
    split_configuration: NotRequired[StoreSplitConfiguration1 | StoreSplitConfiguration1Dict]
    status: NotRequired[Status41OrStr]
    sub_merchant_data: NotRequired[SubMerchantData1 | SubMerchantData1Dict]
