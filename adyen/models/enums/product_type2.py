from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType2(str, Enum):
    """The type of component.

    For `Onboarding components <https://docs.adyen.com/platforms/onboard-users/components>`__, set this to
    **onboarding**.

    For `Platform Experience components <https://docs.adyen.com/platforms/build-user-dashboards>`__, set this to
    **platform**."""

    ONBOARDING = "onboarding"
    PLATFORM = "platform"
    BANK = "bank"

    __str__ = str.__str__


ProductType2OrStr: TypeAlias = Annotated[ProductType2 | str, open_enum_validator(ProductType2)]
