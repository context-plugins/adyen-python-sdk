from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transaction_description_info1 import TransactionDescriptionInfo1, TransactionDescriptionInfo1Dict


class GenericPmWithTdiUpdateInfo10(SdkBaseModel):
    """Details to provide if ``type`` is **jcb**. For merchants operating in Japan, ``midNumber``, ``reuseMidNumber``,
    and ``serviceLevel`` fields are required. For merchants operating outside of Japan, these fields are not
    required."""

    transaction_description: Optional[TransactionDescriptionInfo1] = Field(
        default=UNSET, alias="transactionDescription"
    )
    """Information regarding the transaction description.
    > You cannot configure the transaction description in the test environment."""


class GenericPmWithTdiUpdateInfo10Dict(TypedDict):
    transaction_description: NotRequired[TransactionDescriptionInfo1 | TransactionDescriptionInfo1Dict]
