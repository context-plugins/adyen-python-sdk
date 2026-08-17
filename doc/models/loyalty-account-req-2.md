
# Loyalty Account Req 2

Data related to a requested Loyalty program or account.

## Structure

`LoyaltyAccountReq2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_acquisition_reference` | [`TransactionIDType`](../../doc/models/transaction-id-type.md) | Optional | Identification of a transaction for the Sale System or the POI System. |
| `loyalty_account_id` | [`LoyaltyAccountID`](../../doc/models/loyalty-account-id.md) | Optional | Identification of a Loyalty account.<br>In the Payment Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device). |

## Example

```python
import dateutil.parser

from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_id import LoyaltyAccountID
from adyen.models.loyalty_account_req_2 import LoyaltyAccountReq2
from adyen.models.transaction_id_type import TransactionIDType

loyalty_account_req_2 = LoyaltyAccountReq2(
    card_acquisition_reference=TransactionIDType(
        transaction_id='TransactionID8',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    loyalty_account_id=LoyaltyAccountID(
        entry_mode=[
            EntryModeEnum.FILE
        ],
        identification_type=IdentificationType11Enum.ISOTRACK2,
        loyalty_id='LoyaltyID4',
        identification_support=IdentificationSupport1Enum.HYBRIDCARD
    )
)
```

