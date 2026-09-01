from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sca_exemption import ScaExemptionOrStr


class CreateScaInformation1(SdkBaseModel):
    """Information for the Strong Customer Authentication (SCA)"""

    exemption: Optional[ScaExemptionOrStr] = UNSET
    """The type of exemption for Strong Customer Authentication (SCA). Possible values:
    * **lowerLimit**: the newly created limit is lower than the existing limit.
    * **notRegulated**: the limit is created in a country, region, or industry where it is not mandated by law to use
        SCA.
    * **setByPlatform**: you set a limit for one of your user's balance accounts, or for your balance platform.
    * **initialLimit**: there are no existing transfer limits set on the balance account or balance platform.
    * **alreadyPerformed**: you are confident about your user's identity and do not need to verify this using SCA."""

    sca_on_approval: Optional[bool] = Field(default=UNSET, alias="scaOnApproval")
    """Indicates whether to initiate Strong Customer Authentication (SCA) later, during approval, or immediately after
    you submit this request. Possible values:
    * **true**: you can initiate SCA later, during approval, for all pending transfer limits.
    * **false** (default): you initiate SCA immediately after submitting the transfer limit request."""


class CreateScaInformation1Dict(TypedDict):
    exemption: NotRequired[ScaExemptionOrStr]
    sca_on_approval: NotRequired[bool]
