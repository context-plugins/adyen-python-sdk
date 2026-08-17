
# Three D Directory Server Response Enum

3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service. Possible values:

* Y (Authentication available)
* N (Card holder not enrolled/not participating)
* U (Unable to authenticate)

## Enumeration

`ThreeDDirectoryServerResponseEnum`

## Fields

| Name |
|  --- |
| `N` |
| `U` |
| `Y` |

## Example

```python
from adyen.models.three_d_directory_server_response_enum import ThreeDDirectoryServerResponseEnum

three_d_directory_server_response = ThreeDDirectoryServerResponseEnum.N
```

