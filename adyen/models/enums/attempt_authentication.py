from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AttemptAuthentication(str, Enum):
    """Indicates when 3D Secure authentication should be attempted. This overrides all other rules, including `Dynamic
    3D Secure settings <https://docs.adyen.com/risk-management/dynamic-3d-secure>`__.

    Possible values:

    * **always**: Perform 3D Secure authentication.
    * **never**: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require
        authentication, the transaction gets declined."""

    ALWAYS = "always"
    NEVER = "never"

    __str__ = str.__str__


AttemptAuthenticationOrStr: TypeAlias = Annotated[
    AttemptAuthentication | str, open_enum_validator(AttemptAuthentication)
]
