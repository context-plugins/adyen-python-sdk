
# Filter Merchant Account Type 2 Enum

Shows how merchant accounts are filtered when configuring the webhook. Possible values:

* **includeAccounts**: The webhook is configured for the merchant accounts listed in `filterMerchantAccounts`.
* **excludeAccounts**: The webhook is not configured for the merchant accounts listed in `filterMerchantAccounts`.
* **allAccounts**: Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`.

## Enumeration

`FilterMerchantAccountType2Enum`

## Fields

| Name |
|  --- |
| `ALLACCOUNTS` |
| `EXCLUDEACCOUNTS` |
| `INCLUDEACCOUNTS` |

## Example

```python
from adyen.models.filter_merchant_account_type_2_enum import FilterMerchantAccountType2Enum

filter_merchant_account_type_2 = FilterMerchantAccountType2Enum.EXCLUDEACCOUNTS
```

