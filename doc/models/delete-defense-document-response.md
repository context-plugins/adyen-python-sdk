
# Delete Defense Document Response

## Structure

`DeleteDefenseDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_service_result` | [`DisputeServiceResult1`](../../doc/models/dispute-service-result-1.md) | Required | The result of the dispute service. |

## Example

```python
from adyen.models.delete_defense_document_response import DeleteDefenseDocumentResponse
from adyen.models.dispute_service_result_1 import DisputeServiceResult1

delete_defense_document_response = DeleteDefenseDocumentResponse(
    dispute_service_result=DisputeServiceResult1(
        success=False,
        error_message='errorMessage8'
    )
)
```

