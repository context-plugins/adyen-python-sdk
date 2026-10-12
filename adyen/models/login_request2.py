from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.customer_order_req import CustomerOrderReqOrStr
from .enums.token_requested_type1 import TokenRequestedType1OrStr
from .sale_software1 import SaleSoftware1, SaleSoftware1Dict
from .sale_terminal_data2 import SaleTerminalData2, SaleTerminalData2Dict


class LoginRequest2(SdkBaseModel):
    """Content of the Login Request message."""

    date_time: RFC3339DateTime = Field(alias="DateTime")
    """Date and Time. In the Login request message, the Sale System gives its date and time to the POI System. In the
    Login response, the POI System gives its date and time to the Sale System."""

    sale_software: SaleSoftware1 = Field(alias="SaleSoftware")
    """Information related to the software of the Sale System which manages the Sale to POI protocol."""

    sale_terminal_data: Optional[SaleTerminalData2] = Field(default=UNSET, alias="SaleTerminalData")
    """Information related to the software and hardware feature of the Sale Terminal. Present if the login involve a
    Sale Terminal."""

    training_mode_flag: bool = Field(default=False, alias="TrainingModeFlag")
    """Training mode. This flag indicates to the POI that the entire session will be not used to make real transaction,
    but is used for test of system or operator training."""

    operator_language: str = Field(alias="OperatorLanguage")
    """Language of the Cashier or Operator. Default value for Device type displays."""

    operator_id: Optional[str] = Field(default=UNSET, alias="OperatorID")
    """Identification of the Cashier or Operator. Four conditions to send it:
    * The Sale System wants the POI to log it in the transaction log.
    * Because of reconciliation with total on OperatorID.
    * Because the POI needs it.
    * Acquirer or issuer need it."""

    shift_number: Optional[str] = Field(default=UNSET, alias="ShiftNumber")
    """Shift number. Same as OperatorID."""

    token_requested_type: Optional[TokenRequestedType1OrStr] = Field(default=UNSET, alias="TokenRequestedType")
    """Type of token replacing the PAN of a payment card to identify the payment
     mean of the customer. It allows, for a merchant, to use a token for a transaction
     only or for a longer period.
    Possible values:
    * **Customer**
    * **Transaction**"""

    customer_order_req: Optional[list[CustomerOrderReqOrStr]] = Field(default=UNSET, alias="CustomerOrderReq")
    """List of customer order open, closed or both to be sent in the response messages. Possible values:
    * **Both**
    * **Closed**
    * **Open**"""

    poi_serial_number: Optional[str] = Field(default=UNSET, alias="POISerialNumber")
    """Serial number of a POI Terminal. If the login involve a POI Terminal and not the first Login to the POI
    System."""


class LoginRequest2Dict(TypedDict):
    date_time: RFC3339DateTime
    sale_software: SaleSoftware1Dict
    sale_terminal_data: NotRequired[SaleTerminalData2Dict]
    training_mode_flag: NotRequired[bool]
    operator_language: str
    operator_id: NotRequired[str]
    shift_number: NotRequired[str]
    token_requested_type: NotRequired[TokenRequestedType1OrStr]
    customer_order_req: NotRequired[list[CustomerOrderReqOrStr]]
    poi_serial_number: NotRequired[str]
