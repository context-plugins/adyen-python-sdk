
# Pay Pal

## Structure

`PayPal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `order_id` | `str` | Optional | The unique ID associated with the order. |
| `payee_preferred` | `str` | Optional | IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED |
| `payer_id` | `str` | Optional | The unique ID associated with the payer. |
| `payer_selected` | `str` | Optional | PAYPAL or PAYPAL_CREDIT |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | [`SubtypeEnum`](../../doc/models/subtype-enum.md) | Optional | The type of flow to initiate. |
| `mtype` | `str` | Required, Constant | **paypal**<br><br>**Value**: `"paypal"` |

## Example

```python
from adyen.models.pay_pal import PayPal

pay_pal = PayPal(
    checkout_attempt_id='checkoutAttemptId0',
    order_id='orderID8',
    payee_preferred='payeePreferred4',
    payer_id='payerID0',
    payer_selected='payerSelected0'
)
```

