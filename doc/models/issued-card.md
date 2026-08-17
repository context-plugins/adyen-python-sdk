
# Issued Card

## Structure

`IssuedCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_type` | `str` | Optional | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** |
| `pan_entry_mode` | [`PanEntryModeEnum`](../../doc/models/pan-entry-mode-enum.md) | Optional | Indicates the method used for entering the PAN to initiate a transaction.<br><br>Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**. |
| `processing_type` | [`ProcessingType1Enum`](../../doc/models/processing-type-1-enum.md) | Optional | Contains information about how the payment was processed.<br><br>Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**, **recurring**, **token**. |
| `relayed_authorisation_data` | [`RelayedAuthorisationData2`](../../doc/models/relayed-authorisation-data-2.md) | Optional | If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server. |
| `scheme_trace_id` | `str` | Optional | The identifier of the original payment. This ID is provided by the scheme and can be alphanumeric or numeric, depending on the scheme. The `schemeTraceID` should refer to an original `schemeUniqueTransactionID` provided in an earlier payment (not necessarily processed by Adyen). A `schemeTraceId` is typically available for authorization adjustments or recurring payments. |
| `scheme_unique_transaction_id` | `str` | Optional | The unique identifier created by the scheme. This ID can be alphanumeric or numeric depending on the scheme. |
| `three_d_secure` | [`ThreeDSecure2`](../../doc/models/three-d-secure-2.md) | Optional | The data of the result from the 3DS authentication. |
| `mtype` | [`Type511Enum`](../../doc/models/type-511-enum.md) | Optional | **issuedCard**<br><br>**Default**: `"issuedCard"` |
| `validation_facts` | [`List[TransferNotificationValidationFact]`](../../doc/models/transfer-notification-validation-fact.md) | Optional | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. |

## Example

```python
from adyen.models.issued_card import IssuedCard
from adyen.models.pan_entry_mode_enum import PanEntryModeEnum
from adyen.models.processing_type_1_enum import ProcessingType1Enum
from adyen.models.relayed_authorisation_data_2 import RelayedAuthorisationData2
from adyen.models.type_511_enum import Type511Enum

issued_card = IssuedCard(
    authorisation_type='authorisationType4',
    pan_entry_mode=PanEntryModeEnum.TOKEN,
    processing_type=ProcessingType1Enum.POS,
    relayed_authorisation_data=RelayedAuthorisationData2(
        metadata={
            'key0': 'metadata9',
            'key1': 'metadata8'
        },
        reference='reference8'
    ),
    scheme_trace_id='schemeTraceId4',
    mtype=Type511Enum.ISSUEDCARD
)
```

