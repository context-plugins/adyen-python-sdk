
# Response Additional Data Domestic Error

## Structure

`ResponseAdditionalDataDomesticError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `domestic_refusal_reason_raw` | `str` | Optional | The reason the transaction was declined, given by the local issuer.<br>Currently available for merchants in Japan. |
| `domestic_shopper_advice` | `str` | Optional | The action the shopper should take, in a local language.<br>Currently available in Japanese, for merchants in Japan. |

## Example

```python
from adyen.models.response_additional_data_domestic_error import ResponseAdditionalDataDomesticError

response_additional_data_domestic_error = ResponseAdditionalDataDomesticError(
    domestic_refusal_reason_raw='domesticRefusalReasonRaw0',
    domestic_shopper_advice='domesticShopperAdvice2'
)
```

