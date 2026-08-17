
# Opi 1

Settings for an Oracle Payment Interface (OPI) integration.

## Structure

`Opi1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_pay_at_table` | `bool` | Optional | Indicates if Pay at table is enabled. |
| `pay_at_table_store_number` | `str` | Optional | The store number to use for Pay at Table. |
| `pay_at_table_url` | `str` | Optional | The URL and port number used for Pay at Table communication. |

## Example

```python
from adyen.models.opi_1 import Opi1

opi_1 = Opi1(
    enable_pay_at_table=False,
    pay_at_table_store_number='payAtTableStoreNumber2',
    pay_at_table_url='payAtTableURL0'
)
```

