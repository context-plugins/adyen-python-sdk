
# Card Details Response

*This model accepts additional fields of type Any.*

## Structure

`CardDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brands` | [`List[CardBrandDetails]`](../../doc/models/card-brand-details.md) | Optional | The list of brands identified for the card. |
| `funding_source` | `str` | Optional | The funding source of the card, for example **DEBIT**, **CREDIT**, or **PREPAID**. |
| `is_card_commercial` | `bool` | Optional | Indicates if this is a commercial card or a consumer card. If **true**, it is a commercial card. If **false**, it is a consumer card. |
| `issuing_country_code` | `str` | Optional | The two-letter country code  of the country where the card was issued. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_brand_details import CardBrandDetails
from adyen.models.card_details_response import CardDetailsResponse

card_details_response = CardDetailsResponse(
    brands=[
        CardBrandDetails(
            healthcare=False,
            supported=False,
            mtype='type6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CardBrandDetails(
            healthcare=False,
            supported=False,
            mtype='type6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    funding_source='fundingSource4',
    is_card_commercial=False,
    issuing_country_code='issuingCountryCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

