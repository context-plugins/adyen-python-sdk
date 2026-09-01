from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..uklocal_mandate_account_identification import (
    UklocalMandateAccountIdentification,
    UklocalMandateAccountIdentificationDict,
)

MandateAccountIdentification: TypeAlias = Annotated[UklocalMandateAccountIdentification, Field(discriminator="type_")]

MandateAccountIdentificationDict: TypeAlias = UklocalMandateAccountIdentificationDict
