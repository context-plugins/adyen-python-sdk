from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CampaignStatusTransition(str, Enum):
    ACTIVATE = "activate"
    END = "end"

    __str__ = str.__str__


CampaignStatusTransitionOrStr: TypeAlias = Annotated[
    CampaignStatusTransition | str, open_enum_validator(CampaignStatusTransition)
]
