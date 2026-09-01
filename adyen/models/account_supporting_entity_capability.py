from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.allowed_level import AllowedLevelOrStr
from .enums.requested_level import RequestedLevelOrStr
from .enums.verification_status import VerificationStatusOrStr


class AccountSupportingEntityCapability(SdkBaseModel):
    allowed: Optional[bool] = UNSET
    """Indicates whether the supporting entity capability is allowed. Adyen sets this to **true** if the verification is
    successful and the account holder is permitted to use the capability."""

    allowed_level: Optional[AllowedLevelOrStr] = Field(default=UNSET, alias="allowedLevel")
    """The capability level that is allowed for the account holder.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    enabled: Optional[bool] = UNSET
    """Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account
    holder."""

    id: Optional[str] = UNSET
    """The ID of the supporting entity."""

    requested: Optional[bool] = UNSET
    """Indicates whether the capability is requested. To check whether the account holder is permitted to use the
    capability, refer to the ``allowed`` field."""

    requested_level: Optional[RequestedLevelOrStr] = Field(default=UNSET, alias="requestedLevel")
    """The requested level of the capability. Some capabilities, such as those used in `card issuing
    <https://docs.adyen.com/issuing/add-capabilities#capability-levels>`__, have different levels. Levels increase the
    capability, but also require additional checks and increased monitoring.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    verification_status: Optional[VerificationStatusOrStr] = Field(default=UNSET, alias="verificationStatus")
    """The status of the verification checks for the supporting entity capability.

    Possible values:

    * **pending**: Adyen is running the verification.

    * **invalid**: The verification failed. Check if the ``errors`` array contains more information.

    * **valid**: The verification has been successfully completed.

    * **rejected**: Adyen has verified the information, but found reasons to not allow the capability."""


class AccountSupportingEntityCapabilityDict(TypedDict):
    allowed: NotRequired[bool]
    allowed_level: NotRequired[AllowedLevelOrStr]
    enabled: NotRequired[bool]
    id: NotRequired[str]
    requested: NotRequired[bool]
    requested_level: NotRequired[RequestedLevelOrStr]
    verification_status: NotRequired[VerificationStatusOrStr]
