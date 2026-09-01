from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.additional_sales_channel import AdditionalSalesChannelOrStr


class CalculatePciStatusRequest(SdkBaseModel):
    additional_sales_channels: Optional[list[AdditionalSalesChannelOrStr]] = Field(
        default=UNSET, alias="additionalSalesChannels"
    )
    """An array of additional sales channels to generate PCI questionnaires. Include the relevant sales channels if you
    need your user to sign PCI questionnaires. Not required if you `create stores <https://docs.adyen.com/platforms>`__
    and `add payment methods <https://docs.adyen.com/adyen-for-platforms-model>`__ before you generate the
    questionnaires.

    Possible values:
    * **eCommerce**
    * **pos**
    * **ecomMoto**
    * **posMoto**"""


class CalculatePciStatusRequestDict(TypedDict):
    additional_sales_channels: NotRequired[list[AdditionalSalesChannelOrStr]]
