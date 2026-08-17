
# Three D Secure

## Structure

`ThreeDSecure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acs_transaction_id` | `str` | Optional | The transaction identifier for the Access Control Server |

## Example

```python
from adyen.models.three_d_secure import ThreeDSecure

three_d_secure = ThreeDSecure(
    acs_transaction_id='acsTransactionId4'
)
```

