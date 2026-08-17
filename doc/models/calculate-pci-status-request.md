
# Calculate Pci Status Request

## Structure

`CalculatePciStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_sales_channels` | [`List[AdditionalSalesChannelEnum]`](../../doc/models/additional-sales-channel-enum.md) | Optional | An array of additional sales channels to generate PCI questionnaires. Include the relevant sales channels if you need your user to sign PCI questionnaires. Not required if you [create stores](https://docs.adyen.com/platforms) and [add payment methods](https://docs.adyen.com/adyen-for-platforms-model) before you generate the questionnaires.<br><br>Possible values:<br><br>* **eCommerce**<br>* **pos**<br>* **ecomMoto**<br>* **posMoto** |

## Example

```python
from adyen.models.additional_sales_channel_enum import AdditionalSalesChannelEnum
from adyen.models.calculate_pci_status_request import CalculatePciStatusRequest

calculate_pci_status_request = CalculatePciStatusRequest(
    additional_sales_channels=[
        AdditionalSalesChannelEnum.ECOMMERCE,
        AdditionalSalesChannelEnum.ECOMMOTO,
        AdditionalSalesChannelEnum.POS
    ]
)
```

