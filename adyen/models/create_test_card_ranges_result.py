from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .test_card_range_creation_result import TestCardRangeCreationResult, TestCardRangeCreationResultDict


class CreateTestCardRangesResult(SdkBaseModel):
    range_creation_results: list[TestCardRangeCreationResult] = Field(alias="rangeCreationResults")
    """The results of the test card creation."""


class CreateTestCardRangesResultDict(TypedDict):
    range_creation_results: list[TestCardRangeCreationResultDict]
