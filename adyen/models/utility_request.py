from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UtilityRequest(SdkBaseModel):
    origin_domains: list[str] = Field(alias="originDomains")
    """The list of origin domains, for which origin keys are requested."""


class UtilityRequestDict(TypedDict):
    origin_domains: list[str]
