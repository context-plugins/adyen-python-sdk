
# Three DS Req Auth Method Enum

Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values:

* **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest).
* **02** — Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials.
* **03** — Login to the cardholder account at the 3DS Requestor system using federated ID.
* **04** — Login to the cardholder account at the 3DS Requestor system using issuer credentials.
* **05** — Login to the cardholder account at the 3DS Requestor system using third-party authentication.
* **06** — Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator., Indicates whether a challenge is requested for this transaction. Possible values:
* **01** — No preference
* **02** — No challenge requested
* **03** — Challenge requested (3DS Requestor preference)
* **04** — Challenge requested (Mandate)
* **05** — No challenge (transactional risk analysis is already performed)
* **06** — Data Only

## Enumeration

`ThreeDSReqAuthMethodEnum`

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
from adyen.models.three_ds_req_auth_method_enum import ThreeDSReqAuthMethodEnum

three_ds_req_auth_method = ThreeDSReqAuthMethodEnum.ENUM_01
```

