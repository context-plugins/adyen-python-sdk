from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataOpi(SdkBaseModel):
    opi_trans_token: Optional[str] = Field(default=UNSET, alias="opi.transToken")
    """Returned in the response if you included ``opi.includeTransToken: true`` in an ecommerce payment request. This
    contains an Oracle Payment Interface token that you can store in your Oracle Opera database to identify tokenized
    ecommerce transactions. For more information and required settings, see `Oracle Opera
    <https://docs.adyen.com/plugins/oracle-opera#opi-token-ecommerce>`__."""


class ResponseAdditionalDataOpiDict(TypedDict):
    opi_trans_token: NotRequired[str]
