
# Donation Flow 1 Enum

The interaction flow for in-person donations. Possible values:

- **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the donation.

- **twoStep**: The shopper presents their payment method twice: after the payment and after the donation.

## Enumeration

`DonationFlow1Enum`

## Fields

| Name |
|  --- |
| `ONESTEP` |
| `TWOSTEP` |

## Example

```python
from adyen.models.donation_flow_1_enum import DonationFlow1Enum

donation_flow_1 = DonationFlow1Enum.ONESTEP
```

