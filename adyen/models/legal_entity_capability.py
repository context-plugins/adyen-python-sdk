from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_settings11 import CapabilitySettings11, CapabilitySettings11Dict
from .capability_settings21 import CapabilitySettings21, CapabilitySettings21Dict
from .enums.allowed_level import AllowedLevelOrStr
from .supporting_entity_capability import SupportingEntityCapability, SupportingEntityCapabilityDict


class LegalEntityCapability(SdkBaseModel):
    allowed: Optional[bool] = UNSET
    """Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful."""

    allowed_level: Optional[AllowedLevelOrStr] = Field(default=UNSET, alias="allowedLevel")
    """The capability level that is allowed for the legal entity.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    allowed_settings: Optional[CapabilitySettings11] = Field(default=UNSET, alias="allowedSettings")
    """The settings that are allowed for the legal entity."""

    requested: Optional[bool] = UNSET
    """Indicates whether the capability is requested. To check whether the legal entity is permitted to use the
    capability, refer to the ``allowed`` field."""

    requested_level: Optional[AllowedLevelOrStr] = Field(default=UNSET, alias="requestedLevel")
    """The requested level of the capability. Some capabilities, such as those used in `card issuing
    <https://docs.adyen.com/issuing/add-capabilities#capability-levels>`__, have different levels. Levels increase the
    capability, but also require additional checks and increased monitoring.

    Possible values: **notApplicable**, **low**, **medium**, **high**."""

    requested_settings: Optional[CapabilitySettings21] = Field(default=UNSET, alias="requestedSettings")
    """The settings that are requested for the legal entity."""

    transfer_instruments: Optional[list[SupportingEntityCapability]] = Field(default=UNSET, alias="transferInstruments")
    """The capability status of transfer instruments associated with the legal entity."""

    verification_status: Optional[str] = Field(default=UNSET, alias="verificationStatus")
    """The status of the verification checks for the capability.

    Possible values:

    * **pending**: Adyen is running the verification.

    * **invalid**: The verification failed. Check if the ``errors`` array contains more information.

    * **valid**: The verification has been successfully completed.

    * **rejected**: Adyen has verified the information, but found reasons to not allow the capability."""


class LegalEntityCapabilityDict(TypedDict):
    allowed: NotRequired[bool]
    allowed_level: NotRequired[AllowedLevelOrStr]
    allowed_settings: NotRequired[CapabilitySettings11Dict]
    requested: NotRequired[bool]
    requested_level: NotRequired[AllowedLevelOrStr]
    requested_settings: NotRequired[CapabilitySettings21Dict]
    transfer_instruments: NotRequired[list[SupportingEntityCapabilityDict]]
    verification_status: NotRequired[str]
