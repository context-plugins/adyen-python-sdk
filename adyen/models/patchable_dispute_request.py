from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.dispute_status import DisputeStatusOrStr
from .patchable_duplicate_info import PatchableDuplicateInfo, PatchableDuplicateInfoDict
from .patchable_fraud_info import PatchableFraudInfo, PatchableFraudInfoDict
from .patchable_not_delivered_info import PatchableNotDeliveredInfo, PatchableNotDeliveredInfoDict
from .patchable_other_info import PatchableOtherInfo, PatchableOtherInfoDict


class PatchableDisputeRequest(SdkBaseModel):
    duplicate_info: OptionalNullable[PatchableDuplicateInfo] = Field(default=UNSET, alias="duplicateInfo")
    """Additional information for raising a dispute of ``type`` **duplicate**. Required for disputes of ``type``
    **duplicate**."""

    fraud_info: OptionalNullable[PatchableFraudInfo] = Field(default=UNSET, alias="fraudInfo")
    """Additional information for raising a dispute of ``type`` **fraud**. Required for disputes of ``type``
    **fraud**."""

    not_delivered_info: OptionalNullable[PatchableNotDeliveredInfo] = Field(default=UNSET, alias="notDeliveredInfo")
    """Additional information for raising a dispute of ``type`` **notDelivered**. Required for disputes of ``type``
    **notDelivered**."""

    other_info: OptionalNullable[PatchableOtherInfo] = Field(default=UNSET, alias="otherInfo")
    """Additional information for raising a dispute of ``type`` **other**. Required for disputes of ``type`` **other**.

    **Note:** The **other** dispute ``type`` is currently in beta testing. Do not create or submit any disputes for this
    dispute ``type`` at this time."""

    status: OptionalNullable[DisputeStatusOrStr] = UNSET
    """The current status of the dispute.

    When you create a dispute, you can only set the ``status`` to **draft**. When you update a dispute, you can set the
    ``status`` to **submitted** or **closed**.

    Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**."""


class PatchableDisputeRequestDict(TypedDict):
    duplicate_info: NotRequired[PatchableDuplicateInfoDict | None]
    fraud_info: NotRequired[PatchableFraudInfoDict | None]
    not_delivered_info: NotRequired[PatchableNotDeliveredInfoDict | None]
    other_info: NotRequired[PatchableOtherInfoDict | None]
    status: NotRequired[DisputeStatusOrStr | None]
