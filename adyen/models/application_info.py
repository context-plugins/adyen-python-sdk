from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_field1 import CommonField1, CommonField1Dict
from .common_field2 import CommonField2, CommonField2Dict
from .common_field4 import CommonField4, CommonField4Dict
from .external_platform import ExternalPlatform, ExternalPlatformDict
from .merchant_device import MerchantDevice, MerchantDeviceDict
from .shopper_interaction_device import ShopperInteractionDevice, ShopperInteractionDeviceDict


class ApplicationInfo(SdkBaseModel):
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    adyen_library: Optional[CommonField4] = Field(default=UNSET, alias="adyenLibrary")
    """Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example,
    Magento plugin, Java API library, etc."""

    adyen_payment_source: Optional[CommonField1] = Field(default=UNSET, alias="adyenPaymentSource")
    """Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc."""

    external_platform: Optional[ExternalPlatform] = Field(default=UNSET, alias="externalPlatform")
    """Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc."""

    merchant_application: Optional[CommonField2] = Field(default=UNSET, alias="merchantApplication")
    """Merchant developed software, such as cashier application, used to interact with the Adyen API."""

    merchant_device: Optional[MerchantDevice] = Field(default=UNSET, alias="merchantDevice")
    """Merchant device information."""

    shopper_interaction_device: Optional[ShopperInteractionDevice] = Field(
        default=UNSET, alias="shopperInteractionDevice"
    )
    """Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests."""


class ApplicationInfoDict(TypedDict):
    adyen_library: NotRequired[CommonField4 | CommonField4Dict]
    adyen_payment_source: NotRequired[CommonField1 | CommonField1Dict]
    external_platform: NotRequired[ExternalPlatform | ExternalPlatformDict]
    merchant_application: NotRequired[CommonField2 | CommonField2Dict]
    merchant_device: NotRequired[MerchantDevice | MerchantDeviceDict]
    shopper_interaction_device: NotRequired[ShopperInteractionDevice | ShopperInteractionDeviceDict]
