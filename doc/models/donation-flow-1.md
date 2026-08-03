
# Donation Flow 1

The interaction flow for in-person donations. Possible values:

- **oneStep**: The shopper presents their payment method for the payment and the donation in one go, after the donation.

- **twoStep**: The shopper presents their payment method twice: after the payment and after the donation.

## Enumeration

`DonationFlow1`

## Fields

| Name |
|  --- |
| `ONESTEP` |
| `TWOSTEP` |

## Example

```python
from adyen.models.donation_flow_1 import DonationFlow1

donation_flow_1 = DonationFlow1.ONESTEP
```

