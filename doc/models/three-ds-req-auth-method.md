
# Three Ds Req Auth Method

Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values:

* **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest).
* **02** — Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials.
* **03** — Login to the cardholder account at the 3DS Requestor system using federated ID.
* **04** — Login to the cardholder account at the 3DS Requestor system using issuer credentials.
* **05** — Login to the cardholder account at the 3DS Requestor system using third-party authentication.
* **06** — Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator.

## Enumeration

`ThreeDsReqAuthMethod`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |
| `ENUM_05` |
| `ENUM_06` |

## Example

```python
from adyen.models.three_ds_req_auth_method import ThreeDsReqAuthMethod

three_ds_req_auth_method = ThreeDsReqAuthMethod.ENUM_01
```

