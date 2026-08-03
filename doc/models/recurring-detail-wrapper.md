
# Recurring Detail Wrapper

*This model accepts additional fields of type Any.*

## Structure

`RecurringDetailWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recurring_detail` | [`RecurringDetail`](../../doc/models/recurring-detail.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank import Bank
from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.recurring_detail import RecurringDetail
from adyen.models.recurring_detail_wrapper import RecurringDetailWrapper

recurring_detail_wrapper = RecurringDetailWrapper(
    recurring_detail=RecurringDetail(
        recurring_detail_reference='recurringDetailReference2',
        variant='variant6',
        additional_data={
            'key0': 'additionalData2'
        },
        alias='alias4',
        alias_type='aliasType6',
        bank=Bank(
            bank_account_number='bankAccountNumber8',
            bank_city='bankCity0',
            bank_location_id='bankLocationId2',
            bank_name='bankName4',
            bic='bic0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        billing_address=BillingAddress7(
            city='city8',
            country='country6',
            house_number_or_name='houseNumberOrName0',
            postal_code='postalCode6',
            street='street2',
            state_or_province='stateOrProvince0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

