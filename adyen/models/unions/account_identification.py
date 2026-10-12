from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..iban_account_identification2 import IbanAccountIdentification2, IbanAccountIdentification2Dict

AccountIdentification: TypeAlias = Annotated[
    Annotated[IbanAccountIdentification2, Tag("iban")], WireDiscriminator("type")
]

AccountIdentificationDict: TypeAlias = IbanAccountIdentification2Dict
