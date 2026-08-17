
# Response Additional Data Opi

## Structure

`ResponseAdditionalDataOpi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `opi_trans_token` | `str` | Optional | Returned in the response if you included `opi.includeTransToken: true` in an ecommerce payment request. This contains an Oracle Payment Interface token that you can store in your Oracle Opera database to identify tokenized ecommerce transactions. For more information and required settings, see [Oracle Opera](https://docs.adyen.com/plugins/oracle-opera#opi-token-ecommerce). |

## Example

```python
from adyen.models.response_additional_data_opi import ResponseAdditionalDataOpi

response_additional_data_opi = ResponseAdditionalDataOpi(
    opi_trans_token='opi.transToken4'
)
```

