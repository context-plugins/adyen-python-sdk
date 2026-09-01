from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChAccChangeInd(str, Enum):
    """Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including
    Billing or Shipping address, new payment account, or new user(s) added. Allowed values:
    * **01** — Changed during this transaction
    * **02** — Less than 30 days
    * **03** — 30–60 days
    * **04** — More than 60 days, Indicates when the shipping address used for this transaction was first used with the
        3DS Requestor.
    Allowed values:
    * **01** — This transaction
    * **02** — Less than 30 days
    * **03** — 30–60 days
    * **04** — More than 60 days, Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor.
        Allowed values:
    * **01** — Frictionless authentication occurred by ACS.
    * **02** — Cardholder challenge occurred by ACS.
    * **03** — AVS verified.
    * **04** — Other issuer methods."""

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"

    __str__ = str.__str__


ChAccChangeIndOrStr: TypeAlias = Annotated[ChAccChangeInd | str, open_enum_validator(ChAccChangeInd)]
