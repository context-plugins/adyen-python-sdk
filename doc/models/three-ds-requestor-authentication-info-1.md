
# Three Ds Requestor Authentication Info 1

*This model accepts additional fields of type Any.*

## Structure

`ThreeDsRequestorAuthenticationInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_req_auth_data` | `str` | Optional | Data that documents and supports a specific authentication process. Maximum length: 2048 bytes. |
| `three_ds_req_auth_method` | [`ThreeDsReqAuthMethod`](../../doc/models/three-ds-req-auth-method.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `three_ds_req_auth_timestamp` | `str` | Optional | Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_ds_req_auth_method import ThreeDsReqAuthMethod
from adyen.models.three_ds_requestor_authentication_info_1 import ThreeDsRequestorAuthenticationInfo1

three_ds_requestor_authentication_info_1 = ThreeDsRequestorAuthenticationInfo1(
    three_ds_req_auth_data='threeDSReqAuthData0',
    three_ds_req_auth_method=ThreeDsReqAuthMethod.ENUM_05,
    three_ds_req_auth_timestamp='threeDSReqAuthTimestamp8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

