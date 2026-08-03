
# Recurring Details Result

*This model accepts additional fields of type Any.*

## Structure

`RecurringDetailsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creation_date` | `datetime` | Optional | The date when the recurring details were created. |
| `details` | [`List[RecurringDetailWrapper]`](../../doc/models/recurring-detail-wrapper.md) | Optional | Payment details stored for recurring payments. |
| `last_known_shopper_email` | `str` | Optional | The most recent email for this shopper (if available). |
| `shopper_reference` | `str` | Optional | The reference you use to uniquely identify the shopper (e.g. user ID or account ID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.bank import Bank
from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.recurring_detail import RecurringDetail
from adyen.models.recurring_detail_wrapper import RecurringDetailWrapper
from adyen.models.recurring_details_result import RecurringDetailsResult

recurring_details_result = RecurringDetailsResult(
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    details=[
        RecurringDetailWrapper(
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
    ],
    last_known_shopper_email='lastKnownShopperEmail4',
    shopper_reference='shopperReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

