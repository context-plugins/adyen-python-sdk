
# Create Session Response

*This model accepts additional fields of type Any.*

## Structure

`CreateSessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the session. |
| `installation_id` | `str` | Optional | The unique identifier of the SDK installation. If you create the [Terminal API](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/) transaction request on your backend, use this as the `POIID` in the `MessageHeader` of the request. |
| `merchant_account` | `str` | Optional | The unique identifier of your merchant account. |
| `sdk_data` | `str` | Optional | The data that the SDK uses to authenticate responses from the Adyen payments platform. Pass this value to your POS app. |
| `store` | `str` | Optional | The unique identifier of the store that you want to process transactions for. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_session_response import CreateSessionResponse

create_session_response = CreateSessionResponse(
    id='id8',
    installation_id='installationId6',
    merchant_account='merchantAccount0',
    sdk_data='sdkData2',
    store='store2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

