
# Delegated Authentication Data

## Structure

`DelegatedAuthenticationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to register the SCA device. You obtain this information by using our authentication SDK.<br><br>**Constraints**: *Maximum Length*: `20000` |

## Example

```python
from adyen.models.delegated_authentication_data import DelegatedAuthenticationData

delegated_authentication_data = DelegatedAuthenticationData(
    sdk_output='sdkOutput4'
)
```

