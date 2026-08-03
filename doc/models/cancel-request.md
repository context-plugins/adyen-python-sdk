
# Cancel Request

*This model accepts additional fields of type Any.*

## Structure

`CancelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular modification request.<br><br>The additionalData object consists of entries, each of which includes the key and value. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `mpi_data` | [`MpiData`](../../doc/models/mpi-data.md) | Optional | - |
| `original_merchant_reference` | `str` | Optional | The original merchant reference to cancel. |
| `original_reference` | `str` | Required | The original pspReference of the payment to modify.<br>This reference is returned in:<br><br>* authorisation response<br>* authorisation notification |
| `platform_chargeback_logic` | [`PlatformChargebackLogic1`](../../doc/models/platform-chargeback-logic-1.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to split payments for [platforms](https://docs.adyen.com/platforms/automatic-split-configuration/). |
| `tender_reference` | `str` | Optional | The transaction reference provided by the PED. For point-of-sale integrations only. |
| `unique_terminal_id` | `str` | Optional | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_response import AuthenticationResponse
from adyen.models.behavior import Behavior
from adyen.models.cancel_request import CancelRequest
from adyen.models.challenge_cancel import ChallengeCancel
from adyen.models.directory_response import DirectoryResponse
from adyen.models.mpi_data import MpiData
from adyen.models.platform_chargeback_logic_1 import PlatformChargebackLogic1

cancel_request = CancelRequest(
    merchant_account='merchantAccount6',
    original_reference='originalReference2',
    additional_data={
        'key0': 'additionalData4'
    },
    mpi_data=MpiData(
        authentication_response=AuthenticationResponse.U,
        cavv='cavv0',
        cavv_algorithm='cavvAlgorithm0',
        challenge_cancel=ChallengeCancel.ENUM_07,
        directory_response=DirectoryResponse.U,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    original_merchant_reference='originalMerchantReference8',
    platform_chargeback_logic=PlatformChargebackLogic1(
        behavior=Behavior.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

