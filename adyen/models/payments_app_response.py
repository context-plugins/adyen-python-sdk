from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payments_app_dto import PaymentsAppDto, PaymentsAppDtoDict


class PaymentsAppResponse(SdkBaseModel):
    payments_apps: list[PaymentsAppDto] = Field(alias="paymentsApps")
    """List of Payments Apps."""


class PaymentsAppResponseDict(TypedDict):
    payments_apps: list[PaymentsAppDtoDict]
