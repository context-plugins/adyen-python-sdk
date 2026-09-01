from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PhoneType(str, Enum):
    """The type of the phone number. >The following values are permitted: ``Landline``, ``Mobile``, ``SIP``, ``Fax``.,
    The type of the phone number. Possible values: **Landline**, **Mobile**, **SIP**, **Fax**."""

    FAX = "Fax"
    LANDLINE = "Landline"
    MOBILE = "Mobile"
    SIP = "SIP"

    __str__ = str.__str__


PhoneTypeOrStr: TypeAlias = Annotated[PhoneType | str, open_enum_validator(PhoneType)]
