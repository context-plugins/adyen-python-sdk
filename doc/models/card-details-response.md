
# Card Details Response

## Structure

`CardDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brands` | [`List[CardBrandDetails]`](../../doc/models/card-brand-details.md) | Optional | The list of brands identified for the card. |
| `funding_source` | `str` | Optional | The funding source of the card, for example **DEBIT**, **CREDIT**, or **PREPAID**. |
| `is_card_commercial` | `bool` | Optional | Indicates if this is a commercial card or a consumer card. If **true**, it is a commercial card. If **false**, it is a consumer card. |
| `issuing_country_code` | `str` | Optional | The two-letter country code  of the country where the card was issued. |

## Example

```python
from adyen.models.card_brand_details import CardBrandDetails
from adyen.models.card_details_response import CardDetailsResponse

card_details_response = CardDetailsResponse(
    brands=[
        CardBrandDetails(
            healthcare=False,
            supported=False,
            mtype='type6'
        ),
        CardBrandDetails(
            healthcare=False,
            supported=False,
            mtype='type6'
        )
    ],
    funding_source='fundingSource4',
    is_card_commercial=False,
    issuing_country_code='issuingCountryCode4'
)
```

