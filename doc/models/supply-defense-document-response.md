
# Supply Defense Document Response

## Structure

`SupplyDefenseDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_service_result` | [`DisputeServiceResult1`](../../doc/models/dispute-service-result-1.md) | Required | The result of the dispute service. |

## Example

```python
from adyen.models.dispute_service_result_1 import DisputeServiceResult1
from adyen.models.supply_defense_document_response import SupplyDefenseDocumentResponse

supply_defense_document_response = SupplyDefenseDocumentResponse(
    dispute_service_result=DisputeServiceResult1(
        success=False,
        error_message='errorMessage8'
    )
)
```

