
# Opi

## Structure

`Opi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_pay_at_table` | `bool` | Optional | Indicates if Pay at table is enabled. |
| `pay_at_table_store_number` | `str` | Optional | The store number to use for Pay at Table. |
| `pay_at_table_url` | `str` | Optional | The URL and port number used for Pay at Table communication. |

## Example

```python
from adyen.models.opi import Opi

opi = Opi(
    enable_pay_at_table=False,
    pay_at_table_store_number='payAtTableStoreNumber0',
    pay_at_table_url='payAtTableURL2'
)
```

