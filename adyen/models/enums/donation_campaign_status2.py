from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationCampaignStatus2(str, Enum):
    """The current status of the donation campaign."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ENDED = "ended"

    __str__ = str.__str__


DonationCampaignStatus2OrStr: TypeAlias = Annotated[
    DonationCampaignStatus2 | str, open_enum_validator(DonationCampaignStatus2)
]
