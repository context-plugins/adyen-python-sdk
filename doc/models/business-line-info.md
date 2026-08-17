
# Business Line Info

## Structure

`BusinessLineInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `industry_code` | `str` | Required | A code that represents the industry of the legal entity for [marketplaces](https://docs.adyen.com/marketplaces/verification-requirements/reference-additional-products/#list-industry-codes) or [platforms](https://docs.adyen.com/platforms/verification-requirements/reference-additional-products/#list-industry-codes). For example, **4431A** for computer software stores. |
| `industry_code_description` | `str` | Optional, Read-only | The description of the industry code. |
| `legal_entity_id` | `str` | Required | Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line. |
| `sales_channels` | `List[str]` | Optional | A list of channels where goods or services are sold.<br><br>Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.<br><br>Required only in combination with the `service` **paymentProcessing**. |
| `service` | [`ServiceEnum`](../../doc/models/service-enum.md) | Required | The service for which you are creating the business line.<br><br>Possible values:<br><br>* **paymentProcessing**<br>* **issuing**<br>* **banking** |
| `source_of_funds` | [`SourceOfFunds11`](../../doc/models/source-of-funds-11.md) | Optional | Contains information about the source of your user's funds. Required only if the `service` is **banking** or **issuing**. |
| `web_data` | [`List[WebData]`](../../doc/models/web-data.md) | Optional | List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the `webDataExemption` object. |
| `web_data_exemption` | [`WebDataExemption1`](../../doc/models/web-data-exemption-1.md) | Optional | The reason why the web data is not provided. |

## Example

```python
import dateutil.parser

from adyen.models.business_line_info import BusinessLineInfo
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.reason_3_enum import Reason3Enum
from adyen.models.service_enum import ServiceEnum
from adyen.models.source_of_funds_11 import SourceOfFunds11
from adyen.models.web_data import WebData
from adyen.models.web_data_exemption_1 import WebDataExemption1

business_line_info = BusinessLineInfo(
    industry_code='industryCode0',
    legal_entity_id='legalEntityId6',
    service=ServiceEnum.PAYMENTPROCESSING,
    sales_channels=[
        'salesChannels2',
        'salesChannels3',
        'salesChannels4'
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
    ],
    web_data_exemption=WebDataExemption1(
        reason=Reason3Enum.NOONLINEPRESENCE
    )
)
```

