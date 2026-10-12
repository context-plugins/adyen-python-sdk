from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authentication1 import Authentication1, Authentication1Dict
from .card_configuration2 import CardConfiguration2, CardConfiguration2Dict
from .delivery_contact1 import DeliveryContact1, DeliveryContact1Dict
from .enums.form_factor1 import FormFactor1OrStr
from .expiry2 import Expiry2, Expiry2Dict


class Card11(SdkBaseModel):
    """Contains information about the card payment instrument. Returned when you create a payment instrument with
    ``type`` **card**."""

    authentication: Optional[Authentication1] = UNSET
    """Contains the card user's password and mobile phone number. This is required when you issue cards that can be used
    to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to `3D Secure and
    digital wallets <https://docs.adyen.com/issuing/3d-secure-and-wallets>`__ for more information."""

    bin: Optional[str] = UNSET
    """The bank identification number (BIN) of the card number."""

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

    cvc: Optional[str] = UNSET
    """The CVC2 value of the card.
    > The CVC2 is not sent by default. This is only returned in the ``POST`` response for single-use virtual cards."""

    delivery_contact: Optional[DeliveryContact1] = Field(default=UNSET, alias="deliveryContact")
    """The delivery contact (name and address) for physical card delivery."""

    expiration: Optional[Expiry2] = UNSET
    """The expiration date of the card."""

    form_factor: FormFactor1OrStr = Field(alias="formFactor")
    """The form factor of the card. Possible values: **virtual**, **physical**."""

    last_four: Optional[str] = Field(default=UNSET, alias="lastFour")
    """Last last four digits of the card number."""

    number: Optional[str] = UNSET
    """The primary account number (PAN) of the card.
    > The PAN is masked by default and returned only for single-use virtual cards."""

    three_d_secure: Optional[str] = Field(default=UNSET, alias="threeDSecure")
    """The 3DS configuration of the physical or the virtual card. Possible values: **fullySupported**,
    **secureCorporate**.
    > Reach out to your Adyen contact to get the values relevant for your integration."""

    usage: Optional[str] = UNSET
    """Specifies how many times the card can be used. Possible values: **singleUse**, **multiUse**.

    > Reach out to your Adyen contact to determine the value relevant for your integration."""


class Card11Dict(TypedDict):
    authentication: NotRequired[Authentication1Dict]
    bin: NotRequired[str]
    brand: str
    brand_variant: str
    cardholder_name: str
    configuration: NotRequired[CardConfiguration2Dict]
    cvc: NotRequired[str]
    delivery_contact: NotRequired[DeliveryContact1Dict]
    expiration: NotRequired[Expiry2Dict]
    form_factor: FormFactor1OrStr
    last_four: NotRequired[str]
    number: NotRequired[str]
    three_d_secure: NotRequired[str]
    usage: NotRequired[str]
