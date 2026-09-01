from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class GetPciQuestionnaireResponse(SdkBaseModel):
    content: Optional[str] = UNSET
    """The generated questionnaire in a base64 encoded format."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date the questionnaire was created, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00"""

    id: Optional[str] = UNSET
    """The unique identifier of the signed questionnaire."""

    valid_until: Optional[RFC3339DateTime] = Field(default=UNSET, alias="validUntil")
    """The expiration date of the questionnaire, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00"""


class GetPciQuestionnaireResponseDict(TypedDict):
    content: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    valid_until: NotRequired[RFC3339DateTime]
