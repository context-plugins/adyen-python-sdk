
# Pay to Info

## Structure

`PayToInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Required | Merchant name displayed to the shopper in the Agreements |
| `pay_to_purpose` | `str` | Required | Represents the purpose of the Agreements created, it relates to the business type<br>**Allowed values**: mortgage, utility, loan, gambling, retail, salary, personal, government, pension, tax, other |

## Example

```python
from adyen.models.pay_to_info import PayToInfo

pay_to_info = PayToInfo(
    merchant_name='merchantName2',
    pay_to_purpose='payToPurpose2'
)
```

