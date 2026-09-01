from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_supporting_entity_capability import (
    AccountSupportingEntityCapability,
    AccountSupportingEntityCapabilityDict,
)
from .capability_problem import CapabilityProblem, CapabilityProblemDict
from .capability_settings1 import CapabilitySettings1, CapabilitySettings1Dict
from .capability_settings3 import CapabilitySettings3, CapabilitySettings3Dict
from .enums.allowed_level import AllowedLevelOrStr
from .enums.requested_level import RequestedLevelOrStr
from .enums.verification_status import VerificationStatusOrStr


class AccountHolderCapability(SdkBaseModel):
    allowed: Optional[bool] = UNSET
    """Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful and
    the account holder is permitted to use the capability."""

    allowed_level: Optional[AllowedLevelOrStr] = Field(default=UNSET, alias="allowedLevel")
    """The capability level that is allowed for the account holder.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    allowed_settings: Optional[CapabilitySettings3] = Field(default=UNSET, alias="allowedSettings")
    """A JSON object containing the settings that are allowed for the account holder."""

    enabled: Optional[bool] = UNSET
    """Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account
    holder."""

    problems: Optional[list[CapabilityProblem]] = UNSET
    """Contains verification errors and the actions that you can take to resolve them."""

    requested: Optional[bool] = UNSET
    """Indicates whether the capability is requested. To check whether the account holder is permitted to use the
    capability, refer to the ``allowed`` field."""

    requested_level: Optional[RequestedLevelOrStr] = Field(default=UNSET, alias="requestedLevel")
    """The requested level of the capability. Some capabilities, such as those used in `card issuing
    <https://docs.adyen.com/issuing/add-capabilities#capability-levels>`__, have different levels. Levels increase the
    capability, but also require additional checks and increased monitoring.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    requested_settings: Optional[CapabilitySettings1] = Field(default=UNSET, alias="requestedSettings")
    """A JSON object containing the settings that were requested for the account holder."""

    transfer_instruments: Optional[list[AccountSupportingEntityCapability]] = Field(
        default=UNSET, alias="transferInstruments"
    )
    """Contains the status of the transfer instruments associated with this capability."""

    verification_status: Optional[VerificationStatusOrStr] = Field(default=UNSET, alias="verificationStatus")
    """The status of the verification checks for the capability.

    Possible values:

    * **pending**: Adyen is running the verification.

    * **invalid**: The verification failed. Check if the ``errors`` array contains more information.

    * **valid**: The verification has been successfully completed.

    * **rejected**: Adyen has verified the information, but found reasons to not allow the capability."""


class AccountHolderCapabilityDict(TypedDict):
    allowed: NotRequired[bool]
    allowed_level: NotRequired[AllowedLevelOrStr]
    allowed_settings: NotRequired[CapabilitySettings3 | CapabilitySettings3Dict]
    enabled: NotRequired[bool]
    problems: NotRequired[list[CapabilityProblem | CapabilityProblemDict]]
    requested: NotRequired[bool]
    requested_level: NotRequired[RequestedLevelOrStr]
    requested_settings: NotRequired[CapabilitySettings1 | CapabilitySettings1Dict]
    transfer_instruments: NotRequired[list[AccountSupportingEntityCapability | AccountSupportingEntityCapabilityDict]]
    verification_status: NotRequired[VerificationStatusOrStr]
