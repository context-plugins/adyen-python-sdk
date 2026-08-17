
# Three DS Request Data

## Structure

`ThreeDSRequestData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `challenge_window_size` | [`ChallengeWindowSizeEnum`](../../doc/models/challenge-window-size-enum.md) | Optional | Dimensions of the 3DS2 challenge window to be displayed to the cardholder.<br><br>Possible values:<br><br>* **01** - size of 250x400<br>* **02** - size of 390x400<br>* **03** - size of 500x600<br>* **04** - size of 600x400<br>* **05** - Fullscreen |
| `data_only` | [`DataOnlyEnum`](../../doc/models/data-only-enum.md) | Optional | Required to trigger the [data-only flow](https://docs.adyen.com/online-payments/3d-secure/data-only/). When set to **true**, forces the 3D Secure 2 data-only flow for all transactions where it is possible. |
| `native_three_ds` | [`NativeThreeDSEnum`](../../doc/models/native-three-ds-enum.md) | Optional | Indicates if [native 3D Secure authentication](https://docs.adyen.com/online-payments/3d-secure/native-3ds2) should be triggered when available. Adyen can still select to fallback to the redirect flow to optimize authorization rates and improve the shopper's experience.<br><br>Possible values:<br><br>* **preferred**: Use native 3D Secure authentication when available.<br>* **disabled**: Use the redirect 3D Secure authentication flow. |
| `three_ds_version` | [`ThreeDSVersionEnum`](../../doc/models/three-ds-version-enum.md) | Optional | The version of 3D Secure to use.<br><br>Possible values:<br><br>* **2.1.0**<br>* **2.2.0** |

## Example

```python
from adyen.models.challenge_window_size_enum import ChallengeWindowSizeEnum
from adyen.models.data_only_enum import DataOnlyEnum
from adyen.models.native_three_ds_enum import NativeThreeDSEnum
from adyen.models.three_ds_request_data import ThreeDSRequestData
from adyen.models.three_ds_version_enum import ThreeDSVersionEnum

three_ds_request_data = ThreeDSRequestData(
    challenge_window_size=ChallengeWindowSizeEnum.ENUM_03,
    data_only=DataOnlyEnum.FALSE,
    native_three_ds=NativeThreeDSEnum.PREFERRED,
    three_ds_version=ThreeDSVersionEnum.ENUM_210
)
```

