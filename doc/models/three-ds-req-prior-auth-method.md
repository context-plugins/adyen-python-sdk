
# Three Ds Req Prior Auth Method

Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values:

* **01** — Frictionless authentication occurred by ACS.
* **02** — Cardholder challenge occurred by ACS.
* **03** — AVS verified.
* **04** — Other issuer methods.

## Enumeration

`ThreeDsReqPriorAuthMethod`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |
| `ENUM_04` |

## Example

```python
from adyen.models.three_ds_req_prior_auth_method import ThreeDsReqPriorAuthMethod

three_ds_req_prior_auth_method = ThreeDsReqPriorAuthMethod.ENUM_03
```

