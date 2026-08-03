
# Amounts Req

Various amounts related to the payment request from the Sale System.

*This model accepts additional fields of type Any.*

## Structure

`AmountsReq`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `requested_amount` | `float` | Required | Amount requested by the Sale for the payment.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `cash_back_amount` | `float` | Optional | The cash-back part of the amount requested by the Sale for the payment.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `tip_amount` | `float` | Optional | Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the amount.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `paid_amount` | `float` | Optional | Amount already paid in case of split payment. Depending on the context, a split payment is either a split amount, or a split basket (required by some payment means as fleet cards). The PaidAmount is present when the split payment is a split<br>of the amount. Split of the basket involves two Sale Transactions, and does not have to be recognised by<br>the POI.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `minimum_amount_to_deliver` | `float` | Optional | Minimum amount the Sale System is allowed to deliver for this payment. For the OneTimeReservation, when the maximum amount is unknown, the Sale System indicates the minimum amount it allows.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `maximum_cash_back_amount` | `float` | Optional | Maximum amount which could be requested for cash-back to the Sale System. Allows the Cashier<br>to limit the amount value of cash-back to deliver to the Customer.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `minimum_split_amount` | `float` | Optional | Minimum amount of a split, which could be requested by a Customer.Allows the Merchant to limit the number of split requested by the Customer.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amounts_req import AmountsReq

amounts_req = AmountsReq(
    currency='Currency4',
    requested_amount=210.88,
    cash_back_amount=84.32,
    tip_amount=209.22,
    paid_amount=246.58,
    minimum_amount_to_deliver=79.98,
    maximum_cash_back_amount=30.22,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

