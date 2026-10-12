from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.device3 import Device3OrStr
from .enums.info_qualify3 import InfoQualify3OrStr
from .response11 import Response11, Response11Dict


class OutputResult1(SdkBaseModel):
    """Information related to the result the output (display, print, input). If DisplayOutput present in the request."""

    device: Device3OrStr = Field(alias="Device")
    """Logical device located on a Sale Terminal or a POI Terminal, in term of class of information to output (display,
    print or store), or input (keyboard) for the Cashier or the Customer. Copy. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    info_qualify: InfoQualify3OrStr = Field(alias="InfoQualify")
    """Qualification of the information to sent to an output logical device, to display or print to the Cashier or the
    Customer. Copy. Possible values:
    * **CustomerAssistance**
    * **Display**
    * **Document**
    * **Error**
    * **Input**
    * **POIReplication**
    * **Receipt**
    * **Sound**
    * **Status**
    * **Voucher**"""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""


class OutputResult1Dict(TypedDict):
    device: Device3OrStr
    info_qualify: InfoQualify3OrStr
    response: Response11Dict
