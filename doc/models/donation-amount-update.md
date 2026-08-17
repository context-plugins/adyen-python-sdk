
# Donation Amount Update

## Structure

`DonationAmountUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | `List[int]` | Optional | The donation amounts in minor units. The list must contain at least one amount and no more than three amounts.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `3` |
| `currency_code` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes).<br><br>**Constraints**: *Pattern*: `^[A-Z]{3}$` |

## Example

```python
from adyen.models.donation_amount_update import DonationAmountUpdate

donation_amount_update = DonationAmountUpdate(
    amounts=[
        204
    ],
    currency_code='currencyCode0'
)
```

