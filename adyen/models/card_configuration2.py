from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_address1 import BulkAddress1, BulkAddress1Dict


class CardConfiguration2(SdkBaseModel):
    """Contains information about the configuration profile for your cards. The configuration profile consists of
    settings required when creating a physical or a virtual card. You identify a configuration profile with its
    ``configurationProfileId``.

    When you provide this field in a request, you can override the settings of an existing configuration profile.

    Reach out to your Adyen contact to get the values that you can send in this object."""

    activation: Optional[str] = UNSET
    """The activation label attached to the card that contains the activation instructions.

    This field overrides the activation label design ID defined in the card configuration profile."""

    activation_url: Optional[str] = Field(default=UNSET, alias="activationUrl")
    """Your app's URL, if you want to activate cards through your app. For example, **my-app://ref1236a7d**. A QR code
    is created based on this URL, and is included in the carrier. Before you use this field, reach out to your Adyen
    contact to set up the QR code process.

    Maximum length: 255 characters."""

    bulk_address: Optional[BulkAddress1] = Field(default=UNSET, alias="bulkAddress")
    """Overrides the shipment bulk address defined in the card configuration profile."""

    card_image_id: Optional[str] = Field(default=UNSET, alias="cardImageId")
    """The unique identifier of the card image. This image is printed on the full front of the card."""

    carrier: Optional[str] = UNSET
    """The letter or packaging to which the card is attached.

    This field overrides the carrier design ID defined in the card configuration profile."""

    carrier_image_id: Optional[str] = Field(default=UNSET, alias="carrierImageId")
    """The unique identifier of the carrier image. This image is printed on the letter to which the card is attached."""

    configuration_profile_id: str = Field(alias="configurationProfileId")
    """The unique identifier of the card configuration profile that contains the settings that are applied to the card.
    For example, the envelope and PIN mailer designs or the logistics company handling the shipment.

    You can override some of the existing settings in the configuration profile by providing the corresponding fields in
    the ``configuration`` object. For example, send the ``shipmentMethod`` to override the logistics company defined in
    the card configuration profile."""

    currency: Optional[str] = UNSET
    """The three-letter `ISO-4217 <https://en.wikipedia.org/wiki/ISO_4217>`__ currency code of the card. For example,
    **EUR**.

    This field overrides the existing currency setting on the card configuration profile."""

    envelope: Optional[str] = UNSET
    """Overrides the envelope design ID defined in the card configuration profile."""

    insert: Optional[str] = UNSET
    """Any additional material, such as marketing material, that is shipped together with the card.

    This field overrides the insert design ID defined in the card configuration profile."""

    language: Optional[str] = UNSET
    """The two-letter `ISO-639-1 <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__ language code of the card.
    For example, **en**."""

    logo_image_id: Optional[str] = Field(default=UNSET, alias="logoImageId")
    """The unique identifier of the logo image. This image is printed on the partial front of the card, for example, a
    logo on the upper right corner."""

    pin_mailer: Optional[str] = Field(default=UNSET, alias="pinMailer")
    """The letter on which the PIN of the card is printed.

    This field overrides the PIN mailer design ID defined in the card configuration profile."""

    print_line: Optional[str] = Field(default=UNSET, alias="printLine")
    """Print Line.

    Text printed on the physical card below the cardholder name. You provide the value, which can be up to 26
    characters."""

    shipment_method: Optional[str] = Field(default=UNSET, alias="shipmentMethod")
    """The logistics company that ships the card.

    This field overrides the logistics company defined in the card configuration profile."""


class CardConfiguration2Dict(TypedDict):
    activation: NotRequired[str]
    activation_url: NotRequired[str]
    bulk_address: NotRequired[BulkAddress1Dict]
    card_image_id: NotRequired[str]
    carrier: NotRequired[str]
    carrier_image_id: NotRequired[str]
    configuration_profile_id: str
    currency: NotRequired[str]
    envelope: NotRequired[str]
    insert: NotRequired[str]
    language: NotRequired[str]
    logo_image_id: NotRequired[str]
    pin_mailer: NotRequired[str]
    print_line: NotRequired[str]
    shipment_method: NotRequired[str]
