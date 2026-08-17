
# Three DS Req Prior Auth Method Enum

Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values:

* **01** — Frictionless authentication occurred by ACS.
* **02** — Cardholder challenge occurred by ACS.
* **03** — AVS verified.
* **04** — Other issuer methods.

## Enumeration

`ThreeDSReqPriorAuthMethodEnum`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |

## Example

```python
from adyen.models.three_ds_req_prior_auth_method_enum import ThreeDSReqPriorAuthMethodEnum

three_ds_req_prior_auth_method = ThreeDSReqPriorAuthMethodEnum.ENUM_03
```

