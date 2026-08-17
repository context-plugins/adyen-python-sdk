
# Loyalty Data

In the Payment, Loyalty or Balance Inquiry Request message, it allows the Sale Terminal to send the identification of the loyalty account or an awarded amount or an amount to redeem to the loyalty account.
Data related to a Loyalty program or account.

## Structure

`LoyaltyData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_acquisition_reference` | [`TransactionIDType3`](../../doc/models/transaction-id-type-3.md) | Optional | Reference to the last CardAcquisition, to use the same card.<br>If the loyalty account ID comes from a previous CardAcquisition. |
| `loyalty_account_id` | [`LoyaltyAccountID1`](../../doc/models/loyalty-account-id-1.md) | Optional | Identification of a Loyalty account.<br>If loyalty identification of the loyalty account is realised by the Sale System. |

## Example

```python
import dateutil.parser

from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_id_1 import LoyaltyAccountID1
from adyen.models.loyalty_data import LoyaltyData
from adyen.models.transaction_id_type_3 import TransactionIDType3

loyalty_data = LoyaltyData(
    card_acquisition_reference=TransactionIDType3(
        transaction_id='TransactionID8',
        time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    loyalty_account_id=LoyaltyAccountID1(
        entry_mode=[
            EntryModeEnum.FILE
        ],
        identification_type=IdentificationType11Enum.ISOTRACK2,
        loyalty_id='LoyaltyID4',
        identification_support=IdentificationSupport1Enum.HYBRIDCARD
    )
)
```

