from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportingEntityCapability(SdkBaseModel):
    allowed: Optional[bool] = UNSET
    """Indicates whether the capability is allowed for the supporting entity.

    If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity
    has other supporting entities that failed verification.

    **You can use the allowed supporting entity** regardless of the verification status of other supporting entities."""

    id: Optional[str] = UNSET
    """Supporting entity reference"""

    requested: Optional[bool] = UNSET
    """Indicates whether the supporting entity capability is requested."""

    verification_status: Optional[str] = Field(default=UNSET, alias="verificationStatus")
    """The status of the verification checks for the capability of the supporting entity.

    Possible values:

    * **pending**: Adyen is running the verification.

    * **invalid**: The verification failed. Check if the ``errors`` array contains more information.

    * **valid**: The verification has been successfully completed.

    * **rejected**: Adyen has verified the information, but found reasons to not allow the capability."""


class SupportingEntityCapabilityDict(TypedDict):
    allowed: NotRequired[bool]
    id: NotRequired[str]
    requested: NotRequired[bool]
    verification_status: NotRequired[str]
