
# Utility Request

## Structure

`UtilityRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `origin_domains` | `List[str]` | Required | The list of origin domains, for which origin keys are requested. |

## Example

```python
from adyen.models.utility_request import UtilityRequest

utility_request = UtilityRequest(
    origin_domains=[
        'originDomains6',
        'originDomains7',
        'originDomains8'
    ]
)
```

