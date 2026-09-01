from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..force_reboot_details import ForceRebootDetails, ForceRebootDetailsDict
from ..install_android_app_details import InstallAndroidAppDetails, InstallAndroidAppDetailsDict
from ..install_android_certificate_details import InstallAndroidCertificateDetails, InstallAndroidCertificateDetailsDict
from ..release_update_details import ReleaseUpdateDetails, ReleaseUpdateDetailsDict
from ..uninstall_android_app_details import UninstallAndroidAppDetails, UninstallAndroidAppDetailsDict
from ..uninstall_android_certificate_details import (
    UninstallAndroidCertificateDetails,
    UninstallAndroidCertificateDetailsDict,
)

ActionDetails: TypeAlias = Annotated[
    (
        ForceRebootDetails
        | InstallAndroidAppDetails
        | InstallAndroidCertificateDetails
        | ReleaseUpdateDetails
        | UninstallAndroidAppDetails
        | UninstallAndroidCertificateDetails
    ),
    Field(discriminator="type_"),
]
"""Information about the action to take."""

ActionDetailsDict: TypeAlias = (
    ForceRebootDetailsDict
    | InstallAndroidAppDetailsDict
    | InstallAndroidCertificateDetailsDict
    | ReleaseUpdateDetailsDict
    | UninstallAndroidAppDetailsDict
    | UninstallAndroidCertificateDetailsDict
)
