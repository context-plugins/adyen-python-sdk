from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .summary import Summary, SummaryDict


class TaxFormSummaryResponse(SdkBaseModel):
    data: list[Summary]
    """A list of tax form summaries, where each summary consists of the legal entity and the tax years in which the
    legal entity has a tax form."""


class TaxFormSummaryResponseDict(TypedDict):
    data: list[Summary | SummaryDict]
