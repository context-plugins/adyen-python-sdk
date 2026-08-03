
# Affirm Info

*This model accepts additional fields of type Any.*

## Structure

`AffirmInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |
| `support_email` | `str` | Required | Merchant support email used to manage disputes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm_info import AffirmInfo

affirm_info = AffirmInfo(
    support_email='supportEmail4',
    price_plan='pricePlan6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

