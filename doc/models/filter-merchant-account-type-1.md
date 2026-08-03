
# Filter Merchant Account Type 1

Shows how merchant accounts are included in company-level webhooks. Possible values:

* **includeAccounts**
* **excludeAccounts**
* **allAccounts**: Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`.

## Enumeration

`FilterMerchantAccountType1`

## Fields

| Name |
|  --- |
| `ALLACCOUNTS` |
| `EXCLUDEACCOUNTS` |
| `INCLUDEACCOUNTS` |

## Example

```python
from adyen.models.filter_merchant_account_type_1 import FilterMerchantAccountType1

filter_merchant_account_type_1 = FilterMerchantAccountType1.EXCLUDEACCOUNTS
```

