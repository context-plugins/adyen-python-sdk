from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type132(str, Enum):
    """Type of identity data. For individuals, the following types are supported. See our `onboarding guide
    <https://docs.adyen.com/platforms/onboard-users/onboarding-steps/?onboarding_type=custom>`__ for other supported
    countries.

    - Australia: **driversLicense**, **passport**

    - Hong Kong: **driversLicense**, **nationalIdNumber**, **passport**

    - New Zealand: **driversLicense**, **passport**

    - Singapore: **driversLicense**, **nationalIdNumber**, **passport**

    - All other supported countries: **nationalIdNumber**"""

    NATIONAL_ID_NUMBER = "nationalIdNumber"
    PASSPORT = "passport"
    DRIVERS_LICENSE = "driversLicense"
    IDENTITY_CARD = "identityCard"

    __str__ = str.__str__


Type132OrStr: TypeAlias = Annotated[Type132 | str, open_enum_validator(Type132)]
