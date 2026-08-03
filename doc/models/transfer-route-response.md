
# Transfer Route Response

*This model accepts additional fields of type Any.*

## Structure

`TransferRouteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_routes` | [`List[TransferRoute]`](../../doc/models/transfer-route.md) | Optional | List of available priorities for a transfer, along with requirements. Use this information to initiate a transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType
from adyen.models.category_2 import Category2
from adyen.models.priority_2 import Priority2
from adyen.models.transfer_route import TransferRoute
from adyen.models.transfer_route_response import TransferRouteResponse
from adyen.models.type_610 import Type610

transfer_route_response = TransferRouteResponse(
    transfer_routes=[
        TransferRoute(
            category=Category2.TOPUP,
            country='country4',
            currency='currency0',
            priority=Priority2.INSTANT,
            requirements=[
                AdditionalBankIdentificationRequirement(
                    mtype=Type610.ADDITIONALBANKIDENTIFICATIONREQUIREMENT,
                    additional_bank_identification_type=AdditionalBankIdentificationType.GBSORTCODE,
                    description='description8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
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

