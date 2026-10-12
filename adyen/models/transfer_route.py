from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.category2 import Category2OrStr
from .enums.priority2 import Priority2OrStr
from .unions.requirement import Requirement, RequirementDict


class TransferRoute(SdkBaseModel):
    category: Optional[Category2OrStr] = UNSET
    """The type of transfer.

     Possible values:

      - **bank**: Transfer to a `transfer instrument
            <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__ or a
            bank account."""

    country: Optional[str] = UNSET
    """The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**."""

    currency: Optional[str] = UNSET
    """The three-character ISO currency code of transfer. For example, **USD** or **EUR**."""

    priority: Optional[Priority2OrStr] = UNSET
    """The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have
    to pay. Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN)."""

    requirements: Optional[list[Requirement]] = UNSET
    """A set of rules defined by clearing houses and banking partners. Your transfer request must adhere to these rules
    to ensure successful initiation of transfer. Based on the priority, one or more requirements may be returned. Each
    requirement is defined with a ``type`` and ``description``."""


class TransferRouteDict(TypedDict):
    category: NotRequired[Category2OrStr]
    country: NotRequired[str]
    currency: NotRequired[str]
    priority: NotRequired[Priority2OrStr]
    requirements: NotRequired[list[RequirementDict]]
