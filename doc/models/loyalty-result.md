
# Loyalty Result

Data related to the result of a processed loyalty transaction.
In the Message Response, the result of each loyalty brand transaction.

## Structure

`LoyaltyResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account` | [`LoyaltyAccount1`](../../doc/models/loyalty-account-1.md) | Required | Data related to a loyalty account processed in the transaction. |
| `current_balance` | `float` | Optional | Balance of an account.<br>If known (provided by the card or an external host).<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `loyalty_acquirer_data` | [`LoyaltyAcquirerData1`](../../doc/models/loyalty-acquirer-data-1.md) | Optional | Data related to the loyalty Acquirer during a loyalty transaction.<br>If content not empty. |

## Example

```python
import dateutil.parser

from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_1 import LoyaltyAccount1
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2
from adyen.models.loyalty_acquirer_data_1 import LoyaltyAcquirerData1
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.transaction_id_type import TransactionIDType

loyalty_result = LoyaltyResult(
    loyalty_account=LoyaltyAccount1(
        loyalty_account_id=LoyaltyAccountID2(
            entry_mode=[
                EntryModeEnum.FILE
            ],
            identification_type=IdentificationType11Enum.ISOTRACK2,
            loyalty_id='LoyaltyID4',
            identification_support=IdentificationSupport1Enum.HYBRIDCARD
        ),
        loyalty_brand='LoyaltyBrand0'
    ),
    current_balance=180.58,
    loyalty_acquirer_data=LoyaltyAcquirerData1(
        loyalty_acquirer_id='LoyaltyAcquirerID4',
        approval_code='ApprovalCode4',
        loyalty_transaction_id=TransactionIDType(
            transaction_id='TransactionID6',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        host_reconciliation_id='HostReconciliationID4'
    )
)
```

