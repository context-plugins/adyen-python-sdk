from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authentication1 import Authentication1, Authentication1Dict
from .card_configuration2 import CardConfiguration2, CardConfiguration2Dict
from .delivery_contact1 import DeliveryContact1, DeliveryContact1Dict
from .enums.form_factor1 import FormFactor1OrStr


class CardInfo1(SdkBaseModel):
    """Contains information about the card. Required when you create a payment instrument of ``type`` **card**."""

    authentication: Optional[Authentication1] = UNSET
    """Contains the card user's password and mobile phone number. This is required when you issue cards that can be used
    to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to `3D Secure and
    digital wallets <https://docs.adyen.com/issuing/3d-secure-and-wallets>`__ for more information."""

    brand: str
    """The brand of the physical or the virtual card. Possible values: **visa**, **mc**."""

    brand_variant: str = Field(alias="brandVariant")
    """The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**. >Reach out to
    your Adyen contact to get the values relevant for your integration."""

    cardholder_name: str = Field(alias="cardholderName")
    """The name of the cardholder.
     Maximum length: 26 characters."""

    configuration: Optional[CardConfiguration2] = UNSET
    """Contains information about the configuration profile for your cards. The configuration profile consists of
    settings required when creating a physical or a virtual card. You identify a configuration profile with its
    ``configurationProfileId``.

    When you provide this field in a request, you can override the settings of an existing configuration profile.

    Reach out to your Adyen contact to get the values that you can send in this object."""

    delivery_contact: Optional[DeliveryContact1] = Field(default=UNSET, alias="deliveryContact")
    """The delivery contact (name and address) for physical card delivery."""

    form_factor: FormFactor1OrStr = Field(alias="formFactor")
    """The form factor of the card. Possible values: **virtual**, **physical**."""

    three_d_secure: Optional[str] = Field(default=UNSET, alias="threeDSecure")
    """The 3DS configuration of the physical or the virtual card. Possible values: **fullySupported**,
    **secureCorporate**.
    > Reach out to your Adyen contact to get the values relevant for your integration."""

    usage: Optional[str] = UNSET
    """Specifies how many times the card can be used. Possible values: **singleUse**, **multiUse**.

    > Reach out to your Adyen contact to determine the value relevant for your integration."""


class CardInfo1Dict(TypedDict):
    authentication: NotRequired[Authentication1 | Authentication1Dict]
    brand: str
    brand_variant: str
    cardholder_name: str
    configuration: NotRequired[CardConfiguration2 | CardConfiguration2Dict]
    delivery_contact: NotRequired[DeliveryContact1 | DeliveryContact1Dict]
    form_factor: FormFactor1OrStr
    three_d_secure: NotRequired[str]
    usage: NotRequired[str]
