
# Business Line Info Update

## Structure

`BusinessLineInfoUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `industry_code` | `str` | Optional | A code that represents the industry of your legal entity. For example, **4431A** for computer software stores. |
| `industry_code_description` | `str` | Optional, Read-only | The description of the industry code. |
| `sales_channels` | `List[str]` | Optional | A list of channels where goods or services are sold.<br><br>Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.<br><br>Required only in combination with the `service` **paymentProcessing**. |
| `source_of_funds` | [`SourceOfFunds11`](../../doc/models/source-of-funds-11.md) | Optional | Contains information about the source of your user's funds. Required only if the `service` is **banking** or **issuing**. |
| `web_data` | [`List[WebData]`](../../doc/models/web-data.md) | Optional | List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the `webDataExemption` object. |
| `web_data_exemption` | [`WebDataExemption1`](../../doc/models/web-data-exemption-1.md) | Optional | The reason why the web data is not provided. |

## Example

```python
import dateutil.parser

from adyen.models.business_line_info_update import BusinessLineInfoUpdate
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.source_of_funds_11 import SourceOfFunds11
from adyen.models.web_data import WebData

business_line_info_update = BusinessLineInfoUpdate(
    industry_code='industryCode8',
    sales_channels=[
        'salesChannels0',
        'salesChannels1'
    ],
    source_of_funds=SourceOfFunds11(
        adyen_processed_funds=False,
        amount=PatchableAmountDTO(
            currency='currency2',
            value=110
        ),
        asset_months_held=46,
        cryptocurrency_exchange='cryptocurrencyExchange2',
        date_of_funds_received=dateutil.parser.parse('2016-03-13').date(),
        date_of_source_event=dateutil.parser.parse('2016-03-13').date()
    ),
    web_data=[
        WebData(
            web_address='webAddress4'
        ),
        WebData(
            web_address='webAddress4'
        )
    ]
)
```

