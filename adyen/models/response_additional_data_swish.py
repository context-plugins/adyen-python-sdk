from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataSwish(SdkBaseModel):
    swish_payer_alias: Optional[str] = Field(default=UNSET, alias="swish.payerAlias")
    """A Swish shopper's telephone number."""


class ResponseAdditionalDataSwishDict(TypedDict):
    swish_payer_alias: NotRequired[str]
