
# Void Pending Refund Request

## Structure

`VoidPendingRefundRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular modification request.<br><br>The additionalData object consists of entries, each of which includes the key and value. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `modification_amount` | [`Amount`](../../doc/models/amount.md) | Optional | The amount that needs to be captured/refunded. Required for `/capture` and `/refund`, not allowed for `/cancel`. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount. |
| `mpi_data` | [`ThreeDSecureData`](../../doc/models/three-d-secure-data.md) | Optional | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). |
| `original_merchant_reference` | `str` | Optional | The original merchant reference to cancel. |
| `original_reference` | `str` | Optional | The original pspReference of the payment to modify.<br>This reference is returned in:<br><br>* authorisation response<br>* authorisation notification |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to split payments for [platforms](https://docs.adyen.com/platforms/automatic-split-configuration/). |
| `tender_reference` | `str` | Optional | The transaction reference provided by the PED. For point-of-sale integrations only. |
| `unique_terminal_id` | `str` | Optional | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.authentication_response_enum import AuthenticationResponseEnum
from adyen.models.challenge_cancel_enum import ChallengeCancelEnum
from adyen.models.directory_response_enum import DirectoryResponseEnum
from adyen.models.three_d_secure_data import ThreeDSecureData
from adyen.models.void_pending_refund_request import VoidPendingRefundRequest

void_pending_refund_request = VoidPendingRefundRequest(
    merchant_account='merchantAccount2',
    additional_data={
        'key0': 'additionalData6'
    },
    modification_amount=Amount(
        currency='currency6',
        value=92
    ),
    mpi_data=ThreeDSecureData(
        authentication_response=AuthenticationResponseEnum.U,
        cavv='cavv0',
        cavv_algorithm='cavvAlgorithm0',
        challenge_cancel=ChallengeCancelEnum.ENUM_07,
        directory_response=DirectoryResponseEnum.U
    ),
    original_merchant_reference='originalMerchantReference0',
    original_reference='originalReference0'
)
```

