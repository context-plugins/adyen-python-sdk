from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IbanaccountIdentifier2(SdkBaseModel):
    """The international bank account number as defined in the ISO-13616 standard."""

    bban: str
    """The Basic Bank Account Number (BBAN) component of the IBAN."""

    bic: str
    """BIC of a bank account."""

    iban: str
    """The international bank account number as defined in the `ISO-13616 <https://www.iso.org/standard/81090.html>`__
    standard. This is the national identifier for the bank account, following the country-specific format, and is part
    of the full IBAN."""


class IbanaccountIdentifier2Dict(TypedDict):
    bban: str
    bic: str
    iban: str
