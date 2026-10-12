from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .android_app_error import AndroidAppError, AndroidAppErrorDict
from .enums.status7 import Status7OrStr


class AndroidApp(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description that was provided when uploading the app. The description is not shown on the terminal."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """The error code of the Android app with the ``status`` of either **error** or **invalid**."""

    errors: Optional[list[AndroidAppError]] = UNSET
    """The list of errors of the Android app."""

    id: str
    """The unique identifier of the app."""

    label: Optional[str] = UNSET
    """The app name that is shown on the terminal."""

    package_name: Optional[str] = Field(default=UNSET, alias="packageName")
    """The package name that uniquely identifies the Android app."""

    status: Status7OrStr
    """The status of the app. Possible values:
    * ``processing``: the app is being signed and converted to a format that the terminal can handle.
    * ``error``: something went wrong. Check that the app matches the `requirements
        <https://docs.adyen.com/point-of-sale/android-terminals/app-requirements>`__.
    * ``invalid``: there is something wrong with the APK file of the app.
    * ``ready``: the app has been signed and converted.
    * ``archived``: the app is no longer available."""

    version_code: Optional[int] = Field(default=UNSET, alias="versionCode")
    """The version number of the app."""

    version_name: Optional[str] = Field(default=UNSET, alias="versionName")
    """The app version number that is shown on the terminal."""


class AndroidAppDict(TypedDict):
    description: NotRequired[str]
    error_code: NotRequired[str]
    errors: NotRequired[list[AndroidAppErrorDict]]
    id: str
    label: NotRequired[str]
    package_name: NotRequired[str]
    status: Status7OrStr
    version_code: NotRequired[int]
    version_name: NotRequired[str]
