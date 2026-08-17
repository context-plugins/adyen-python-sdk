
# Store Split Configuration 1

Rules for Adyen for Platforms merchants to split the transaction amount and fees.

## Structure

`StoreSplitConfiguration1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The [unique identifier of the balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id) to which the split amount must be booked, depending on the defined [split logic](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/splitConfigurations#request-rules-splitLogic). |
| `split_configuration_id` | `str` | Optional | The unique identifier of the [split configuration profile](https://docs.adyen.com/platforms/automatic-split-configuration/create-split-configuration/). |

## Example

```python
from adyen.models.store_split_configuration_1 import StoreSplitConfiguration1

store_split_configuration_1 = StoreSplitConfiguration1(
    balance_account_id='balanceAccountId4',
    split_configuration_id='splitConfigurationId2'
)
```

