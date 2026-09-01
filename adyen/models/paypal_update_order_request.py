from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount44 import Amount44, Amount44Dict
from .amount45 import Amount45, Amount45Dict
from .amount46 import Amount46, Amount46Dict
from .delivery_address5 import DeliveryAddress5, DeliveryAddress5Dict
from .delivery_method import DeliveryMethod, DeliveryMethodDict
from .tax_total2 import TaxTotal2, TaxTotal2Dict


class PaypalUpdateOrderRequest(SdkBaseModel):
    amount: Optional[Amount44] = UNSET
    """The updated final payment amount. This amount is the item total plus the shipping costs of the selected
    ``deliveryMethod``."""

    delivery_address: Optional[DeliveryAddress5] = Field(default=UNSET, alias="deliveryAddress")
    """The delivery address for this order."""

    delivery_methods: Optional[list[DeliveryMethod]] = Field(default=UNSET, alias="deliveryMethods")
    """The list of new delivery methods and the cost of each."""

    discount_amount: Optional[Amount45] = Field(default=UNSET, alias="discountAmount")
    """The discount amount for this order."""

    payment_data: Optional[str] = Field(default=UNSET, alias="paymentData")
    """The ``paymentData`` from the client side. This value changes every time you make a ``/paypal/updateOrder``
    request."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The original ``pspReference`` from the ``/payments`` response."""

    session_id: Optional[str] = Field(default=UNSET, alias="sessionId")
    """The original ``sessionId`` from the ``/sessions`` response."""

    shipping_amount: Optional[Amount46] = Field(default=UNSET, alias="shippingAmount")
    """The shipping amount for this order."""

    tax_total: Optional[TaxTotal2] = Field(default=UNSET, alias="taxTotal")
    """Total tax amount from the order."""


class PaypalUpdateOrderRequestDict(TypedDict):
    amount: NotRequired[Amount44 | Amount44Dict]
    delivery_address: NotRequired[DeliveryAddress5 | DeliveryAddress5Dict]
    delivery_methods: NotRequired[list[DeliveryMethod | DeliveryMethodDict]]
    discount_amount: NotRequired[Amount45 | Amount45Dict]
    payment_data: NotRequired[str]
    psp_reference: NotRequired[str]
    session_id: NotRequired[str]
    shipping_amount: NotRequired[Amount46 | Amount46Dict]
    tax_total: NotRequired[TaxTotal2 | TaxTotal2Dict]
