
# Account Holder Resource

## Structure

`AccountHolderResource`

## Inherits From

[`Resource`](../../doc/models/resource.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the resource connected to the component. For [Platform Experience components](https://docs.adyen.com/platforms/build-user-dashboards), this is the account holder linked to the balance account shown in the component.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.resource import AccountHolderResource

account_holder_resource = AccountHolderResource(
    account_holder_id='accountHolderId4',
    mtype='accountHolder'
)
```

