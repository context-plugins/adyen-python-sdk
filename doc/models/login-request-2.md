
# Login Request 2

Content of the Login Request message.

*This model accepts additional fields of type Any.*

## Structure

`LoginRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_time` | `datetime` | Required | Date and Time. In the Login request message, the Sale System gives its date and time to the POI System. In the Login response, the POI System gives its date and time to the Sale System. |
| `sale_software` | [`SaleSoftware2`](../../doc/models/sale-software-2.md) | Required | - |
| `sale_terminal_data` | [`SaleTerminalData3`](../../doc/models/sale-terminal-data-3.md) | Optional | - |
| `training_mode_flag` | `bool` | Optional | Training mode.<br>This flag indicates to the POI that the entire session will be not used to make real transaction, but is used for test of system or operator training.<br><br>**Default**: `False` |
| `operator_language` | `str` | Required | Language of the Cashier or Operator.<br>Default value for Device type displays.<br><br>**Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br>Four conditions to send it:<br><br>* The Sale System wants the POI to log it in the transaction log.<br>* Because of reconciliation with total on OperatorID.<br>* Because the POI needs it.<br>* Acquirer or issuer need it.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `shift_number` | `str` | Optional | Shift number.<br>Same as OperatorID.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `token_requested_type` | [`TokenRequestedType1`](../../doc/models/token-requested-type-1.md) | Optional | - |
| `customer_order_req` | [`List[CustomerOrderReq]`](../../doc/models/customer-order-req.md) | Optional | List of customer order open, closed or both to be sent in the response messages.<br>Possible values:<br><br>* **Both**<br>* **Closed**<br>* **Open** |
| `poi_serial_number` | `str` | Optional | Serial number of a POI Terminal.<br>If the login involve a POI Terminal and not the first Login to the POI System.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.login_request_2 import LoginRequest2
from adyen.models.sale_software_2 import SaleSoftware2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.token_requested_type_1 import TokenRequestedType1

login_request_2 = LoginRequest2(
    date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    sale_software=SaleSoftware2(
        manufacturer_id='ManufacturerID4',
        application_name='ApplicationName8',
        software_version='SoftwareVersion0',
        certification_code='CertificationCode4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    operator_language='OperatorLanguage4',
    sale_terminal_data=SaleTerminalData3(
        totals_group_id='TotalsGroupID4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    training_mode_flag=False,
    operator_id='OperatorID0',
    shift_number='ShiftNumber2',
    token_requested_type=TokenRequestedType1.TRANSACTION,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

