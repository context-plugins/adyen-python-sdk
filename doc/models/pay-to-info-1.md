
# Pay to Info 1

Details to provide if `type` is **payto**.

## Structure

`PayToInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_name` | `str` | Required | Merchant name displayed to the shopper in the Agreements |
| `pay_to_purpose` | `str` | Required | Represents the purpose of the Agreements created, it relates to the business type<br>**Allowed values**: mortgage, utility, loan, gambling, retail, salary, personal, government, pension, tax, other |

## Example

```python
from adyen.models.pay_to_info_1 import PayToInfo1

pay_to_info_1 = PayToInfo1(
    merchant_name='merchantName8',
    pay_to_purpose='payToPurpose4'
)
```

