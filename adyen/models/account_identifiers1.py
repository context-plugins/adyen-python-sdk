from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .achaccount_identifier1 import AchaccountIdentifier1, AchaccountIdentifier1Dict
from .bacsaccount_identifier2 import BacsaccountIdentifier2, BacsaccountIdentifier2Dict
from .bsbaccount_identifier2 import BsbaccountIdentifier2, BsbaccountIdentifier2Dict
from .eftaccount_identifier2 import EftaccountIdentifier2, EftaccountIdentifier2Dict
from .ibanaccount_identifier2 import IbanaccountIdentifier2, IbanaccountIdentifier2Dict
from .rixaccount_identifier2 import RixaccountIdentifier2, RixaccountIdentifier2Dict


class AccountIdentifiers1(SdkBaseModel):
    """Contains various codes and details used to uniquely identify the bank account across different regions."""

    ach: Optional[AchaccountIdentifier1] = UNSET
    """Identifiers relevant for Automated Clearing House (ACH) payments, primarily used in the United States."""

    bacs: Optional[BacsaccountIdentifier2] = UNSET
    """Identifiers relevant for Bankers' Automated Clearing Services (BACS) payments, primarily used in the United
    Kingdom."""

    bsb: Optional[BsbaccountIdentifier2] = UNSET
    """Identifiers relevant for Australian banking, specifically for BSB (Bank-State-Branch) numbers."""

    eft: Optional[EftaccountIdentifier2] = UNSET
    """Identifiers relevant for Electronic Funds Transfer (EFT) payments, commonly used in Canada."""

    iban: Optional[IbanaccountIdentifier2] = UNSET
    """The international bank account number as defined in the ISO-13616 standard."""

    rix: Optional[RixaccountIdentifier2] = UNSET
    """Identifiers relevant for the Rix (Russian Interbank eXchange) system, used for interbank payments within
    Russia."""


class AccountIdentifiers1Dict(TypedDict):
    ach: NotRequired[AchaccountIdentifier1Dict]
    bacs: NotRequired[BacsaccountIdentifier2Dict]
    bsb: NotRequired[BsbaccountIdentifier2Dict]
    eft: NotRequired[EftaccountIdentifier2Dict]
    iban: NotRequired[IbanaccountIdentifier2Dict]
    rix: NotRequired[RixaccountIdentifier2Dict]
