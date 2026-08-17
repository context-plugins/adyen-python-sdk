
# Request Activation Response

## Structure

`RequestActivationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Optional | The unique identifier of the company account. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant account you requested to activate. |

## Example

```python
from adyen.models.request_activation_response import RequestActivationResponse

request_activation_response = RequestActivationResponse(
    company_id='companyId0',
    merchant_id='merchantId6'
)
```

