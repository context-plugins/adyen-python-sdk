
# Cash App Update Info

*This model accepts additional fields of type Any.*

## Structure

`CashAppUpdateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo_url` | `str` | Optional | The URL of the logo image shown in Cash App checkout next to payments. |
| `merchant_name` | `str` | Optional | The merchant display name shown in Cash App checkout. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cash_app_update_info import CashAppUpdateInfo

cash_app_update_info = CashAppUpdateInfo(
    logo_url='logoUrl2',
    merchant_name='merchantName2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

