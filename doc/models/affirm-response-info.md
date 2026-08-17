
# Affirm Response Info

## Structure

`AffirmResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_api_key` | `str` | Optional | Affirm public API key |

## Example

```python
from adyen.models.affirm_response_info import AffirmResponseInfo

affirm_response_info = AffirmResponseInfo(
    public_api_key='publicApiKey0'
)
```

