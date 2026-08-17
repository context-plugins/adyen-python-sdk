
# Source of Funds 11

Contains information about the source of your user's funds. Required only if the `service` is **banking** or **issuing**.

## Structure

`SourceOfFunds11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_processed_funds` | `bool` | Required | Indicates whether the funds are coming from transactions processed by Adyen. If **false**, the `type` is required. |
| `amount` | [`PatchableAmountDTO`](../../doc/models/patchable-amount-dto.md) | Optional | Required if `type` is **business**, **assetSale**, **gamblingWinnings** or **inheritance**.<br><br>For `type` **business**, provide the annual turn over of the business. For `type` **assetSale**, **gamblingWinnings** or **inheritance**, provide the amount of the funds. |
| `asset_months_held` | `int` | Optional | The number of months that the asset has been in possession of the user.<br><br>For example, if the source of funds is of type **cryptocurrencyIncome** then `assetMonthsHeld` is the number of months the user has owned the cryptocurrency. |
| `cryptocurrency_exchange` | `str` | Optional | Required if `type` is **cryptocurrencyIncome**. The cryptocurrency exchange where the funds were acquired. |
| `date_of_funds_received` | `date` | Optional | Required if `type` is **donations** or **inheritance**. The date the funds were received, in YYYY-MM-DD format. |
| `date_of_source_event` | `date` | Optional | Required if `type` is **assetSale** or **gamblingWinnings**. The date the funds were received, in YYYY-MM-DD format.<br><br>For example, if the source of funds is of type **assetSale**, the dateOfSourceEvent is the date of the sale. If the source of funds is of type **gamblingWinnings**, the dateOfSourceEvent is the date of winnings. |
| `description` | `str` | Optional | Required if `type` is **business** or **assetSale**. A description for the source of funds.<br><br>For example, for `type` **business**, provide a description of where the business transactions come from, such as payments through bank transfer. For `type` **assetSale**, provide a description of the asset. For example, the address of a residential property if it is a property sale. |
| `financiers` | [`List[Financier]`](../../doc/models/financier.md) | Optional | Required if `type` is **thirdPartyFunding**. Information about the financiers. |
| `originator_legal_entity_id` | `str` | Optional | Required if `type` is **donations** or **inheritance**. The legal entity ID representing the originator of the source of funds.<br><br>For example, if the source of funds is **inheritance**, then `originatorOfFundsReference` should be the legal entity reference of the benefactor. |
| `purpose` | `str` | Optional | Required if `type` is **donations**. The reason for receiving the funds. |
| `relationship` | `str` | Optional | Required if `type` is **donations** or **inheritance**. The relationship of the originator of the funds to the recipient. |
| `mtype` | [`Type74Enum`](../../doc/models/type-74-enum.md) | Optional | The type of the source of funds.<br><br>Possible values:<br><br>* **business**<br>* **employment**<br>* **donations**<br>* **inheritance**<br>* **financialAid**<br>* **rentalIncome**<br>* **dividendIncome**<br>* **royaltyIncome**<br>* **thirdPartyFunding**<br>* **pensionIncome**<br>* **insuranceSettlement**<br>* **cryptocurrencyIncome**<br>* **assetSale**<br>* **loans**<br>* **gamblingWinnings** |
| `website` | `str` | Optional | Required if `type` is **gamblingWinnings**. The location of the gambling site for the winnings.<br><br>For example, if the source of funds is online gambling, provide the website of the gambling company. |

## Example

```python
import dateutil.parser

from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.source_of_funds_11 import SourceOfFunds11

source_of_funds_11 = SourceOfFunds11(
    adyen_processed_funds=False,
    amount=PatchableAmountDTO(
        currency='currency2',
        value=110
    ),
    asset_months_held=244,
    cryptocurrency_exchange='cryptocurrencyExchange6',
    date_of_funds_received=dateutil.parser.parse('2016-03-13').date(),
    date_of_source_event=dateutil.parser.parse('2016-03-13').date()
)
```

