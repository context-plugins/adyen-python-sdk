from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payment_flow import PaymentFlowOrStr
from .enums.status8 import Status8OrStr
from .vias_address7 import ViasAddress7, ViasAddress7Dict
from .vias_phone_number4 import ViasPhoneNumber4, ViasPhoneNumber4Dict


class StoreDetail(SdkBaseModel):
    address: ViasAddress7
    """The address of the physical store where the account holder will process payments from."""

    full_phone_number: Optional[str] = Field(default=UNSET, alias="fullPhoneNumber")
    """The phone number of the store provided as a single string. It will be handled as a landline phone.

    Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
    """

    logo: Optional[str] = UNSET
    """Store logo for payment method setup."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account to which the store belongs."""

    merchant_category_code: str = Field(alias="merchantCategoryCode")
    """The merchant category code (MCC) that classifies the business of the account holder."""

    merchant_house_number: Optional[str] = Field(default=UNSET, alias="merchantHouseNumber")
    """Merchant house number for payment method setup."""

    phone_number: Optional[ViasPhoneNumber4] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the store."""

    shopper_interaction: Optional[PaymentFlowOrStr] = Field(default=UNSET, alias="shopperInteraction")
    """The sales channel. Possible values: **Ecommerce**, **POS**."""

    split_configuration_uuid: Optional[str] = Field(default=UNSET, alias="splitConfigurationUUID")
    """The unique reference for the split configuration, returned when you configure splits in your Customer Area. When
    this is provided, the ``virtualAccount`` is also required. Adyen uses the configuration and the ``virtualAccount``
    to split funds between accounts in your platform."""

    status: Optional[Status8OrStr] = UNSET
    """The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**,
    **Closed**."""

    store: Optional[str] = UNSET
    """Adyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a
    store. Required when updating an existing store in an ``/updateAccountHolder`` request."""

    store_name: Optional[str] = Field(default=UNSET, alias="storeName")
    r"""The name of the account holder's store. This value is shown in shopper statements.

     * Length: Between 3 to 22 characters

     * The following characters are *not* supported: **:;}{$#@!|<>%^*+=\\**

    **Note:** storeName does not appear in American Express shopper statements by default. Contact Adyen Support to
    enable this for American Express."""

    store_reference: Optional[str] = Field(default=UNSET, alias="storeReference")
    r"""Your unique identifier for the store. The Customer Area also uses this value for the store description.

     * Length: Between 3 to 128 characters

    * The following characters are *not* supported: **:;}{$#@!|<>%^*+=\\**"""

    virtual_account: Optional[str] = Field(default=UNSET, alias="virtualAccount")
    """The account holder's ``accountCode`` where the split amount will be sent. Required when you provide the
    ``splitConfigurationUUID``."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """URL of the ecommerce store."""


class StoreDetailDict(TypedDict):
    address: ViasAddress7Dict
    full_phone_number: NotRequired[str]
    logo: NotRequired[str]
    merchant_account: str
    merchant_category_code: str
    merchant_house_number: NotRequired[str]
    phone_number: NotRequired[ViasPhoneNumber4Dict]
    shopper_interaction: NotRequired[PaymentFlowOrStr]
    split_configuration_uuid: NotRequired[str]
    status: NotRequired[Status8OrStr]
    store: NotRequired[str]
    store_name: NotRequired[str]
    store_reference: NotRequired[str]
    virtual_account: NotRequired[str]
    web_address: NotRequired[str]
