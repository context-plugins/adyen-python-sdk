from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.form_factor import FormFactorOrStr


class BankAccountModel1(SdkBaseModel):
    """Contains the business account details."""

    form_factor: OptionalNullable[FormFactorOrStr] = Field(default=UNSET, alias="formFactor")
    """Business accounts with a ``formFactor`` value of **physical** are business accounts issued under the central bank
    of that country. The default value is **physical** for NL, US, and UK business accounts.

    Adyen creates a local IBAN for business accounts when the ``formFactor`` value is set to **virtual**. The local
    IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through
    the central bank of NL."""


class BankAccountModel1Dict(TypedDict):
    form_factor: NotRequired[FormFactorOrStr | None]
