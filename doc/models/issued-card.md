
# Issued Card

*This model accepts additional fields of type Any.*

## Structure

`IssuedCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_type` | `str` | Optional | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** |
| `pan_entry_mode` | [`PanEntryMode`](../../doc/models/pan-entry-mode.md) | Optional | - |
| `processing_type` | [`ProcessingType1`](../../doc/models/processing-type-1.md) | Optional | - |
| `relayed_authorisation_data` | [`RelayedAuthorisationData`](../../doc/models/relayed-authorisation-data.md) | Optional | - |
| `scheme_trace_id` | `str` | Optional | The identifier of the original payment. This ID is provided by the scheme and can be alphanumeric or numeric, depending on the scheme. The `schemeTraceID` should refer to an original `schemeUniqueTransactionID` provided in an earlier payment (not necessarily processed by Adyen). A `schemeTraceId` is typically available for authorization adjustments or recurring payments. |
| `scheme_unique_transaction_id` | `str` | Optional | The unique identifier created by the scheme. This ID can be alphanumeric or numeric depending on the scheme. |
| `three_d_secure` | [`ThreeDSecure`](../../doc/models/three-d-secure.md) | Optional | - |
| `mtype` | [`Type512`](../../doc/models/type-512.md) | Optional | - |
| `validation_facts` | [`List[TransferNotificationValidationFact]`](../../doc/models/transfer-notification-validation-fact.md) | Optional | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.issued_card import IssuedCard
from adyen.models.pan_entry_mode import PanEntryMode
from adyen.models.processing_type_1 import ProcessingType1
from adyen.models.relayed_authorisation_data import RelayedAuthorisationData

issued_card = IssuedCard(
    authorisation_type='authorisationType4',
    pan_entry_mode=PanEntryMode.TOKEN,
    processing_type=ProcessingType1.POS,
    relayed_authorisation_data=RelayedAuthorisationData(
        metadata={
            'key0': 'metadata9',
            'key1': 'metadata8'
        },
        reference='reference8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    scheme_trace_id='schemeTraceId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

