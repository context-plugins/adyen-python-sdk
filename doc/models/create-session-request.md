
# Create Session Request

## Structure

`CreateSessionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The unique identifier of your merchant account. |
| `setup_token` | `str` | Required | The setup token provided by the POS Mobile SDK.<br><br>- When using the Android POS Mobile SDK, obtain the token through the `AuthenticationService.authenticate(setupToken)` callback of `AuthenticationService`.<br>- When using the iOS POS Mobile SDK, obtain the token through the `PaymentServiceDelegate.register(with:)` callback of `PaymentServiceDelegate`.<br><br>**Constraints**: *Maximum Length*: `50000` |
| `store` | `str` | Optional | The unique identifier of the store that you want to process transactions for. |

## Example

```python
from adyen.models.create_session_request import CreateSessionRequest

create_session_request = CreateSessionRequest(
    merchant_account='merchantAccount6',
    setup_token='setupToken0',
    store='store6'
)
```

