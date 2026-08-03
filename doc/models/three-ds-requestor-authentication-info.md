
# Three Ds Requestor Authentication Info

Information about how the 3DS Requestor authenticated the cardholder before or during the transaction

*This model accepts additional fields of type Any.*

## Structure

`ThreeDsRequestorAuthenticationInfo`

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
from adyen.models.three_ds_requestor_authentication_info import ThreeDsRequestorAuthenticationInfo

three_ds_requestor_authentication_info = ThreeDsRequestorAuthenticationInfo(
    three_ds_req_auth_data='threeDSReqAuthData2',
    three_ds_req_auth_method=ThreeDsReqAuthMethod.ENUM_03,
    three_ds_req_auth_timestamp='threeDSReqAuthTimestamp6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

