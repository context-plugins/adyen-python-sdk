from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..aulocal_account_identification import AulocalAccountIdentification, AulocalAccountIdentificationDict
from ..brlocal_account_identification import BrlocalAccountIdentification, BrlocalAccountIdentificationDict
from ..calocal_account_identification import CalocalAccountIdentification, CalocalAccountIdentificationDict
from ..czlocal_account_identification import CzlocalAccountIdentification, CzlocalAccountIdentificationDict
from ..dklocal_account_identification import DklocalAccountIdentification, DklocalAccountIdentificationDict
from ..hklocal_account_identification import HklocalAccountIdentification, HklocalAccountIdentificationDict
from ..hulocal_account_identification import HulocalAccountIdentification, HulocalAccountIdentificationDict
from ..iban_account_identification import IbanAccountIdentification, IbanAccountIdentificationDict
from ..nolocal_account_identification import NolocalAccountIdentification, NolocalAccountIdentificationDict
from ..number_and_bic_account_identification import (
    NumberAndBicAccountIdentification,
    NumberAndBicAccountIdentificationDict,
)
from ..nzlocal_account_identification import NzlocalAccountIdentification, NzlocalAccountIdentificationDict
from ..pllocal_account_identification import PllocalAccountIdentification, PllocalAccountIdentificationDict
from ..selocal_account_identification import SelocalAccountIdentification, SelocalAccountIdentificationDict
from ..sglocal_account_identification import SglocalAccountIdentification, SglocalAccountIdentificationDict
from ..uklocal_account_identification import UklocalAccountIdentification, UklocalAccountIdentificationDict
from ..uslocal_account_identification import UslocalAccountIdentification, UslocalAccountIdentificationDict

AccountIdentification2: TypeAlias = Annotated[
    (
        Annotated[AulocalAccountIdentification, Tag("auLocal")]
        | Annotated[BrlocalAccountIdentification, Tag("brLocal")]
        | Annotated[CalocalAccountIdentification, Tag("caLocal")]
        | Annotated[CzlocalAccountIdentification, Tag("czLocal")]
        | Annotated[DklocalAccountIdentification, Tag("dkLocal")]
        | Annotated[HklocalAccountIdentification, Tag("hkLocal")]
        | Annotated[HulocalAccountIdentification, Tag("huLocal")]
        | Annotated[IbanAccountIdentification, Tag("iban")]
        | Annotated[NolocalAccountIdentification, Tag("noLocal")]
        | Annotated[NzlocalAccountIdentification, Tag("nzLocal")]
        | Annotated[NumberAndBicAccountIdentification, Tag("numberAndBic")]
        | Annotated[PllocalAccountIdentification, Tag("plLocal")]
        | Annotated[SelocalAccountIdentification, Tag("seLocal")]
        | Annotated[SglocalAccountIdentification, Tag("sgLocal")]
        | Annotated[UklocalAccountIdentification, Tag("ukLocal")]
        | Annotated[UslocalAccountIdentification, Tag("usLocal")]
    ),
    WireDiscriminator("type"),
]
"""Contains the bank account details. The fields required in this object depend on the country of the bank account and
the currency of the transfer."""

AccountIdentification2Dict: TypeAlias = (
    AulocalAccountIdentificationDict
    | BrlocalAccountIdentificationDict
    | CalocalAccountIdentificationDict
    | CzlocalAccountIdentificationDict
    | DklocalAccountIdentificationDict
    | HklocalAccountIdentificationDict
    | HulocalAccountIdentificationDict
    | IbanAccountIdentificationDict
    | NolocalAccountIdentificationDict
    | NzlocalAccountIdentificationDict
    | NumberAndBicAccountIdentificationDict
    | PllocalAccountIdentificationDict
    | SelocalAccountIdentificationDict
    | SglocalAccountIdentificationDict
    | UklocalAccountIdentificationDict
    | UslocalAccountIdentificationDict
)
