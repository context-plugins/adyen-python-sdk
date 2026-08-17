
# Amounts Resp

## Structure

`AmountsResp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `authorized_amount` | `float` | Required | Amount requested by the Sale for the payment.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `total_rebates_amount` | `float` | Optional | Sum of rebates in amount (total amount or line item amount) for all the loyalty programs.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `total_fees_amount` | `float` | Optional | Total amount of financial fees.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `cash_back_amount` | `float` | Optional | The cash-back part of the amount requested by the Sale for the payment.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `tip_amount` | `float` | Optional | Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |

## Example

```python
from adyen.models.amounts_resp import AmountsResp

amounts_resp = AmountsResp(
    authorized_amount=164.54,
    currency='Currency6',
    total_rebates_amount=88.78,
    total_fees_amount=106.18,
    cash_back_amount=237.84,
    tip_amount=200.3
)
```

