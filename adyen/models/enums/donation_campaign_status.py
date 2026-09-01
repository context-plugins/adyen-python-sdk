from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DonationCampaignStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ENDED = "ended"

    __str__ = str.__str__


DonationCampaignStatusOrStr: TypeAlias = Annotated[
    DonationCampaignStatus | str, open_enum_validator(DonationCampaignStatus)
]
