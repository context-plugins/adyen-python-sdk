from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.additional_sales_channel import AdditionalSalesChannelOrStr


class GeneratePciDescriptionRequest(SdkBaseModel):
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

    language: Optional[str] = UNSET
    """Sets the language of the PCI questionnaire. Its value is a two-character `ISO 639-1
    <https://en.wikipedia.org/wiki/ISO_639-1>`__ language code, for example, **en**."""


class GeneratePciDescriptionRequestDict(TypedDict):
    additional_sales_channels: NotRequired[list[AdditionalSalesChannelOrStr]]
    language: NotRequired[str]
