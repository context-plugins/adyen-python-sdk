
# Transaction Description Info

*This model accepts additional fields of type Any.*

## Structure

`TransactionDescriptionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `doing_business_as_name` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**.<br><br>**Constraints**: *Maximum Length*: `22` |
| `mtype` | [`Type33`](../../doc/models/type-33.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

transaction_description_info = TransactionDescriptionInfo(
    doing_business_as_name='doingBusinessAsName2',
    mtype=Type33.DYNAMIC,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

