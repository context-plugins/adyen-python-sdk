from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Priority1(str, Enum):
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

    CROSS_BORDER = "crossBorder"
    FAST = "fast"
    INSTANT = "instant"
    INTERNAL = "internal"
    REGULAR = "regular"
    WIRE = "wire"

    __str__ = str.__str__


Priority1OrStr: TypeAlias = Annotated[Priority1 | str, open_enum_validator(Priority1)]
