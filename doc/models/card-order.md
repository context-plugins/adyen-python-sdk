
# Card Order

## Structure

`CardOrder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_date` | `datetime` | Optional | The date when the card order is created. |
| `card_manufacturing_profile_id` | `str` | Optional | The unique identifier of the card manufacturer profile. |
| `closed_date` | `datetime` | Optional | The date when the card order processing ends. |
| `end_date` | `datetime` | Optional | The date when you manually closed the card order.<br><br>Card orders are automatically closed by the end of the day it was created. If you manually closed it beforehand, the closing date is shown as the `endDate`. |
| `id` | `str` | Optional | The unique identifier of the card order. |
| `lock_date` | `datetime` | Optional | The date when the card order processing begins. |
| `service_center` | `str` | Optional | The service center. |
| `status` | [`Status61Enum`](../../doc/models/status-61-enum.md) | Optional | The status of the card order.<br><br>Possible values: **Open**, **Closed**. |

## Example

```python
import dateutil.parser

from adyen.models.card_order import CardOrder

card_order = CardOrder(
    begin_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    card_manufacturing_profile_id='cardManufacturingProfileId8',
    closed_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id4'
)
```

