
# Pix Recurring

*This model accepts additional fields of type Any.*

## Structure

`PixRecurring`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_date` | `str` | Optional | The date on which the shopper's payment method will be charged, in YYYY-MM-DD format. |
| `business_day_only` | `bool` | Optional | Flag used to define whether liquidation can happen only on business days |
| `ends_at` | `str` | Optional | End date of the billing plan, in YYYY-MM-DD format. The end date must align with the frequency and the start date of the billing plan. If left blank, the subscription will continue indefinitely unless it is cancelled by the shopper. |
| `frequency` | [`Frequency2`](../../doc/models/frequency-2.md) | Optional | - |
| `min_amount` | [`MinAmount`](../../doc/models/min-amount.md) | Optional | - |
| `original_psp_reference` | `str` | Optional | The pspReference for the failed recurring payment. Find this in AUTHORISATION webhook you received after the billing date. |
| `recurring_amount` | [`RecurringAmount`](../../doc/models/recurring-amount.md) | Optional | - |
| `recurring_statement` | `str` | Optional | The text that that will be shown on the shopper's bank statement for the recurring payments. We recommend to add a descriptive text about the subscription to let your shoppers recognize your recurring payments.<br>Maximum length: 35 characters. |
| `retry_policy` | `bool` | Optional | When set to true, you can retry for failed recurring payments. The default value is true. |
| `starts_at` | `str` | Optional | Start date of the billing plan, in YYYY-MM-DD format. The default value is the transaction date. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.frequency_2 import Frequency2
from adyen.models.min_amount import MinAmount
from adyen.models.pix_recurring import PixRecurring

pix_recurring = PixRecurring(
    billing_date='billingDate0',
    business_day_only=False,
    ends_at='endsAt8',
    frequency=Frequency2.YEARLY,
    min_amount=MinAmount(
        currency='currency6',
        value=156,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

