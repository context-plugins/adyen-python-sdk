
# Recurring Detail Wrapper

## Structure

`RecurringDetailWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recurring_detail` | [`RecurringDetail`](../../doc/models/recurring-detail.md) | Optional | - |

## Example

```python
from adyen.models.address import Address
from adyen.models.bank_account import BankAccount
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
        bank=BankAccount(
            bank_account_number='bankAccountNumber8',
            bank_city='bankCity0',
            bank_location_id='bankLocationId2',
            bank_name='bankName4',
            bic='bic0'
        ),
        billing_address=Address(
            city='city8',
            country='country6',
            house_number_or_name='houseNumberOrName0',
            postal_code='postalCode6',
            street='street2',
            state_or_province='stateOrProvince0'
        )
    )
)
```

