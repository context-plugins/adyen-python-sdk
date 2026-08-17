
# Reconciliation Response 2

Content of the Reconciliation Response message.

## Structure

`ReconciliationResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `reconciliation_type` | [`ReconciliationType1Enum`](../../doc/models/reconciliation-type-1-enum.md) | Required | Type of Reconciliation requested by the Sale to the POI.<br>Possible values:<br><br>* **AcquirerReconciliation**<br>* **AcquirerSynchronisation**<br>* **PreviousReconciliation**<br>* **SaleReconciliation** |
| `poi_reconciliation_id` | `int` | Optional | Identification of the reconciliation period between Sale and POI.<br>Absent if ReconciliationType is `AcquirerReconciliation`. |
| `transaction_totals` | [`List[TransactionTotals]`](../../doc/models/transaction-totals.md) | Optional | Result of the Sale to POI Reconciliation processing.<br>If `Response.Result` is Success. |

## Example

```python
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.reconciliation_response_2 import ReconciliationResponse2
from adyen.models.reconciliation_type_1_enum import ReconciliationType1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.transaction_totals import TransactionTotals

reconciliation_response_2 = ReconciliationResponse2(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    reconciliation_type=ReconciliationType1Enum.ACQUIRERRECONCILIATION,
    poi_reconciliation_id=196,
    transaction_totals=[
        TransactionTotals(
            payment_instrument_type=PaymentInstrumentType11Enum.MOBILE,
            acquirer_id=138,
            host_reconciliation_id='HostReconciliationID4',
            card_brand='CardBrand8',
            poiid='POIID6',
            sale_id='SaleID2'
        ),
        TransactionTotals(
            payment_instrument_type=PaymentInstrumentType11Enum.MOBILE,
            acquirer_id=138,
            host_reconciliation_id='HostReconciliationID4',
            card_brand='CardBrand8',
            poiid='POIID6',
            sale_id='SaleID2'
        )
    ]
)
```

