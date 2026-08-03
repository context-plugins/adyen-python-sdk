
# Source of Funds

*This model accepts additional fields of type Any.*

## Structure

`SourceOfFunds`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_processed_funds` | `bool` | Required | Indicates whether the funds are coming from transactions processed by Adyen. If **false**, the `type` is required. |
| `amount` | [`Amount64`](../../doc/models/amount-64.md) | Optional | - |
| `asset_months_held` | `int` | Optional | The number of months that the asset has been in possession of the user.<br><br>For example, if the source of funds is of type **cryptocurrencyIncome** then `assetMonthsHeld` is the number of months the user has owned the cryptocurrency. |
| `cryptocurrency_exchange` | `str` | Optional | Required if `type` is **cryptocurrencyIncome**. The cryptocurrency exchange where the funds were acquired. |
| `date_of_funds_received` | `date` | Optional | Required if `type` is **donations** or **inheritance**. The date the funds were received, in YYYY-MM-DD format. |
| `date_of_source_event` | `date` | Optional | Required if `type` is **assetSale** or **gamblingWinnings**. The date the funds were received, in YYYY-MM-DD format.<br><br>For example, if the source of funds is of type **assetSale**, the dateOfSourceEvent is the date of the sale. If the source of funds is of type **gamblingWinnings**, the dateOfSourceEvent is the date of winnings. |
| `description` | `str` | Optional | Required if `type` is **business** or **assetSale**. A description for the source of funds.<br><br>For example, for `type` **business**, provide a description of where the business transactions come from, such as payments through bank transfer. For `type` **assetSale**, provide a description of the asset. For example, the address of a residential property if it is a property sale. |
| `financiers` | [`List[Financier]`](../../doc/models/financier.md) | Optional | Required if `type` is **thirdPartyFunding**. Information about the financiers. |
| `originator_legal_entity_id` | `str` | Optional | Required if `type` is **donations** or **inheritance**. The legal entity ID representing the originator of the source of funds.<br><br>For example, if the source of funds is **inheritance**, then `originatorOfFundsReference` should be the legal entity reference of the benefactor. |
| `purpose` | `str` | Optional | Required if `type` is **donations**. The reason for receiving the funds. |
| `relationship` | `str` | Optional | Required if `type` is **donations** or **inheritance**. The relationship of the originator of the funds to the recipient. |
| `mtype` | [`Type72`](../../doc/models/type-72.md) | Optional | - |
| `website` | `str` | Optional | Required if `type` is **gamblingWinnings**. The location of the gambling site for the winnings.<br><br>For example, if the source of funds is online gambling, provide the website of the gambling company. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_64 import Amount64
from adyen.models.source_of_funds import SourceOfFunds

source_of_funds = SourceOfFunds(
    adyen_processed_funds=False,
    amount=Amount64(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    asset_months_held=248,
    cryptocurrency_exchange='cryptocurrencyExchange6',
    date_of_funds_received=dateutil.parser.parse('2016-03-13').date(),
    date_of_source_event=dateutil.parser.parse('2016-03-13').date(),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

