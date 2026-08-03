
# Opi 1

Settings for an Oracle Payment Interface (OPI) integration.

*This model accepts additional fields of type Any.*

## Structure

`Opi1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_pay_at_table` | `bool` | Optional | Indicates if Pay at table is enabled. |
| `pay_at_table_store_number` | `str` | Optional | The store number to use for Pay at Table. |
| `pay_at_table_url` | `str` | Optional | The URL and port number used for Pay at Table communication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.opi_1 import Opi1

opi_1 = Opi1(
    enable_pay_at_table=False,
    pay_at_table_store_number='payAtTableStoreNumber2',
    pay_at_table_url='payAtTableURL0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

