from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..uklocal_mandate_account_identification import (
    UklocalMandateAccountIdentification,
    UklocalMandateAccountIdentificationDict,
)

MandateAccountIdentification: TypeAlias = Annotated[
    Annotated[UklocalMandateAccountIdentification, Tag("ukLocal")], WireDiscriminator("type")
]

MandateAccountIdentificationDict: TypeAlias = UklocalMandateAccountIdentificationDict
