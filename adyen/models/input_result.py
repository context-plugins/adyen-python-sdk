from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.device4 import Device4OrStr
from .enums.info_qualify2 import InfoQualify2OrStr
from .input2 import Input2, Input2Dict
from .response1 import Response1, Response1Dict


class InputResult(SdkBaseModel):
    device: Device4OrStr = Field(alias="Device")
    """Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display,
    print or store), or input (keyboard) for the Cashier or the Customer. Possible values:
    * **CashierDisplay**
    * **CashierInput**
    * **CustomerDisplay**
    * **CustomerInput**"""

    info_qualify: InfoQualify2OrStr = Field(alias="InfoQualify")
    """Qualification of the information to send to an output logical device, to display or print to the Cashier or the
    Customer. Possible values:
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

    response: Response1 = Field(alias="Response")
    """Result of a message request processing. If Result is Success, ``ErrorCondition`` is absent or not used in the
    processing of the message. In the other cases, the ``ErrorCondition`` has to be present and can refine the
    processing of the message response. ``AdditionalResponse`` gives more information about the success or the failure
    of the message request processing, for logging without real time involvements."""

    input: Optional[Input2] = Field(default=UNSET, alias="Input")
    """Data entered by the user, related to the input command."""


class InputResultDict(TypedDict):
    device: Device4OrStr
    info_qualify: InfoQualify2OrStr
    response: Response1Dict
    input: NotRequired[Input2Dict]
