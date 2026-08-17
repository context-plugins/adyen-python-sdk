
# Loyalty Account

This data structure conveys the identification of the account and the associated loyalty brand.
Data related to a loyalty account processed in the transaction.

## Structure

`LoyaltyAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account_id` | [`LoyaltyAccountID2`](../../doc/models/loyalty-account-id-2.md) | Required | Identification of a Loyalty account. |
| `loyalty_brand` | `str` | Optional | Identification of a Loyalty brand.<br>If a card is analysed.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2

loyalty_account = LoyaltyAccount(
    loyalty_account_id=LoyaltyAccountID2(
        entry_mode=[
            EntryModeEnum.FILE
        ],
        identification_type=IdentificationType11Enum.ISOTRACK2,
        loyalty_id='LoyaltyID4',
        identification_support=IdentificationSupport1Enum.HYBRIDCARD
    ),
    loyalty_brand='LoyaltyBrand2'
)
```

