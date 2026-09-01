from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .app_identifier_info1 import AppIdentifierInfo1, AppIdentifierInfo1Dict


class PaymentMethodUpiapps(SdkBaseModel):
    app_identifier_info: Optional[AppIdentifierInfo1] = Field(default=UNSET, alias="appIdentifierInfo")
    """The app identifier information containing iOS scheme and Android package ID."""

    id: str
    """The unique identifier of this app, to submit in requests to /payments."""

    name: str
    """A localized name of the app."""


class PaymentMethodUpiappsDict(TypedDict):
    app_identifier_info: NotRequired[AppIdentifierInfo1 | AppIdentifierInfo1Dict]
    id: str
    name: str
