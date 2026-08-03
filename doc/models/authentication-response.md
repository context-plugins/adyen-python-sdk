
# Authentication Response

In 3D Secure 2, this is the `transStatus` from the challenge result. If the transaction was frictionless, omit this parameter.

## Enumeration

`AuthenticationResponse`

## Fields

| Name |
|  --- |
| `Y` |
| `N` |
| `U` |
| `A` |

## Example

```python
from adyen.models.authentication_response import AuthenticationResponse

authentication_response = AuthenticationResponse.Y
```

