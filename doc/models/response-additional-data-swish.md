
# Response Additional Data Swish

## Structure

`ResponseAdditionalDataSwish`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_payer_alias` | `str` | Optional | A Swish shopper's telephone number. |

## Example

```python
from adyen.models.response_additional_data_swish import ResponseAdditionalDataSwish

response_additional_data_swish = ResponseAdditionalDataSwish(
    swish_payer_alias='swish.payerAlias0'
)
```

