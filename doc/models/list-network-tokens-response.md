
# List Network Tokens Response

## Structure

`ListNetworkTokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_tokens` | [`List[NetworkToken]`](../../doc/models/network-token.md) | Optional | List of network tokens. |

## Example

```python
import dateutil.parser

from adyen.models.device_info_1 import DeviceInfo1
from adyen.models.list_network_tokens_response import ListNetworkTokensResponse
from adyen.models.network_token import NetworkToken
from adyen.models.phone_info_2 import PhoneInfo2

list_network_tokens_response = ListNetworkTokensResponse(
    network_tokens=[
        NetworkToken(
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
        ),
        NetworkToken(
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
    ]
)
```

