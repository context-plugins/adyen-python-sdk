
# Pay by Bank Plaid Response Info

## Structure

`PayByBankPlaidResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Merchant logo |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.pay_by_bank_plaid_response_info import PayByBankPlaidResponseInfo
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

pay_by_bank_plaid_response_info = PayByBankPlaidResponseInfo(
    logo='logo2',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

