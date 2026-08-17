
# Transaction Totals

If Result is Success, contains all the totals, classified as required by the Sale in the message request. At least, transaction totals are provided per Acquirer, Acquirer Settlement, and Card Brand.
Result of the Sale to POI Reconciliation processing.

## Structure

`TransactionTotals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_type` | [`PaymentInstrumentType11Enum`](../../doc/models/payment-instrument-type-11-enum.md) | Required | Type of payment instrument.<br>Possible values:<br><br>* **Card**<br>* **Cash**<br>* **Check**<br>* **Mobile**<br>* **StoredValue** |
| `acquirer_id` | `int` | Optional | Identification of the Acquirer. |
| `host_reconciliation_id` | `str` | Optional | Identifier of a reconciliation period with a payment or loyalty host.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `card_brand` | `str` | Optional | Type of payment or loyalty card.<br>If configured to present totals per card brand, and Response.Result is Success.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `poiid` | `str` | Optional | Identification of a POI System or a POI Terminal for the Sale to POI protocol.<br>Sent if requested in the message request.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `sale_id` | `str` | Optional | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.<br>Sent if requested in the message request.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `operator_id` | `str` | Optional | Identification of the Cashier or Operator.<br>Sent if requested in the message request.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `shift_number` | `str` | Optional | Shift number.<br>Sent if requested in the message request.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `totals_group_id` | `str` | Optional | Identification of a group of transaction on a POI Terminal, having the same Sale features.<br>Sent if requested in the message request.<br><br>**Constraints**: *Pattern*: `^.{1,16}$` |
| `payment_currency` | `str` | Optional | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `payment_totals` | [`List[PaymentTotals]`](../../doc/models/payment-totals.md) | Optional | Totals of the payment transaction during the reconciliation period.<br>If both `TransactionCount` and `TransactionAmount` are not equal to zero. |

## Example

```python
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.transaction_totals import TransactionTotals

transaction_totals = TransactionTotals(
    payment_instrument_type=PaymentInstrumentType11Enum.STOREDVALUE,
    acquirer_id=190,
    host_reconciliation_id='HostReconciliationID8',
    card_brand='CardBrand6',
    poiid='POIID8',
    sale_id='SaleID2'
)
```

