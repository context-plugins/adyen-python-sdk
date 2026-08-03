
# Transaction List for Account

*This model accepts additional fields of type Any.*

## Structure

`TransactionListForAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The account for which to retrieve the transactions. |
| `page` | `int` | Required | The page of transactions to retrieve.<br>Each page lists fifty (50) transactions.  The most recent transactions are included on page 1. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_list_for_account import TransactionListForAccount

transaction_list_for_account = TransactionListForAccount(
    account_code='accountCode2',
    page=78,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

