
# Cancel or Refund Request

## Structure

`CancelOrRefundRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular modification request.<br><br>The additionalData object consists of entries, each of which includes the key and value. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `mpi_data` | [`ThreeDSecureData`](../../doc/models/three-d-secure-data.md) | Optional | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). |
| `original_merchant_reference` | `str` | Optional | The original merchant reference to cancel. |
| `original_reference` | `str` | Required | The original pspReference of the payment to modify.<br>This reference is returned in:<br><br>* authorisation response<br>* authorisation notification |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |
| `tender_reference` | `str` | Optional | The transaction reference provided by the PED. For point-of-sale integrations only. |
| `unique_terminal_id` | `str` | Optional | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. |

## Example

```python
from adyen.models.authentication_response_enum import AuthenticationResponseEnum
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.cancel_or_refund_request import CancelOrRefundRequest
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.directory_response_enum import DirectoryResponseEnum
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic
from adyen.models.three_d_secure_data import ThreeDSecureData

cancel_or_refund_request = CancelOrRefundRequest(
    merchant_account='merchantAccount4',
    original_reference='originalReference4',
    additional_data={
        'key0': 'additionalData2',
        'key1': 'additionalData3',
        'key2': 'additionalData4'
    },
    mpi_data=ThreeDSecureData(
        authentication_response=AuthenticationResponseEnum.U,
        cavv='cavv0',
        cavv_algorithm='cavvAlgorithm0',
        challenge_cancel=ChallengeCancelEnum.ENUM_07,
        directory_response=DirectoryResponseEnum.U
    ),
    original_merchant_reference='originalMerchantReference6',
    platform_chargeback_logic=PlatformChargebackLogic(
        behavior=BehaviorEnum.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6'
    ),
    reference='reference2'
)
```

