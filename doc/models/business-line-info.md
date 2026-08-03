
# Business Line Info

*This model accepts additional fields of type Any.*

## Structure

`BusinessLineInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `industry_code` | `str` | Required | A code that represents the industry of the legal entity for [marketplaces](https://docs.adyen.com/marketplaces/verification-requirements/reference-additional-products/#list-industry-codes) or [platforms](https://docs.adyen.com/platforms/verification-requirements/reference-additional-products/#list-industry-codes). For example, **4431A** for computer software stores. |
| `industry_code_description` | `str` | Optional, Read-only | The description of the industry code. |
| `legal_entity_id` | `str` | Required | Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line. |
| `sales_channels` | `List[str]` | Optional | A list of channels where goods or services are sold.<br><br>Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.<br><br>Required only in combination with the `service` **paymentProcessing**. |
| `service` | [`Service`](../../doc/models/service.md) | Required | - |
| `source_of_funds` | [`SourceOfFunds`](../../doc/models/source-of-funds.md) | Optional | - |
| `web_data` | [`List[WebData]`](../../doc/models/web-data.md) | Optional | List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the `webDataExemption` object. |
| `web_data_exemption` | [`WebDataExemption`](../../doc/models/web-data-exemption.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_64 import Amount64
from adyen.models.business_line_info import BusinessLineInfo
from adyen.models.reason_1 import Reason1
from adyen.models.service import Service
from adyen.models.source_of_funds import SourceOfFunds
from adyen.models.web_data import WebData
from adyen.models.web_data_exemption import WebDataExemption

business_line_info = BusinessLineInfo(
    industry_code='industryCode0',
    legal_entity_id='legalEntityId6',
    service=Service.PAYMENTPROCESSING,
    industry_code_description='industryCodeDescription6',
    sales_channels=[
        'salesChannels2',
        'salesChannels3',
        'salesChannels4'
    ],
    source_of_funds=SourceOfFunds(
        adyen_processed_funds=False,
        amount=Amount64(
            currency='currency2',
            value=110,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        asset_months_held=46,
        cryptocurrency_exchange='cryptocurrencyExchange2',
        date_of_funds_received=dateutil.parser.parse('2016-03-13').date(),
        date_of_source_event=dateutil.parser.parse('2016-03-13').date(),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    web_data=[
        WebData(
            web_address='webAddress4',
            web_address_id='webAddressId8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        WebData(
            web_address='webAddress4',
            web_address_id='webAddressId8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    web_data_exemption=WebDataExemption(
        reason=Reason1.NOONLINEPRESENCE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

