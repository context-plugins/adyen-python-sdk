
# Sofort Response Info

*This model accepts additional fields of type Any.*

## Structure

`SofortResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Optional | Sofort logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sofort_response_info import SofortResponseInfo

sofort_response_info = SofortResponseInfo(
    currency_code='currencyCode2',
    logo='logo8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

