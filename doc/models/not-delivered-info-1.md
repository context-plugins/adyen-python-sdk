
# Not Delivered Info 1

Additional information for raising a dispute of `type` **notDelivered**. Required for disputes of `type` **notDelivered**.

*This model accepts additional fields of type Any.*

## Structure

`NotDeliveredInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agreed_delivery_location` | `str` | Optional | The delivery location specified by the cardholder. Required if **deliveredToWrongLocation** is **true**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `500` |
| `date_of_cancellation` | `date` | Optional | The date the undelivered goods or services were cancelled in YYYY-MM-DD format. |
| `delivered_to_wrong_location` | `bool` | Optional | Indicates goods were delivered to the wrong location.<br><br>Possible values: **true**, **false**. |
| `description_of_issue` | `str` | Required | Your description of the issue for raising a dispute of `type` **notDelivered**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `did_cardholder_return` | `bool` | Optional | Indicates if the cardholder returned the goods to the merchant. Required if **isDeliveryLate** is **true**.<br><br>Possible values: **true**, **false**. |
| `is_delivery_late` | `bool` | Optional | Indicates if the goods or services were delivered late. Required if **whatWasNotDelivered** is **goods**.<br><br>Possible values: **true**, **false**. |
| `is_merchant_bankrupt` | `bool` | Optional | Indicates if the transaction was processed by a bankrupt merchant.<br><br>Possible values: **true**, **false**. |
| `is_non_fiat_or_nft` | `bool` | Optional | Indicates if the transaction is non-fiat or non-fungible token (NFT) related.<br><br>Possible values: **true**, **false**. |
| `last_expected_date` | `date` | Required | The date the undelivered goods or services were expected to be delivered in YYYY-MM-DD format. |
| `what_was_not_delivered` | [`ProductType2`](../../doc/models/product-type-2.md) | Required | - |
| `who_cancelled` | [`CancellingEntity1`](../../doc/models/cancelling-entity-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.not_delivered_info_1 import NotDeliveredInfo1
from adyen.models.product_type_2 import ProductType2

not_delivered_info_1 = NotDeliveredInfo1(
    description_of_issue='descriptionOfIssue8',
    last_expected_date=dateutil.parser.parse('2016-03-13').date(),
    what_was_not_delivered=ProductType2.GOODS,
    agreed_delivery_location='agreedDeliveryLocation2',
    date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
    delivered_to_wrong_location=False,
    did_cardholder_return=False,
    is_delivery_late=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

