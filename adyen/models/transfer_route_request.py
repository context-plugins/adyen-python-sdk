from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .counterparty1 import Counterparty1, Counterparty1Dict
from .enums.priority1 import Priority1OrStr


class TransferRouteRequest(SdkBaseModel):
    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the source `balance account
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id>`__. Required if
    ``counterparty`` is **transferInstrumentId**."""

    balance_platform: str = Field(alias="balancePlatform")
    """The unique identifier assigned to the balance platform associated with the account holder."""

    category: Literal["bank"] = "bank"
    """The type of transfer. Possible values:

      - **bank**: Transfer to a `transfer instrument
            <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__ or a
            bank account."""

    counterparty: Optional[Counterparty1] = UNSET
    """The recipient of the funds transfer. A bank account or a transfer instrument."""

    country: Optional[str] = UNSET
    """The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**.
     > Either ``counterparty`` or ``country`` field must be provided in a transfer route request."""

    currency: str
    """The three-character ISO currency code of transfer. For example, **USD** or **EUR**."""

    priorities: Optional[list[Priority1OrStr]] = UNSET
    """The list of priorities for the bank transfer. Priorities set the speed at which the transfer is sent and the fees
    that you have to pay. Multiple values can be provided. Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN)."""


class TransferRouteRequestDict(TypedDict):
    balance_account_id: NotRequired[str]
    balance_platform: str
    category: Literal["bank"]
    counterparty: NotRequired[Counterparty1Dict]
    country: NotRequired[str]
    currency: str
    priorities: NotRequired[list[Priority1OrStr]]
