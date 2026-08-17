
# Pay to Response Info

## Structure

`PayToResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Merchant name displayed to the shopper in the Agreements |
| `pay_to_purpose` | `str` | Optional | Represents the purpose of the Agreements created, it relates to the business type<br>**Allowed values**: mortgage, utility, loan, gambling, retail, salary, personal, government, pension, tax, other |

## Example

```python
from adyen.models.pay_to_response_info import PayToResponseInfo

pay_to_response_info = PayToResponseInfo(
    merchant_name='merchantName6',
    pay_to_purpose='payToPurpose2'
)
```

