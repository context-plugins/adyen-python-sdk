from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links21 import Links21, Links21Dict
from .transaction import Transaction, TransactionDict


class TransactionSearchResponse(SdkBaseModel):
    links: Optional[Links21] = Field(default=UNSET, alias="_links")
    """Contains links to the next and previous page whenever applicable."""

    data: Optional[list[Transaction]] = UNSET
    """Contains the transactions that match the query parameters."""


class TransactionSearchResponseDict(TypedDict):
    links: NotRequired[Links21 | Links21Dict]
    data: NotRequired[list[Transaction | TransactionDict]]
