from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonField(SdkBaseModel):
    """Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc., Merchant
    developed software, such as cashier application, used to interact with the Adyen API., Adyen-developed software,
    such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library,
    etc."""

    name: Optional[str] = UNSET
    """Name of the field. For example, Name of External Platform."""

    version: Optional[str] = UNSET
    """Version of the field. For example, Version of External Platform."""


class CommonFieldDict(TypedDict):
    name: NotRequired[str]
    version: NotRequired[str]
