from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.status6 import Status6OrStr
from .patchable_top_up_amount2 import PatchableTopUpAmount2, PatchableTopUpAmount2Dict
from .patchable_trigger2 import PatchableTrigger2, PatchableTrigger2Dict


class PatchableCreateRecurringTopUp(SdkBaseModel):
    description: Optional[str] = UNSET
    """Your description for the recurring top-up.

    Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters."""

    reference_for_beneficiary: OptionalNullable[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer,
    so you can use it to track statuses for both parties involved in the funds movement.

     Supported characters: **a-z**, **A-Z**, **0-9**."""

    status: OptionalNullable[Status6OrStr] = UNSET
    """The status of the recurring top-up. If not provided, by default, this is set to **active**.

    Possible values:

     * **active**: the top up is enabled and funds will be pulled in.

     * **inactive**: the top up is disabled and cannot be triggered."""

    top_up_amount: Optional[PatchableTopUpAmount2] = Field(default=UNSET, alias="topUpAmount")
    """The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount
    or a target amount."""

    trigger: Optional[PatchableTrigger2] = UNSET
    """The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold."""


class PatchableCreateRecurringTopUpDict(TypedDict):
    description: NotRequired[str]
    reference_for_beneficiary: NotRequired[str | None]
    status: NotRequired[Status6OrStr | None]
    top_up_amount: NotRequired[PatchableTopUpAmount2 | PatchableTopUpAmount2Dict]
    trigger: NotRequired[PatchableTrigger2 | PatchableTrigger2Dict]
