
# Delegated Authentication Data 1

Contains information required to register the SCA device.

## Structure

`DelegatedAuthenticationData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_output` | `str` | Required | A base64-encoded block with the data required to register the SCA device. You obtain this information by using our authentication SDK.<br><br>**Constraints**: *Maximum Length*: `20000` |

## Example

```python
from adyen.models.delegated_authentication_data_1 import DelegatedAuthenticationData1

delegated_authentication_data_1 = DelegatedAuthenticationData1(
    sdk_output='sdkOutput4'
)
```

