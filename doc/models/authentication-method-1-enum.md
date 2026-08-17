
# Authentication Method 1 Enum

## Enumeration

`AuthenticationMethod1Enum`

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
from adyen.models.authentication_method_1_enum import AuthenticationMethod1Enum

authentication_method_1 = AuthenticationMethod1Enum.PAPERSIGNATURE
```

