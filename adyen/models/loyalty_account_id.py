from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.entry_mode import EntryModeOrStr
from .enums.identification_support1 import IdentificationSupport1OrStr
from .enums.identification_type11 import IdentificationType11OrStr


class LoyaltyAccountId(SdkBaseModel):
    """Identification of a Loyalty account. In the Payment Request message, it allows to identify the loyalty account by
    the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the
    Cashier on a scanner device)."""

    entry_mode: list[EntryModeOrStr] = Field(alias="EntryMode")
    """Entry mode of the payment instrument information. In the Payment, Loyalty or StoredValue Request messages, it
    informs the POI System the entry mode of the payment instrument information when read by the Sale Terminal. In the
    Payment, Loyalty or StoredValue Response messages, it informs the Sale System the entry mode of the payment
    instrument. Possible values:
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

    identification_support: Optional[IdentificationSupport1OrStr] = Field(default=UNSET, alias="IdentificationSupport")
    """Support of the loyalty account identification. Allows knowing where and how you have found the loyalty account
    identification. Possible values:
    * **HybridCard**
    * **LinkedCard**
    * **LoyaltyCard**
    * **NoCard**"""

    loyalty_id: str = Field(alias="LoyaltyID")
    """Loyalty account identification conforming to the IdentificationType."""


class LoyaltyAccountIdDict(TypedDict):
    entry_mode: list[EntryModeOrStr]
    identification_type: IdentificationType11OrStr
    identification_support: NotRequired[IdentificationSupport1OrStr]
    loyalty_id: str
