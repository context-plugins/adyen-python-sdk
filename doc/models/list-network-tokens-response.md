
# List Network Tokens Response

*This model accepts additional fields of type Any.*

## Structure

`ListNetworkTokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_tokens` | [`List[NetworkToken]`](../../doc/models/network-token.md) | Optional | List of network tokens. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.device_info import DeviceInfo
from adyen.models.list_network_tokens_response import ListNetworkTokensResponse
from adyen.models.network_token import NetworkToken
from adyen.models.phone_info import PhoneInfo

list_network_tokens_response = ListNetworkTokensResponse(
    network_tokens=[
        NetworkToken(
            brand_variant='brandVariant8',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            device=DeviceInfo(
                form_factor='formFactor4',
                os_name='osName6',
                phone=PhoneInfo(
                    hashed_number='hashedNumber2',
                    last_four_digits='lastFourDigits8',
                    number='number8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id6',
            payment_instrument_id='paymentInstrumentId8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        NetworkToken(
            brand_variant='brandVariant8',
            creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            device=DeviceInfo(
                form_factor='formFactor4',
                os_name='osName6',
                phone=PhoneInfo(
                    hashed_number='hashedNumber2',
                    last_four_digits='lastFourDigits8',
                    number='number8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id6',
            payment_instrument_id='paymentInstrumentId8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

