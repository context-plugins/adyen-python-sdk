from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ThirdPartyTokenRedundancyInfo(SdkBaseModel):
    request_parameters: Optional[dict[str, str]] = Field(default=UNSET, alias="requestParameters")
    """Request-specific parameter values to populate the template placeholders. Each key must match a placeholder
    defined in the template referenced by ``requestTemplateCode``."""

    request_template_code: str = Field(alias="requestTemplateCode")
    """Identifier for the third-party token request template configured in your Adyen account. This template defines the
    structure and endpoint for token requests."""


class ThirdPartyTokenRedundancyInfoDict(TypedDict):
    request_parameters: NotRequired[dict[str, str]]
    request_template_code: str
