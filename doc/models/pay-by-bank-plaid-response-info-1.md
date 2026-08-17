
# Pay by Bank Plaid Response Info 1

**paybybank_plaid** details

## Structure

`PayByBankPlaidResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Merchant logo |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.pay_by_bank_plaid_response_info_1 import PayByBankPlaidResponseInfo1
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

pay_by_bank_plaid_response_info_1 = PayByBankPlaidResponseInfo1(
    logo='logo8',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

