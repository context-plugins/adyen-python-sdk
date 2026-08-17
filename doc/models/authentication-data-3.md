
# Authentication Data 3

Data for 3DS authentication.

## Structure

`AuthenticationData3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attempt_authentication` | [`AttemptAuthenticationEnum`](../../doc/models/attempt-authentication-enum.md) | Optional | Indicates when 3D Secure authentication should be attempted. This overrides all other rules, including [Dynamic 3D Secure settings](https://docs.adyen.com/risk-management/dynamic-3d-secure).<br><br>Possible values:<br><br>* **always**: Perform 3D Secure authentication.<br>* **never**: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require authentication, the transaction gets declined. |
| `authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.<br>Default: **false**.<br><br>**Default**: `False` |
| `three_ds_request_data` | [`ThreeDSRequestData2`](../../doc/models/three-ds-request-data-2.md) | Optional | Object with additional parameters for the 3D Secure authentication flow. |

## Example

```python
from adyen.models.attempt_authentication_enum import AttemptAuthenticationEnum
from adyen.models.authentication_data_3 import AuthenticationData3
from adyen.models.challenge_window_size_enum import ChallengeWindowSizeEnum
from adyen.models.data_only_enum import DataOnlyEnum
from adyen.models.native_three_ds_enum import NativeThreeDSEnum
from adyen.models.three_ds_request_data_2 import ThreeDSRequestData2
from adyen.models.three_ds_version_enum import ThreeDSVersionEnum

authentication_data_3 = AuthenticationData3(
    attempt_authentication=AttemptAuthenticationEnum.ALWAYS,
    authentication_only=False,
    three_ds_request_data=ThreeDSRequestData2(
        challenge_window_size=ChallengeWindowSizeEnum.ENUM_03,
        data_only=DataOnlyEnum.FALSE,
        native_three_ds=NativeThreeDSEnum.PREFERRED,
        three_ds_version=ThreeDSVersionEnum.ENUM_210
    )
)
```

