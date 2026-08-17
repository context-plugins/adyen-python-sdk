
# Filter Merchant Account Type Enum

Shows how merchant accounts are filtered when configuring the webhook.

Possible values:

* **allAccounts** : Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`.
* **includeAccounts** : The webhook is configured for the merchant accounts listed in `filterMerchantAccounts`.
* **excludeAccounts** : The webhook is not configured for the merchant accounts listed in `filterMerchantAccounts`.

## Enumeration

`FilterMerchantAccountTypeEnum`

## Fields

| Name |
|  --- |
| `ALLACCOUNTS` |
| `EXCLUDEACCOUNTS` |
| `INCLUDEACCOUNTS` |

## Example

```python
from adyen.models.filter_merchant_account_type_enum import FilterMerchantAccountTypeEnum

filter_merchant_account_type = FilterMerchantAccountTypeEnum.EXCLUDEACCOUNTS
```

