
# Loyalty Result

Data related to the result of a processed loyalty transaction.
In the Message Response, the result of each loyalty brand transaction.

*This model accepts additional fields of type Any.*

## Structure

`LoyaltyResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account` | [`LoyaltyAccount12`](../../doc/models/loyalty-account-12.md) | Required | - |
| `current_balance` | `float` | Optional | Balance of an account.<br>If known (provided by the card or an external host).<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `loyalty_acquirer_data` | [`LoyaltyAcquirerData`](../../doc/models/loyalty-acquirer-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account_12 import LoyaltyAccount12
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_acquirer_data import LoyaltyAcquirerData
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.loyalty_transaction_id import LoyaltyTransactionId

loyalty_result = LoyaltyResult(
    loyalty_account=LoyaltyAccount12(
        loyalty_account_id=LoyaltyAccountId3(
            entry_mode=[
                EntryMode.FILE
            ],
            identification_type=IdentificationType11.ISOTRACK2,
            loyalty_id='LoyaltyID4',
            identification_support=IdentificationSupport1.HYBRIDCARD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        loyalty_brand='LoyaltyBrand0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    current_balance=180.58,
    loyalty_acquirer_data=LoyaltyAcquirerData(
        loyalty_acquirer_id='LoyaltyAcquirerID4',
        approval_code='ApprovalCode4',
        loyalty_transaction_id=LoyaltyTransactionId(
            transaction_id='TransactionID6',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        host_reconciliation_id='HostReconciliationID4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

