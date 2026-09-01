from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NativeThreeDs(str, Enum):
    """Indicates if `native 3D Secure authentication <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__
    should be triggered when available. Adyen can still select to fallback to the redirect flow to optimize
    authorization rates and improve the shopper's experience.

    Possible values:
    * **preferred**: Use native 3D Secure authentication when available.
    * **disabled**: Use the redirect 3D Secure authentication flow."""

    PREFERRED = "preferred"
    DISABLED = "disabled"

    __str__ = str.__str__


NativeThreeDsOrStr: TypeAlias = Annotated[NativeThreeDs | str, open_enum_validator(NativeThreeDs)]
