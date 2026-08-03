
# Sofort Info 2

Sofort details.

*This model accepts additional fields of type Any.*

## Structure

`SofortInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Required | Sofort logo. Format: Base64-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sofort_info_2 import SofortInfo2

sofort_info_2 = SofortInfo2(
    currency_code='currencyCode2',
    logo='logo8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

