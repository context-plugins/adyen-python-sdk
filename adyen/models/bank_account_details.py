from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankAccountDetails(SdkBaseModel):
    account_number: Optional[str] = Field(default=UNSET, alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """The bank account type.

    Possible values: **checking** or **savings**. Defaults to **checking**."""

    branch_number: Optional[str] = Field(default=UNSET, alias="branchNumber")
    """The bank account branch number, without separators or whitespace"""

    form_factor: Optional[str] = Field(default=UNSET, alias="formFactor")
    """Business accounts with a ``formFactor`` value of **physical** are business accounts issued under the central bank
    of that country. The default value is **physical** for NL, US, and UK business accounts.

    Adyen creates a local IBAN for business accounts when the ``formFactor`` value is set to **virtual**. The local
    IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through
    the central bank of NL."""

    iban: Optional[str] = UNSET
    """The international bank account number as defined in the `ISO-13616 <https://www.iso.org/standard/81090.html>`__
    standard."""

    routing_number: Optional[str] = Field(default=UNSET, alias="routingNumber")
    """The `routing number <https://en.wikipedia.org/wiki/ABA_routing_transit_number>`__, without separators or
    whitespace."""

    sort_code: Optional[str] = Field(default=UNSET, alias="sortCode")
    """The `sort code <https://en.wikipedia.org/wiki/Sort_code>`__, without separators or whitespace."""

    type_: str = Field(alias="type")
    """**iban** or **usLocal** or **ukLocal**"""


class BankAccountDetailsDict(TypedDict):
    account_number: NotRequired[str]
    account_type: NotRequired[str]
    branch_number: NotRequired[str]
    form_factor: NotRequired[str]
    iban: NotRequired[str]
    routing_number: NotRequired[str]
    sort_code: NotRequired[str]
    type_: str
