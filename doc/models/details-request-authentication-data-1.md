
# Details Request Authentication Data 1

Data for 3DS authentication.

## Structure

`DetailsRequestAuthenticationData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**.<br><br>**Default**: `False` |

## Example

```python
from adyen.models.details_request_authentication_data_1 import DetailsRequestAuthenticationData1

details_request_authentication_data_1 = DetailsRequestAuthenticationData1(
    authentication_only=False
)
```

