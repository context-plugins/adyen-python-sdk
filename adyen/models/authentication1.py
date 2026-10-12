from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .phone11 import Phone11, Phone11Dict


class Authentication1(SdkBaseModel):
    """Contains the card user's password and mobile phone number. This is required when you issue cards that can be used
    to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to `3D Secure and
    digital wallets <https://docs.adyen.com/issuing/3d-secure-and-wallets>`__ for more information."""

    email: Optional[str] = UNSET
    """The email address where the one-time password (OTP) is sent."""

    password: Optional[str] = UNSET
    """The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and
    must only contain the following supported characters.

    * Characters between **a-z**, **A-Z**, and **0-9**

    * Special characters: **äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúó**"""

    phone: Optional[Phone11] = UNSET
    """The phone number where the one-time password (OTP) is sent.

    This object must have:

    * A ``type`` set to **mobile**.

    * A ``number`` with a valid country code.

    * A ``number`` with more than 4 digits, excluding the country code.

    >Make sure to verify that the card user owns the phone number."""


class Authentication1Dict(TypedDict):
    email: NotRequired[str]
    password: NotRequired[str]
    phone: NotRequired[Phone11Dict]
