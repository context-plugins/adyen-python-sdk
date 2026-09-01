from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .installed_apks import InstalledApks, InstalledApksDict
from .terminal_assignment2 import TerminalAssignment2, TerminalAssignment2Dict
from .terminal_connectivity2 import TerminalConnectivity2, TerminalConnectivity2Dict


class Terminal(SdkBaseModel):
    assignment: Optional[TerminalAssignment2] = UNSET
    """Indicates the account level to which the terminal is assigned, the `assignment status
    <https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api>`__, and where the
    terminals is in the process of being reassigned to."""

    cloud_device_api_endpoint: Optional[str] = Field(default=UNSET, alias="cloudDeviceApiEndpoint")
    """The `regional base URL
    <https://docs.adyen.com/api-explorer/terminal-api/1/overview#endpoints-for-cloud-communications>`__ to use for
    sending Terminal API requests when using cloud communications."""

    connectivity: Optional[TerminalConnectivity2] = UNSET
    """Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The country code of the country where the terminal is located."""

    firmware_version: Optional[str] = Field(default=UNSET, alias="firmwareVersion")
    """The software release currently in use on the terminal."""

    id: Optional[str] = UNSET
    """The unique identifier of the terminal."""

    installed_apks: Optional[list[InstalledApks]] = Field(default=UNSET, alias="installedAPKs")
    """A list of Android apps installed on the terminal."""

    last_activity_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastActivityAt")
    """Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days
    ago."""

    last_transaction_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastTransactionAt")
    """Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14
    days ago."""

    model: Optional[str] = UNSET
    """The model name of the terminal."""

    restart_local_time: Optional[str] = Field(default=UNSET, alias="restartLocalTime")
    """The exact time of the terminal reboot, in the timezone of the terminal in **HH:mm** format."""

    serial_number: Optional[str] = Field(default=UNSET, alias="serialNumber")
    """The serial number of the terminal."""


class TerminalDict(TypedDict):
    assignment: NotRequired[TerminalAssignment2 | TerminalAssignment2Dict]
    cloud_device_api_endpoint: NotRequired[str]
    connectivity: NotRequired[TerminalConnectivity2 | TerminalConnectivity2Dict]
    country_code: NotRequired[str]
    firmware_version: NotRequired[str]
    id: NotRequired[str]
    installed_apks: NotRequired[list[InstalledApks | InstalledApksDict]]
    last_activity_at: NotRequired[RFC3339DateTime]
    last_transaction_at: NotRequired[RFC3339DateTime]
    model: NotRequired[str]
    restart_local_time: NotRequired[str]
    serial_number: NotRequired[str]
