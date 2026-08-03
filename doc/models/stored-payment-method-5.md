
# Stored Payment Method 5

*This model accepts additional fields of type Any.*

## Structure

`StoredPaymentMethod5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `device_id` | `str` | Optional | **Constraints**: *Maximum Length*: `36` |
| `issuer` | `str` | Optional | - |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `risk_signals` | [`PixPayByBankRiskSignals`](../../doc/models/pix-pay-by-bank-risk-signals.md) | Optional | - |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type45`](../../doc/models/type-45.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.confidence_score import ConfidenceScore
from adyen.models.pix_pay_by_bank_risk_signals import PixPayByBankRiskSignals
from adyen.models.stored_payment_method_5 import StoredPaymentMethod5

stored_payment_method_5 = StoredPaymentMethod5(
    checkout_attempt_id='checkoutAttemptId4',
    device_id='deviceId8',
    issuer='issuer8',
    recurring_detail_reference='recurringDetailReference8',
    risk_signals=PixPayByBankRiskSignals(
        confidence_score=ConfidenceScore(
            errors=[
                'errors9',
                'errors0',
                'errors1'
            ],
            score=155.44,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        elapsed_time_since_boot=84,
        is_rooted_device=False,
        language='language0',
        os_version='osVersion8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

