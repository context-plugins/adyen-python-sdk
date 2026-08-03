
# Pay by Bank Plaid Response Info 1

**paybybank_plaid** details

*This model accepts additional fields of type Any.*

## Structure

`PayByBankPlaidResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Merchant logo |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_by_bank_plaid_response_info_1 import PayByBankPlaidResponseInfo1
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

pay_by_bank_plaid_response_info_1 = PayByBankPlaidResponseInfo1(
    logo='logo8',
    transaction_description=TransactionDescriptionInfo(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type33.FIXED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

