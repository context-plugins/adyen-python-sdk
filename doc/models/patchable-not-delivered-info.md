
# Patchable Not Delivered Info

## Structure

`PatchableNotDeliveredInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agreed_delivery_location` | `str` | Optional | The delivery location specified by the cardholder. Required if **deliveredToWrongLocation** is **true**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `500` |
| `date_of_cancellation` | `date` | Optional | The date the undelivered goods or services were cancelled in YYYY-MM-DD format. |
| `delivered_to_wrong_location` | `bool` | Optional | Indicates goods were delivered to the wrong location.<br><br>Possible values: **true**, **false**. |
| `description_of_issue` | `str` | Optional | Your description of the issue for raising a dispute of `type` **notDelivered**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `did_cardholder_return` | `bool` | Optional | Indicates if the cardholder returned the goods to the merchant. Required if **isDeliveryLate** is **true**.<br><br>Possible values: **true**, **false**. |
| `is_delivery_late` | `bool` | Optional | Indicates if the goods or services were delivered late. Required if **whatWasNotDelivered** is **goods**.<br><br>Possible values: **true**, **false**. |
| `is_merchant_bankrupt` | `bool` | Optional | Indicates if the transaction was processed by a bankrupt merchant.<br><br>Possible values: **true**, **false**. |
| `is_non_fiat_or_nft` | `bool` | Optional | Indicates if the transaction is non-fiat or non-fungible token (NFT) related.<br><br>Possible values: **true**, **false**. |
| `last_expected_date` | `date` | Optional | The date the undelivered goods or services were expected to be delivered in YYYY-MM-DD format. |
| `what_was_not_delivered` | [`ProductType21Enum`](../../doc/models/product-type-21-enum.md) | Optional | The type of product that you expected to receive.<br><br>Possible values: **goods**, **services**. |
| `who_cancelled` | [CancellingEntity](../../doc/models/cancelling-entity-enum.md) \| None | Optional | This is a container for one-of cases. |

## Example

```python
import dateutil.parser

from adyen.models.patchable_not_delivered_info import PatchableNotDeliveredInfo

patchable_not_delivered_info = PatchableNotDeliveredInfo(
    agreed_delivery_location='agreedDeliveryLocation0',
    date_of_cancellation=dateutil.parser.parse('2016-03-13').date(),
    delivered_to_wrong_location=False,
    description_of_issue='descriptionOfIssue0',
    did_cardholder_return=False
)
```

