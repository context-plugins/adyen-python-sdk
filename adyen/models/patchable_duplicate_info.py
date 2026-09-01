from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PatchableDuplicateInfo(SdkBaseModel):
    duplicate_transaction_id: Optional[str] = Field(default=UNSET, alias="duplicateTransactionId")
    """The transaction id associated with the duplicate charge for which you are disputing. The disputed transaction
    must be in the same amount as the duplicate transaction."""

    same_card: Optional[bool] = Field(default=UNSET, alias="sameCard")
    """The duplicate charge was made on the same card. Possible values: **true**, **false**."""

    same_issuer: OptionalNullable[bool] = Field(default=UNSET, alias="sameIssuer")
    """The issuer associated with each charge is the same. Possible values: **true**, **false**."""


class PatchableDuplicateInfoDict(TypedDict):
    duplicate_transaction_id: NotRequired[str]
    same_card: NotRequired[bool]
    same_issuer: NotRequired[bool | None]
