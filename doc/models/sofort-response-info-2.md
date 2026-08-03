
# Sofort Response Info 2

Sofort details.

*This model accepts additional fields of type Any.*

## Structure

`SofortResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Optional | Sofort logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sofort_response_info_2 import SofortResponseInfo2

sofort_response_info_2 = SofortResponseInfo2(
    currency_code='currencyCode4',
    logo='logo0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

