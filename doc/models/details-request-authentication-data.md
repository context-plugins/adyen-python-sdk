
# Details Request Authentication Data

## Structure

`DetailsRequestAuthenticationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**.<br><br>**Default**: `False` |

## Example

```python
from adyen.models.details_request_authentication_data import DetailsRequestAuthenticationData

details_request_authentication_data = DetailsRequestAuthenticationData(
    authentication_only=False
)
```

