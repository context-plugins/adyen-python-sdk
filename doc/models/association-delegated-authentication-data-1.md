
# Association Delegated Authentication Data 1

Contains authentication information required to associate the resource with the SCA device.

## Structure

`AssociationDelegatedAuthenticationData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to authenticate the request. You obtain this information by using our authentication SDK.<br><br>**Constraints**: *Maximum Length*: `20000` |

## Example

```python
from adyen.models.association_delegated_authentication_data_1 import AssociationDelegatedAuthenticationData1

association_delegated_authentication_data_1 = AssociationDelegatedAuthenticationData1(
    sdk_output='sdkOutput6'
)
```

