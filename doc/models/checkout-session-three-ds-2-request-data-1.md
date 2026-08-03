
# Checkout Session Three Ds 2 Request Data 1

Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments).

*This model accepts additional fields of type Any.*

## Structure

`CheckoutSessionThreeDs2RequestData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `home_phone` | [`HomePhone`](../../doc/models/home-phone.md) | Optional | - |
| `mobile_phone` | [`MobilePhone`](../../doc/models/mobile-phone.md) | Optional | - |
| `three_ds_requestor_challenge_ind` | [`ThreeDsRequestorChallengeInd`](../../doc/models/three-ds-requestor-challenge-ind.md) | Optional | - |
| `work_phone` | [`WorkPhone`](../../doc/models/work-phone.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_session_three_ds_2_request_data_1 import CheckoutSessionThreeDs2RequestData1
from adyen.models.home_phone import HomePhone
from adyen.models.mobile_phone import MobilePhone
from adyen.models.three_ds_requestor_challenge_ind import ThreeDsRequestorChallengeInd
from adyen.models.work_phone import WorkPhone

checkout_session_three_ds_2_request_data_1 = CheckoutSessionThreeDs2RequestData1(
    home_phone=HomePhone(
        cc='cc0',
        subscriber='subscriber2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mobile_phone=MobilePhone(
        cc='cc4',
        subscriber='subscriber6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    three_ds_requestor_challenge_ind=ThreeDsRequestorChallengeInd.ENUM_03,
    work_phone=WorkPhone(
        cc='cc2',
        subscriber='subscriber4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

