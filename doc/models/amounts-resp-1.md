
# Amounts Resp 1

Various amounts related to the payment response from the POI System. Amounts approved by the POI and the Acquirer for the payment and loyalty transaction, containing:

* The authorised amount to be paid.
* The amount of the rebates.
* The amount of financial fees.
* The cash back part of the requested amount for a payment with cash back.
* The tip part of the requested amount for a payment with tip.

## Structure

`AmountsResp1`

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
from adyen.models.amounts_resp_1 import AmountsResp1

amounts_resp_1 = AmountsResp1(
    authorized_amount=121.46,
    currency='Currency8',
    total_rebates_amount=131.86,
    total_fees_amount=63.1,
    cash_back_amount=194.76,
    tip_amount=157.22
)
```

