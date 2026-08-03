
# Donation Request

*This model accepts additional fields of type Any.*

## Structure

`DonationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `donation_account` | `str` | Required | The Adyen account name of the charity. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `modification_amount` | [`ModificationAmount`](../../doc/models/modification-amount.md) | Required | - |
| `original_reference` | `str` | Optional | The original pspReference of the payment to modify.<br>This reference is returned in:<br><br>* authorisation response<br>* authorisation notification |
| `platform_chargeback_logic` | [`PlatformChargebackLogic1`](../../doc/models/platform-chargeback-logic-1.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.behavior import Behavior
from adyen.models.donation_request import DonationRequest
from adyen.models.modification_amount import ModificationAmount
from adyen.models.platform_chargeback_logic_1 import PlatformChargebackLogic1

donation_request = DonationRequest(
    donation_account='donationAccount6',
    merchant_account='merchantAccount4',
    modification_amount=ModificationAmount(
        currency='currency6',
        value=92,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    original_reference='originalReference4',
    platform_chargeback_logic=PlatformChargebackLogic1(
        behavior=Behavior.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

