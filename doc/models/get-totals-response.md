
# Get Totals Response

Content of the Reconciliation Response message.
It conveys Information related to the Reconciliation transaction processed by the POI System.

*This model accepts additional fields of type Any.*

## Structure

`GetTotalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `poi_reconciliation_id` | `int` | Required | Identification of the reconciliation period between Sale and POI. |
| `transaction_totals` | [`List[TransactionTotals]`](../../doc/models/transaction-totals.md) | Optional | Result of the Sale to POI Reconciliation processing.<br>If `Response.Result` is Success. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.get_totals_response import GetTotalsResponse
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.transaction_totals import TransactionTotals

get_totals_response = GetTotalsResponse(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_reconciliation_id=222,
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
        ),
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
        ),
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

