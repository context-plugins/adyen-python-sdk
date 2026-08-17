
# Login Request 2

Content of the Login Request message.

## Structure

`LoginRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | `datetime` | Required | Date and Time. In the Login request message, the Sale System gives its date and time to the POI System. In the Login response, the POI System gives its date and time to the Sale System. |
| `sale_software` | [`SaleSoftware1`](../../doc/models/sale-software-1.md) | Required | Information related to the software of the Sale System which manages the Sale to POI protocol. |
| `sale_terminal_data` | [`SaleTerminalData2`](../../doc/models/sale-terminal-data-2.md) | Optional | Information related to the software and hardware feature of the Sale Terminal.<br>Present if the login involve a Sale Terminal. |
| `training_mode_flag` | `bool` | Optional | Training mode.<br>This flag indicates to the POI that the entire session will be not used to make real transaction, but is used for test of system or operator training.<br><br>**Default**: `False` |
| `operator_language` | `str` | Required | Language of the Cashier or Operator.<br>Default value for Device type displays.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br>Four conditions to send it:<br><br>* The Sale System wants the POI to log it in the transaction log.<br>* Because of reconciliation with total on OperatorID.<br>* Because the POI needs it.<br>* Acquirer or issuer need it.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `shift_number` | `str` | Optional | Shift number.<br>Same as OperatorID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `token_requested_type` | [`TokenRequestedType1Enum`](../../doc/models/token-requested-type-1-enum.md) | Optional | Type of token replacing the PAN of a payment card to identify the payment<br>mean of the customer. It allows, for a merchant, to use a token for a transaction<br>only or for a longer period.<br>Possible values:<br><br>* **Customer**<br>* **Transaction** |
| `customer_order_req` | [`List[CustomerOrderReqEnum]`](../../doc/models/customer-order-req-enum.md) | Optional | List of customer order open, closed or both to be sent in the response messages.<br>Possible values:<br><br>* **Both**<br>* **Closed**<br>* **Open** |
| `poi_serial_number` | `str` | Optional | Serial number of a POI Terminal.<br>If the login involve a POI Terminal and not the first Login to the POI System.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
import dateutil.parser

from adyen.models.login_request_2 import LoginRequest2
from adyen.models.sale_software_1 import SaleSoftware1
from adyen.models.sale_terminal_data_2 import SaleTerminalData2
from adyen.models.token_requested_type_1_enum import TokenRequestedType1Enum

login_request_2 = LoginRequest2(
    date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    sale_software=SaleSoftware1(
        manufacturer_id='ManufacturerID4',
        application_name='ApplicationName8',
        software_version='SoftwareVersion0',
        certification_code='CertificationCode4'
    ),
    operator_language='OperatorLanguage4',
    sale_terminal_data=SaleTerminalData2(
        totals_group_id='TotalsGroupID4'
    ),
    training_mode_flag=False,
    operator_id='OperatorID0',
    shift_number='ShiftNumber2',
    token_requested_type=TokenRequestedType1Enum.TRANSACTION
)
```

