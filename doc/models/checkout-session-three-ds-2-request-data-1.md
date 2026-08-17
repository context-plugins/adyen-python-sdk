
# Checkout Session Three DS 2 Request Data 1

Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments).

## Structure

`CheckoutSessionThreeDS2RequestData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `home_phone` | [`Phone3`](../../doc/models/phone-3.md) | Optional | The home phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |
| `mobile_phone` | [`Phone1`](../../doc/models/phone-1.md) | Optional | The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |
| `three_ds_requestor_challenge_ind` | [`ThreeDSRequestorChallengeIndEnum`](../../doc/models/three-ds-requestor-challenge-ind-enum.md) | Optional | Indicates whether a challenge is requested for this transaction. Possible values:<br><br>* **01** — No preference<br>* **02** — No challenge requested<br>* **03** — Challenge requested (3DS Requestor preference)<br>* **04** — Challenge requested (Mandate)<br>* **05** — No challenge (transactional risk analysis is already performed)<br>* **06** — Data Only |
| `work_phone` | [`Phone2`](../../doc/models/phone-2.md) | Optional | The work phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |

## Example

```python
from adyen.models.checkout_session_three_ds_2_request_data_1 import CheckoutSessionThreeDS2RequestData1
from adyen.models.phone_1 import Phone1
from adyen.models.phone_2 import Phone2
from adyen.models.phone_3 import Phone3
from adyen.models.three_ds_requestor_challenge_ind_enum import ThreeDSRequestorChallengeIndEnum

checkout_session_three_ds_2_request_data_1 = CheckoutSessionThreeDS2RequestData1(
    home_phone=Phone3(
        cc='cc0',
        subscriber='subscriber2'
    ),
    mobile_phone=Phone1(
        cc='cc4',
        subscriber='subscriber6'
    ),
    three_ds_requestor_challenge_ind=ThreeDSRequestorChallengeIndEnum.ENUM_03,
    work_phone=Phone2(
        cc='cc2',
        subscriber='subscriber4'
    )
)
```

