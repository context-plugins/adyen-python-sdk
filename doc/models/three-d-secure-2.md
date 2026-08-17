
# Three D Secure 2

The data of the result from the 3DS authentication.

## Structure

`ThreeDSecure2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_transaction_id` | `str` | Optional | The transaction identifier for the Access Control Server |

## Example

```python
from adyen.models.three_d_secure_2 import ThreeDSecure2

three_d_secure_2 = ThreeDSecure2(
    acs_transaction_id='acsTransactionId6'
)
```

