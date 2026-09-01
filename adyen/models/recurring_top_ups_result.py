from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link import Link, LinkDict
from .recurring_top_up import RecurringTopUp, RecurringTopUpDict


class RecurringTopUpsResult(SdkBaseModel):
    link: Link
    recurring_top_ups: list[RecurringTopUp] = Field(alias="recurringTopUps")


class RecurringTopUpsResultDict(TypedDict):
    link: Link | LinkDict
    recurring_top_ups: list[RecurringTopUp | RecurringTopUpDict]
