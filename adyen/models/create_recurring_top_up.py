from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status6 import Status6OrStr
from .top_up_amount1 import TopUpAmount1, TopUpAmount1Dict
from .top_up_counterparty1 import TopUpCounterparty1, TopUpCounterparty1Dict
from .trigger1 import Trigger1, Trigger1Dict


class CreateRecurringTopUp(SdkBaseModel):
    counterparty: TopUpCounterparty1
    """The details about the counterparty that is funding the top-up."""

    description: str
    """Your description for the recurring top-up.

    Maximum length is 140 characters. If you set a longer description, it will be cut off at 140 characters."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer,
    so you can use it to track statuses for both parties involved in the funds movement.

     Supported characters: **a-z**, **A-Z**, **0-9**."""

    status: Optional[Status6OrStr] = UNSET
    """The status of the recurring top-up. If not provided, by default, this is set to **active**.

    Possible values:

     * **active**: the top up is enabled and funds will be pulled in.

     * **inactive**: the top up is disabled and cannot be triggered."""

    top_up_amount: TopUpAmount1 = Field(alias="topUpAmount")
    """The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount
    or a target amount."""

    trigger: Trigger1
    """The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold."""


class CreateRecurringTopUpDict(TypedDict):
    counterparty: TopUpCounterparty1 | TopUpCounterparty1Dict
    description: str
    reference_for_beneficiary: NotRequired[str]
    status: NotRequired[Status6OrStr]
    top_up_amount: TopUpAmount1 | TopUpAmount1Dict
    trigger: Trigger1 | Trigger1Dict
