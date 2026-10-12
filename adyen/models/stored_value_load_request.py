from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.load_type import LoadTypeOrStr
from .enums.shopper_interaction import ShopperInteractionOrStr


class StoredValueLoadRequest(SdkBaseModel):
    amount: Amount
    """The amount information for the transaction."""

    load_type: Optional[LoadTypeOrStr] = Field(default=UNSET, alias="loadType")
    """The type of load you are trying to do, when absent we default to 'load'"""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    payment_method: dict[str, str] = Field(alias="paymentMethod")
    """The collection that contains the type of the payment method and its specific information if available"""

    recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="recurringDetailReference")
    reference: str
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to
    provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters."""

    shopper_interaction: Optional[ShopperInteractionOrStr] = Field(default=UNSET, alias="shopperInteraction")
    """Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a
    returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.

    This field has the following possible values:
    * ``Ecommerce`` - Online transactions where the cardholder is present (online). For better authorisation rates, we
        recommend sending the card security code (CSC) along with the request.
    * ``ContAuth`` - Card on file and/or subscription transactions, where the cardholder is known to the merchant
        (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation
        (one-click payment).
    * ``Moto`` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email
        or telephone.
    * ``POS`` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure
        payment terminal."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    store: Optional[str] = UNSET
    """The physical store, for which this payment is processed."""


class StoredValueLoadRequestDict(TypedDict):
    amount: AmountDict
    load_type: NotRequired[LoadTypeOrStr]
    merchant_account: str
    payment_method: dict[str, str]
    recurring_detail_reference: NotRequired[str]
    reference: str
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_reference: NotRequired[str]
    store: NotRequired[str]
