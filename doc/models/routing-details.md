
# Routing Details

## Structure

`RoutingDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `str` | Optional | A human-readable explanation specific to this occurrence of the problem. |
| `error_code` | `str` | Optional | A code that identifies the problem type. |
| `priority` | [`Priority1Enum`](../../doc/models/priority-1-enum.md) | Optional | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.<br><br>Possible values:<br><br>* **regular**: For normal, low-value transactions.<br><br>* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.<br><br>* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.<br><br>* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).<br><br>* **crossBorder**: For high-value transfers to a recipient in a different country.<br><br>* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
| `title` | `str` | Optional | A short, human-readable summary of the problem type. |

## Example

```python
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.routing_details import RoutingDetails

routing_details = RoutingDetails(
    detail='detail8',
    error_code='errorCode8',
    priority=Priority1Enum.REGULAR,
    title='title2'
)
```

