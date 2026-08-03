
# Affirm Info 1

Details to provide if `type` is **affirm**.

*This model accepts additional fields of type Any.*

## Structure

`AffirmInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |
| `support_email` | `str` | Required | Merchant support email used to manage disputes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm_info_1 import AffirmInfo1

affirm_info_1 = AffirmInfo1(
    support_email='supportEmail8',
    price_plan='pricePlan8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

