
# Three DS Requestor Authentication Info

Information about how the 3DS Requestor authenticated the cardholder before or during the transaction

## Structure

`ThreeDSRequestorAuthenticationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_ds_req_auth_data` | `str` | Optional | Data that documents and supports a specific authentication process. Maximum length: 2048 bytes. |
| `three_ds_req_auth_method` | [`ThreeDSReqAuthMethodEnum`](../../doc/models/three-ds-req-auth-method-enum.md) | Optional | Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values:<br><br>* **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest).<br>* **02** — Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials.<br>* **03** — Login to the cardholder account at the 3DS Requestor system using federated ID.<br>* **04** — Login to the cardholder account at the 3DS Requestor system using issuer credentials.<br>* **05** — Login to the cardholder account at the 3DS Requestor system using third-party authentication.<br>* **06** — Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `three_ds_req_auth_timestamp` | `str` | Optional | Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `12` |

## Example

```python
from adyen.models.three_ds_req_auth_method_enum import ThreeDSReqAuthMethodEnum
from adyen.models.three_ds_requestor_authentication_info import ThreeDSRequestorAuthenticationInfo

three_ds_requestor_authentication_info = ThreeDSRequestorAuthenticationInfo(
    three_ds_req_auth_data='threeDSReqAuthData2',
    three_ds_req_auth_method=ThreeDSReqAuthMethodEnum.ENUM_03,
    three_ds_req_auth_timestamp='threeDSReqAuthTimestamp6'
)
```

