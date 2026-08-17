
# Pay to Response Info 1

**payto** details

## Structure

`PayToResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Optional | Merchant name displayed to the shopper in the Agreements |
| `pay_to_purpose` | `str` | Optional | Represents the purpose of the Agreements created, it relates to the business type<br>**Allowed values**: mortgage, utility, loan, gambling, retail, salary, personal, government, pension, tax, other |

## Example

```python
from adyen.models.pay_to_response_info_1 import PayToResponseInfo1

pay_to_response_info_1 = PayToResponseInfo1(
    merchant_name='merchantName4',
    pay_to_purpose='payToPurpose0'
)
```

