
# Disable Result

## Structure

`DisableResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | `str` | Optional | Depending on whether a specific recurring detail was in the request, result is either [detail-successfully-disabled] or [all-details-successfully-disabled]. |

## Example

```python
from adyen.models.disable_result import DisableResult

disable_result = DisableResult(
    response='response6'
)
```

