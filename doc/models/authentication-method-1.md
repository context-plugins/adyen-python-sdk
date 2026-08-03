
# Authentication Method 1

## Enumeration

`AuthenticationMethod1`

## Fields

| Name |
|  --- |
| `BYPASS` |
| `MANUALVERIFICATION` |
| `MERCHANTAUTHENTICATION` |
| `OFFLINEPIN` |
| `ONLINEPIN` |
| `PAPERSIGNATURE` |
| `SECUREDCHANNEL` |
| `SECURECERTIFICATE` |
| `SECURENOCERTIFICATE` |
| `SIGNATURECAPTURE` |
| `UNKNOWNMETHOD` |

## Example

```python
from adyen.models.authentication_method_1 import AuthenticationMethod1

authentication_method_1 = AuthenticationMethod1.PAPERSIGNATURE
```

