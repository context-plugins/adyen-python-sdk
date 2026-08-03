
# Calculate Pci Status Request

*This model accepts additional fields of type Any.*

## Structure

`CalculatePciStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_sales_channels` | [`List[AdditionalSalesChannel]`](../../doc/models/additional-sales-channel.md) | Optional | An array of additional sales channels to generate PCI questionnaires. Include the relevant sales channels if you need your user to sign PCI questionnaires. Not required if you [create stores](https://docs.adyen.com/platforms) and [add payment methods](https://docs.adyen.com/adyen-for-platforms-model) before you generate the questionnaires.<br><br>Possible values:<br><br>* **eCommerce**<br>* **pos**<br>* **ecomMoto**<br>* **posMoto** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_sales_channel import AdditionalSalesChannel
from adyen.models.calculate_pci_status_request import CalculatePciStatusRequest

calculate_pci_status_request = CalculatePciStatusRequest(
    additional_sales_channels=[
        AdditionalSalesChannel.ECOMMERCE,
        AdditionalSalesChannel.ECOMMOTO,
        AdditionalSalesChannel.POS
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

