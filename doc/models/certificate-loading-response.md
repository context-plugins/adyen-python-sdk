
# Certificate Loading Response

## Structure

`CertificateLoadingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the communication session. |
| `installation_id` | `str` | Optional | The unique identifier of the SDK installation. If you create the [Terminal API](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/) transaction request on your backend, use this as the `POIID` in the `MessageHeader` of the request. |
| `merchant_account` | `str` | Optional | The unique identifier of your merchant account. |
| `sdk_data` | `str` | Optional | The data that the SDK uses to authenticate responses from the Adyen payments platform. Pass this value to your POS app. |
| `store` | `str` | Optional | The reference of the store that the transactions are processed for. |

## Example

```python
from adyen.models.certificate_loading_response import CertificateLoadingResponse

certificate_loading_response = CertificateLoadingResponse(
    id='id2',
    installation_id='installationId8',
    merchant_account='merchantAccount4',
    sdk_data='sdkData8',
    store='store2'
)
```

