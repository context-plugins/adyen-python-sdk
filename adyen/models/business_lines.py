from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_line import BusinessLine, BusinessLineDict


class BusinessLines(SdkBaseModel):
    business_lines: list[BusinessLine] = Field(alias="businessLines")
    """List of business lines."""


class BusinessLinesDict(TypedDict):
    business_lines: list[BusinessLine | BusinessLineDict]
