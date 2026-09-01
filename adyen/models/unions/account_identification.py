from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..iban_account_identification2 import IbanAccountIdentification2, IbanAccountIdentification2Dict

AccountIdentification: TypeAlias = Annotated[IbanAccountIdentification2, Field(discriminator="type_")]

AccountIdentificationDict: TypeAlias = IbanAccountIdentification2Dict
