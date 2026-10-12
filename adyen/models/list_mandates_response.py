from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link2 import Link2, Link2Dict
from .mandate1 import Mandate1, Mandate1Dict


class ListMandatesResponse(SdkBaseModel):
    link: Link2
    """Contains links to the next and previous page whenever applicable."""

    mandates: list[Mandate1]
    """Contains a list of the mandates."""


class ListMandatesResponseDict(TypedDict):
    link: Link2Dict
    mandates: list[Mandate1Dict]
