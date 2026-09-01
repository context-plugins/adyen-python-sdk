from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipNameIndicator(str, Enum):
    """Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction.
    Allowed values:
    * **01** — Account Name identical to shipping Name
    * **02** — Account Name different to shipping Name, Indicates whether the 3DS Requestor has experienced suspicious
        activity (including previous fraud) on the cardholder account.
    Allowed values:
    * **01** — No suspicious activity has been observed
    * **02** — Suspicious activity has been observed"""

    _01 = "01"
    _02 = "02"

    __str__ = str.__str__


ShipNameIndicatorOrStr: TypeAlias = Annotated[ShipNameIndicator | str, open_enum_validator(ShipNameIndicator)]
