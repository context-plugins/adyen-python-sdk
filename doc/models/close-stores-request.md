
# Close Stores Request

## Structure

`CloseStoresRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `stores` | `List[str]` | Required | List of stores to be closed. |

## Example

```python
from adyen.models.close_stores_request import CloseStoresRequest

close_stores_request = CloseStoresRequest(
    account_holder_code='accountHolderCode2',
    stores=[
        'stores7',
        'stores8'
    ]
)
```

