
# Sofort Info

*This model accepts additional fields of type Any.*

## Structure

`SofortInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Required | Sofort logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sofort_info import SofortInfo

sofort_info = SofortInfo(
    currency_code='currencyCode4',
    logo='logo0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

