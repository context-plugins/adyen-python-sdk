from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..aulocal_account_identification1 import AulocalAccountIdentification1, AulocalAccountIdentification1Dict
from ..brlocal_account_identification1 import BrlocalAccountIdentification1, BrlocalAccountIdentification1Dict
from ..calocal_account_identification1 import CalocalAccountIdentification1, CalocalAccountIdentification1Dict
from ..czlocal_account_identification1 import CzlocalAccountIdentification1, CzlocalAccountIdentification1Dict
from ..dklocal_account_identification1 import DklocalAccountIdentification1, DklocalAccountIdentification1Dict
from ..hklocal_account_identification1 import HklocalAccountIdentification1, HklocalAccountIdentification1Dict
from ..hulocal_account_identification1 import HulocalAccountIdentification1, HulocalAccountIdentification1Dict
from ..iban_account_identification1 import IbanAccountIdentification1, IbanAccountIdentification1Dict
from ..nolocal_account_identification1 import NolocalAccountIdentification1, NolocalAccountIdentification1Dict
from ..number_and_bic_account_identification1 import (
    NumberAndBicAccountIdentification1,
    NumberAndBicAccountIdentification1Dict,
)
from ..nzlocal_account_identification1 import NzlocalAccountIdentification1, NzlocalAccountIdentification1Dict
from ..pllocal_account_identification1 import PllocalAccountIdentification1, PllocalAccountIdentification1Dict
from ..selocal_account_identification1 import SelocalAccountIdentification1, SelocalAccountIdentification1Dict
from ..sglocal_account_identification1 import SglocalAccountIdentification1, SglocalAccountIdentification1Dict
from ..uklocal_account_identification1 import UklocalAccountIdentification1, UklocalAccountIdentification1Dict
from ..uslocal_account_identification1 import UslocalAccountIdentification1, UslocalAccountIdentification1Dict

BankAccountIdentification: TypeAlias = Annotated[
    (
        AulocalAccountIdentification1
        | BrlocalAccountIdentification1
        | CalocalAccountIdentification1
        | CzlocalAccountIdentification1
        | DklocalAccountIdentification1
        | HklocalAccountIdentification1
        | HulocalAccountIdentification1
        | IbanAccountIdentification1
        | NolocalAccountIdentification1
        | NzlocalAccountIdentification1
        | NumberAndBicAccountIdentification1
        | PllocalAccountIdentification1
        | SelocalAccountIdentification1
        | SglocalAccountIdentification1
        | UklocalAccountIdentification1
        | UslocalAccountIdentification1
    ),
    Field(discriminator="type_"),
]

BankAccountIdentificationDict: TypeAlias = (
    AulocalAccountIdentification1Dict
    | BrlocalAccountIdentification1Dict
    | CalocalAccountIdentification1Dict
    | CzlocalAccountIdentification1Dict
    | DklocalAccountIdentification1Dict
    | HklocalAccountIdentification1Dict
    | HulocalAccountIdentification1Dict
    | IbanAccountIdentification1Dict
    | NolocalAccountIdentification1Dict
    | NzlocalAccountIdentification1Dict
    | NumberAndBicAccountIdentification1Dict
    | PllocalAccountIdentification1Dict
    | SelocalAccountIdentification1Dict
    | SglocalAccountIdentification1Dict
    | UklocalAccountIdentification1Dict
    | UslocalAccountIdentification1Dict
)
