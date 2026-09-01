from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.entry_mode import EntryModeOrStr
from .enums.identification_type11 import IdentificationType11OrStr
from .enums.stored_value_account_type1 import StoredValueAccountType1OrStr


class StoredValueAccountId(SdkBaseModel):
    """Identification of the stored value account or the stored value card and the associated product sold by the Sale
    System for stored value requests."""

    stored_value_account_type: StoredValueAccountType1OrStr = Field(alias="StoredValueAccountType")
    """Type of stored value account. Allows the distinction of the stored value instrument to access the stored value
    account. Possible values:
    * **GiftCard**
    * **Other**
    * **PhoneCard**"""

    stored_value_provider: Optional[str] = Field(default=UNSET, alias="StoredValueProvider")
    """Identification of the provider of the stored value account load/reload. When the ProductCode is not sufficient to
    identify the provider host which delivers the load or reload of the stored value account (for example if it contains
    the identification of the application.)"""

    owner_name: Optional[str] = Field(default=UNSET, alias="OwnerName")
    """Name of the owner of a stored value account."""

    expiry_date: Optional[int] = Field(default=UNSET, alias="ExpiryDate")
    """Date after which the card cannot be used. If EMV expiry date is present, it overrides Track2 information. Format
    is MMYY."""

    entry_mode: list[EntryModeOrStr] = Field(alias="EntryMode")
    """Entry mode of the payment instrument information. In the Payment, Loyalty, or StoredValue Request messages, it
    informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. (e.g.
    because the payment instrument information are a barcode read by the Cashier on a scanner device). Possible values:
    * **Contactless**
    * **File**
    * **ICC**
    * **Keyed**
    * **MagStripe**
    * **Manual**
    * **Mobile**
    * **RFID**
    * **Scanned**
    * **SynchronousICC**
    * **Tapped**"""

    identification_type: IdentificationType11OrStr = Field(alias="IdentificationType")
    """Type of account identification. In a request message, it informs the POI System the type of the account or card
    identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the
    Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card
    identification. Possible values:
    * **AccountNumber**
    * **BarCode**
    * **ISOTrack2**
    * **PAN**
    * **PhoneNumber**"""

    stored_value_id: str = Field(alias="StoredValueID")
    """Stored value account identification. The identification of the stored value account conforming to the
    IdentificationType."""


class StoredValueAccountIdDict(TypedDict):
    stored_value_account_type: StoredValueAccountType1OrStr
    stored_value_provider: NotRequired[str]
    owner_name: NotRequired[str]
    expiry_date: NotRequired[int]
    entry_mode: list[EntryModeOrStr]
    identification_type: IdentificationType11OrStr
    stored_value_id: str
