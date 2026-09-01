from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataOpi(SdkBaseModel):
    opi_include_trans_token: Optional[str] = Field(default=UNSET, alias="opi.includeTransToken")
    """Optional boolean indicator. Set to **true** if you want an ecommerce transaction to return an ``opi.transToken``
    as additional data in the response.

    You can store this Oracle Payment Interface token in your Oracle Opera database. For more information and required
    settings, see `Oracle Opera <https://docs.adyen.com/plugins/oracle-opera#opi-token-ecommerce>`__."""


class AdditionalDataOpiDict(TypedDict):
    opi_include_trans_token: NotRequired[str]
