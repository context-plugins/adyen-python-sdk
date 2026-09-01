from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DuplicateInfo1(SdkBaseModel):
    """Additional information for raising a dispute of ``type`` **duplicate**. Required for disputes of ``type``
    **duplicate**."""

    duplicate_transaction_id: str = Field(alias="duplicateTransactionId")
    """The transaction id associated with the duplicate charge for which you are disputing. The disputed transaction
    must be in the same amount as the duplicate transaction."""

    same_card: bool = Field(alias="sameCard")
    """The duplicate charge was made on the same card. Possible values: **true**, **false**."""

    same_issuer: Optional[bool] = Field(default=UNSET, alias="sameIssuer")
    """The issuer associated with each charge is the same. Possible values: **true**, **false**."""


class DuplicateInfo1Dict(TypedDict):
    duplicate_transaction_id: str
    same_card: bool
    same_issuer: NotRequired[bool]
