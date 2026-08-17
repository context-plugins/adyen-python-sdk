
# Ideal Donations

## Structure

`IdealDonations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `issuer` | `str` | Optional | The iDEAL issuer value of the shopper's selected bank. Set this to an **id** of an iDEAL issuer to preselect it. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type25Enum`](../../doc/models/type-25-enum.md) | Optional | **ideal**<br><br>**Default**: `"ideal"` |

## Example

```python
from adyen.models.ideal_donations import IdealDonations
from adyen.models.type_25_enum import Type25Enum

ideal_donations = IdealDonations(
    checkout_attempt_id='checkoutAttemptId6',
    issuer='issuer0',
    recurring_detail_reference='recurringDetailReference0',
    sdk_data='sdkData0',
    stored_payment_method_id='storedPaymentMethodId4',
    mtype=Type25Enum.IDEAL
)
```

