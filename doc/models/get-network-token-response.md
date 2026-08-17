
# Get Network Token Response

## Structure

`GetNetworkTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | [`NetworkToken2`](../../doc/models/network-token-2.md) | Required | The details of the network token. |

## Example

```python
import dateutil.parser

from adyen.models.device_info_1 import DeviceInfo1
from adyen.models.get_network_token_response import GetNetworkTokenResponse
from adyen.models.network_token_2 import NetworkToken2
from adyen.models.phone_info_2 import PhoneInfo2

get_network_token_response = GetNetworkTokenResponse(
    token=NetworkToken2(
        brand_variant='brandVariant8',
        creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        device=DeviceInfo1(
            form_factor='formFactor4',
            os_name='osName6',
            phone=PhoneInfo2(
                hashed_number='hashedNumber2',
                last_four_digits='lastFourDigits8',
                number='number8'
            )
        ),
        id='id6',
        payment_instrument_id='paymentInstrumentId8'
    )
)
```

