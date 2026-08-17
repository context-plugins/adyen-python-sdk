
# List Nonprofits Request

## Structure

`ListNonprofitsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Required | The unique identifiers of the account holders to be included in a donation campaign.<br><br>**Constraints**: *Minimum Items*: `1` |

## Example

```python
from adyen.models.list_nonprofits_request import ListNonprofitsRequest

list_nonprofits_request = ListNonprofitsRequest(
    account_holder_ids=[
        'accountHolderIds1',
        'accountHolderIds2',
        'accountHolderIds3'
    ]
)
```

