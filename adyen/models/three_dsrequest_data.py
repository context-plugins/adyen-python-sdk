from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.challenge_window_size import ChallengeWindowSizeOrStr
from .enums.data_only import DataOnlyOrStr
from .enums.native_three_ds import NativeThreeDsOrStr
from .enums.three_dsversion import ThreeDsversionOrStr


class ThreeDsrequestData(SdkBaseModel):
    challenge_window_size: Optional[ChallengeWindowSizeOrStr] = Field(default=UNSET, alias="challengeWindowSize")
    """Dimensions of the 3DS2 challenge window to be displayed to the cardholder.

    Possible values:

    * **01** - size of 250x400
    * **02** - size of 390x400
    * **03** - size of 500x600
    * **04** - size of 600x400
    * **05** - Fullscreen"""

    data_only: Optional[DataOnlyOrStr] = Field(default=UNSET, alias="dataOnly")
    """Required to trigger the `data-only flow <https://docs.adyen.com/online-payments/3d-secure/data-only/>`__. When
    set to **true**, forces the 3D Secure 2 data-only flow for all transactions where it is possible."""

    native_three_ds: Optional[NativeThreeDsOrStr] = Field(default=UNSET, alias="nativeThreeDS")
    """Indicates if `native 3D Secure authentication <https://docs.adyen.com/online-payments/3d-secure/native-3ds2>`__
    should be triggered when available. Adyen can still select to fallback to the redirect flow to optimize
    authorization rates and improve the shopper's experience.

    Possible values:
    * **preferred**: Use native 3D Secure authentication when available.
    * **disabled**: Use the redirect 3D Secure authentication flow."""

    three_ds_version: Optional[ThreeDsversionOrStr] = Field(default=UNSET, alias="threeDSVersion")
    """The version of 3D Secure to use.

    Possible values:

    * **2.1.0**
    * **2.2.0**"""


class ThreeDsrequestDataDict(TypedDict):
    challenge_window_size: NotRequired[ChallengeWindowSizeOrStr]
    data_only: NotRequired[DataOnlyOrStr]
    native_three_ds: NotRequired[NativeThreeDsOrStr]
    three_ds_version: NotRequired[ThreeDsversionOrStr]
