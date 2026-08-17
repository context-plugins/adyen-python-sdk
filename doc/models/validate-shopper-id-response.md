
# Validate Shopper Id Response

## Structure

`ValidateShopperIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Reason for the result. |
| `result` | [`Result1Enum`](../../doc/models/result-1-enum.md) | Optional | Result of the validation. Ex: valid, invalid, unknown |

## Example

```python
from adyen.models.result_1_enum import Result1Enum
from adyen.models.validate_shopper_id_response import ValidateShopperIdResponse

validate_shopper_id_response = ValidateShopperIdResponse(
    reason='reason4',
    result=Result1Enum.VALID
)
```

