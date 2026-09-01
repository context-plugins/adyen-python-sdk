from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_data1 import CardData1, CardData1Dict
from .check_data1 import CheckData1, CheckData1Dict
from .enums.payment_instrument_type11 import PaymentInstrumentType11OrStr
from .mobile_data1 import MobileData1, MobileData1Dict
from .stored_value_account_id import StoredValueAccountId, StoredValueAccountIdDict


class PaymentInstrumentData1(SdkBaseModel):
    """Data related to the instrument of payment for the transaction. If this type of payment card is configured to send
    information if the CardAcquisition response."""

    payment_instrument_type: PaymentInstrumentType11OrStr = Field(alias="PaymentInstrumentType")
    """Type of payment instrument. Possible values:
    * **Card**
    * **Cash**
    * **Check**
    * **Mobile**
    * **StoredValue**"""

    protected_card_data: Optional[str] = Field(default=UNSET, alias="ProtectedCardData")
    """Sensitive information related to the payment card, protected by CMS. SensitiveCardData protected by CMS
    EnvelopedData."""

    card_data: Optional[CardData1] = Field(default=UNSET, alias="CardData")
    """Information related to the payment card used for the transaction. If PaymentInstrumentType is Card."""

    check_data: Optional[CheckData1] = Field(default=UNSET, alias="CheckData")
    """Information related to the paper check used for the transaction. If PaymentInstrumentType is Check."""

    mobile_data: Optional[MobileData1] = Field(default=UNSET, alias="MobileData")
    """Information related to the mobile for the payment transaction. If PaymentInstrumentType is Mobile."""

    stored_value_account_id: Optional[StoredValueAccountId] = Field(default=UNSET, alias="StoredValueAccountID")
    """Identification of the stored value account or the stored value card and the associated product sold by the Sale
    System for stored value requests."""


class PaymentInstrumentData1Dict(TypedDict):
    payment_instrument_type: PaymentInstrumentType11OrStr
    protected_card_data: NotRequired[str]
    card_data: NotRequired[CardData1 | CardData1Dict]
    check_data: NotRequired[CheckData1 | CheckData1Dict]
    mobile_data: NotRequired[MobileData1 | MobileData1Dict]
    stored_value_account_id: NotRequired[StoredValueAccountId | StoredValueAccountIdDict]
