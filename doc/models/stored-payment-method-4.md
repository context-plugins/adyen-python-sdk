
# Stored Payment Method 4

## Structure

`StoredPaymentMethod4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `pix_recurring` | [`PixRecurring`](../../doc/models/pix-recurring.md) | Optional | - |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type44Enum`](../../doc/models/type-44-enum.md) | Optional | The payment method type. |

## Example

```python
from adyen.models.amount_42 import Amount42
from adyen.models.frequency_2_enum import Frequency2Enum
from adyen.models.pix_recurring import PixRecurring
from adyen.models.stored_payment_method_4 import StoredPaymentMethod4

stored_payment_method_4 = StoredPaymentMethod4(
    checkout_attempt_id='checkoutAttemptId0',
    pix_recurring=PixRecurring(
        billing_date='billingDate0',
        business_day_only=False,
        ends_at='endsAt8',
        frequency=Frequency2Enum.YEARLY,
        min_amount=Amount42(
            currency='currency6',
            value=156
        )
    ),
    recurring_detail_reference='recurringDetailReference4',
    sdk_data='sdkData6',
    stored_payment_method_id='storedPaymentMethodId8'
)
```

