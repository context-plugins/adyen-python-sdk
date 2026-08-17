
# Funds Collection

## Structure

`FundsCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_identification` | [`BankAccountIdentification1`](../../doc/models/bank-account-identification-1.md) | Optional | Contains the identification information of the account to which you can transfer funds related to repayments. |
| `funds_collection_type` | [`FundsCollectionType2Enum`](../../doc/models/funds-collection-type-2-enum.md) | Optional | The type of funds collection.<br><br>Possible values: **UnscheduledRepayment**, **Revocation**. |

## Example

```python
from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2_enum import FundsCollectionType2Enum

funds_collection = FundsCollection(
    account_identification=BankAccountIdentification1(
        mtype='BankAccountIdentification1'
    ),
    funds_collection_type=FundsCollectionType2Enum.UNSCHEDULEDREPAYMENT
)
```

