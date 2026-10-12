from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .display_output2 import DisplayOutput2, DisplayOutput2Dict
from .enums.services_enabled import ServicesEnabledOrStr
from .enums.transaction_action1 import TransactionAction1OrStr


class EnableServiceRequest(SdkBaseModel):
    """It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and a
    possible invitation for the Customer to start the services. Content of the Enable Service Request message."""

    transaction_action: TransactionAction1OrStr = Field(alias="TransactionAction")
    """Action to realise on a transaction. In an ``EnableService`` request message:
      - Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.
      - Aborts a swipe-ahead transaction or started by a ``CardAcquisition``, and not followed by a service request from
            the Sale System to complete the transaction.
    Possible values:
    * **AbortTransaction**
    * **StartTransaction**"""

    services_enabled: Optional[list[ServicesEnabledOrStr]] = Field(default=UNSET, alias="ServicesEnabled")
    """Services which are enabled before the start-up of a transaction. Mandatory if ``TransactionAction`` is
    ``StartTransaction``, absent if not. Possible values:
    * **CardAcquisition**
    * **Loyalty**
    * **Payment**"""

    display_output: Optional[DisplayOutput2] = Field(default=UNSET, alias="DisplayOutput")
    """Information to display and the way to process the display."""


class EnableServiceRequestDict(TypedDict):
    transaction_action: TransactionAction1OrStr
    services_enabled: NotRequired[list[ServicesEnabledOrStr]]
    display_output: NotRequired[DisplayOutput2Dict]
