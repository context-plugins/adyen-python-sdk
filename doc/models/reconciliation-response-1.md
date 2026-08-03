
# Reconciliation Response 1

*This model accepts additional fields of type Any.*

## Structure

`ReconciliationResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `reconciliation_type` | [`ReconciliationType1`](../../doc/models/reconciliation-type-1.md) | Required | - |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>Absent if ReconciliationType is `AcquirerReconciliation`. |
| `transaction_totals` | [`List[TransactionTotals]`](../../doc/models/transaction-totals.md) | Optional | Result of the Sale to POI Reconciliation processing.<br>If `Response.Result` is Success. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.reconciliation_response_1 import ReconciliationResponse1
from adyen.models.reconciliation_type_1 import ReconciliationType1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.transaction_totals import TransactionTotals

reconciliation_response_1 = ReconciliationResponse1(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reconciliation_type=ReconciliationType1.SALERECONCILIATION,
    poi_reconciliation_id=162,
    transaction_totals=[
        TransactionTotals(
            payment_instrument_type=PaymentInstrumentType11.MOBILE,
            acquirer_id=138,
            host_reconciliation_id='HostReconciliationID4',
            card_brand='CardBrand8',
            poiid='POIID6',
            sale_id='SaleID2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

