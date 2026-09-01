from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .test_output import TestOutput, TestOutputDict


class TestWebhookResponse(SdkBaseModel):
    data: Optional[list[TestOutput]] = UNSET
    """List with test results. Each test webhook we send has a list element with the result."""


class TestWebhookResponseDict(TypedDict):
    data: NotRequired[list[TestOutput | TestOutputDict]]
