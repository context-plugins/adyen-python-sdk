
# Ideal Auth Link Request

## Structure

`IdealAuthLinkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `150` |

## Example

```python
from adyen.models.ideal_auth_link_request import IdealAuthLinkRequest

ideal_auth_link_request = IdealAuthLinkRequest(
    account_holder_id='AH00000000000000000000000'
)
```

