
# Affirm Update Info 1

Details to provide if `type` is **affirm**.

*This model accepts additional fields of type Any.*

## Structure

`AffirmUpdateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.affirm_update_info_1 import AffirmUpdateInfo1

affirm_update_info_1 = AffirmUpdateInfo1(
    price_plan='pricePlan4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

