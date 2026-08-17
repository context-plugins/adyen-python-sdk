
# Donation Request

## Structure

`DonationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `donation_account` | `str` | Required | The Adyen account name of the charity. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `modification_amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount to be donated.The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount. |
| `original_reference` | `str` | Optional | The original pspReference of the payment to modify.<br>This reference is returned in:<br><br>* authorisation response<br>* authorisation notification |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.donation_request import DonationRequest
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic

donation_request = DonationRequest(
    donation_account='donationAccount6',
    merchant_account='merchantAccount4',
    modification_amount=Amount(
        currency='currency6',
        value=92
    ),
    original_reference='originalReference4',
    platform_chargeback_logic=PlatformChargebackLogic(
        behavior=BehaviorEnum.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6'
    ),
    reference='reference2'
)
```

