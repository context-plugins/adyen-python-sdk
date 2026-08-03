
# Three Ds Requestor Prior Authentication Info

Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDsRequestorPriorAuthenticationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_req_prior_auth_data` | `str` | Optional | Data that documents and supports a specific authentication process. Maximum length: 2048 bytes. |
| `three_ds_req_prior_auth_method` | [`ThreeDsReqPriorAuthMethod`](../../doc/models/three-ds-req-prior-auth-method.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `three_ds_req_prior_auth_timestamp` | `str` | Optional | Date and time in UTC of the prior cardholder authentication. Format: YYYYMMDDHHMM<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |
| `three_ds_req_prior_ref` | `str` | Optional | This data element provides additional information to the ACS to determine the best approach for handing a request. This data element contains an ACS Transaction ID for a prior authenticated transaction. For example, the first recurring transaction that was authenticated with the cardholder. Length: 30 characters.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.three_ds_req_prior_auth_method import ThreeDsReqPriorAuthMethod
from adyen.models.three_ds_requestor_prior_authentication_info import ThreeDsRequestorPriorAuthenticationInfo

three_ds_requestor_prior_authentication_info = ThreeDsRequestorPriorAuthenticationInfo(
    three_ds_req_prior_auth_data='threeDSReqPriorAuthData4',
    three_ds_req_prior_auth_method=ThreeDsReqPriorAuthMethod.ENUM_03,
    three_ds_req_prior_auth_timestamp='threeDSReqPriorAuthTimestamp2',
    three_ds_req_prior_ref='threeDSReqPriorRef4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

