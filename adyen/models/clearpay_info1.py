from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClearpayInfo1(SdkBaseModel):
    """Details to provide if ``type`` is **clearpay**."""

    support_url: str = Field(alias="supportUrl")
    """Support Url"""


class ClearpayInfo1Dict(TypedDict):
    support_url: str
