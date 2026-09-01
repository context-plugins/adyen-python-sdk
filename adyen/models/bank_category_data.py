from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.priority1 import Priority1OrStr
from .enums.type310 import Type310OrStr


class BankCategoryData(SdkBaseModel):
    priority: Optional[Priority1OrStr] = UNSET
    """The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have
    to pay. Required for transfers with ``category`` **bank**.

    Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN)."""

    type_: Optional[Type310OrStr] = Field(default=UNSET, alias="type")
    """**bank**"""


class BankCategoryDataDict(TypedDict):
    priority: NotRequired[Priority1OrStr]
    type_: NotRequired[Type310OrStr]
