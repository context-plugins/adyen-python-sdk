
# Transfer Route Response

## Structure

`TransferRouteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_routes` | [`List[TransferRoute]`](../../doc/models/transfer-route.md) | Optional | List of available priorities for a transfer, along with requirements. Use this information to initiate a transfer. |

## Example

```python
from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type_enum import AdditionalBankIdentificationTypeEnum
from adyen.models.category_2_enum import Category2Enum
from adyen.models.priority_2_enum import Priority2Enum
from adyen.models.transfer_route import TransferRoute
from adyen.models.transfer_route_response import TransferRouteResponse

transfer_route_response = TransferRouteResponse(
    transfer_routes=[
        TransferRoute(
            category=Category2Enum.TOPUP,
            country='country4',
            currency='currency0',
            priority=Priority2Enum.INSTANT,
            requirements=[
                AdditionalBankIdentificationRequirement(
                    additional_bank_identification_type=AdditionalBankIdentificationTypeEnum.GBSORTCODE,
                    description='description8'
                )
            ]
        )
    ]
)
```

