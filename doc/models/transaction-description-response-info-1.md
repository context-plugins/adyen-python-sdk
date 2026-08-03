
# Transaction Description Response Info 1

Information regarding the transaction description.

*This model accepts additional fields of type Any.*

## Structure

`TransactionDescriptionResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `doing_business_as_name` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**.<br><br>**Constraints**: *Maximum Length*: `22` |
| `mtype` | [`Type33`](../../doc/models/type-33.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_33 import Type33

transaction_description_response_info_1 = TransactionDescriptionResponseInfo1(
    doing_business_as_name='doingBusinessAsName8',
    mtype=Type33.DYNAMIC,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

