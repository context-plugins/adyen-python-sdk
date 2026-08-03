
# Checkout Bank Transfer Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutBankTransferAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The account number of the bank transfer. |
| `bank_code` | `str` | Optional | The bank code of the bank transfer. |
| `beneficiary` | `str` | Optional | The name of the account holder. |
| `bic` | `str` | Optional | The BIC of the IBAN. |
| `branch_code` | `str` | Optional | The branch code of the bank transfer. |
| `download_url` | `str` | Optional | The url to download payment details with. |
| `iban` | `str` | Optional | The IBAN of the bank transfer. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `reference` | `str` | Optional | The transfer reference. |
| `routing_number` | `str` | Optional | The routing number of the bank transfer. |
| `shopper_email` | `str` | Optional | The e-mail of the shopper, included if an e-mail was sent to the shopper. |
| `sort_code` | `str` | Optional | The sort code of the bank transfer. |
| `total_amount` | [`TotalAmount2`](../../doc/models/total-amount-2.md) | Optional | - |
| `mtype` | [`Type503`](../../doc/models/type-503.md) | Required | The type of the action. |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_bank_transfer_action import CheckoutBankTransferAction
from adyen.models.type_503 import Type503

checkout_bank_transfer_action = CheckoutBankTransferAction(
    mtype=Type503.BANKTRANSFER,
    account_number='accountNumber8',
    bank_code='bankCode0',
    beneficiary='beneficiary8',
    bic='bic2',
    branch_code='branchCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

