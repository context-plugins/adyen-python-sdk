from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.namespace import NamespaceOrStr


class NetworkReason2(SdkBaseModel):
    """Contains information that explains why the transfer was rejected or returned by the network."""

    code: Optional[str] = UNSET
    """The reason code provided by the network."""

    description: Optional[str] = UNSET
    """The description of the reason code."""

    namespace: Optional[NamespaceOrStr] = UNSET
    """The namespace that corresponds to the reason code.

    Possible values:
    * **ukFpsRejectionCode**
    * **ukFpsReturnReasonCode**
    * **usAchReturnReasonCode**
    * **iso8583ResponseCode**"""


class NetworkReason2Dict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    namespace: NotRequired[NamespaceOrStr]
