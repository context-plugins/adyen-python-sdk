
# Sepa Direct Debit Info 2

Details to provide if `type` is **sepadirectdebit**.

*This model accepts additional fields of type Any.*

## Structure

`SepaDirectDebitInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creditor_id` | `str` | Optional | Creditor id |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sepa_direct_debit_info_2 import SepaDirectDebitInfo2
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

sepa_direct_debit_info_2 = SepaDirectDebitInfo2(
    creditor_id='creditorId6',
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

