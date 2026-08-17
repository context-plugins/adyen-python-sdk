
# Status 51 Enum

The result of the transfer.

For example:

- **received**: an outgoing transfer request is created.
- **refused**: the transfer request is rejected by Adyen for one of the following reasons:
  - Transfer limit exceeded.
  - Transaction rule requirements violated.
- **authorised**: the transfer request is authorized and the funds are reserved.
- **booked**: the funds are deducted from your user's balance account.
- **failed**: the transfer is rejected by the counterparty's bank.
- **returned**: the transfer is returned by the counterparty's bank.

## Enumeration

`Status51Enum`

## Fields

| Name |
|  --- |
| `APPROVALPENDING` |
| `ATMWITHDRAWAL` |
| `ATMWITHDRAWALREVERSALPENDING` |
| `ATMWITHDRAWALREVERSED` |
| `AUTHADJUSTMENTAUTHORISED` |
| `AUTHADJUSTMENTERROR` |
| `AUTHADJUSTMENTREFUSED` |
| `AUTHORISED` |
| `BANKTRANSFER` |
| `BANKTRANSFERPENDING` |
| `BOOKED` |
| `BOOKINGPENDING` |
| `CANCELLED` |
| `CAPTUREPENDING` |
| `CAPTUREREVERSALPENDING` |
| `CAPTUREREVERSED` |
| `CAPTURED` |
| `CAPTUREDEXTERNALLY` |
| `CHARGEBACK` |
| `CHARGEBACKEXTERNALLY` |
| `CHARGEBACKPENDING` |
| `CHARGEBACKREVERSALPENDING` |
| `CHARGEBACKREVERSED` |
| `CREDITED` |
| `DEPOSITCORRECTION` |
| `DEPOSITCORRECTIONPENDING` |
| `DISPUTE` |
| `DISPUTECLOSED` |
| `DISPUTEEXPIRED` |
| `DISPUTENEEDSREVIEW` |
| `ERROR` |
| `EXPIRED` |
| `FAILED` |
| `FEE` |
| `FEEPENDING` |
| `INTERCHANGEADJUSTED` |
| `INTERNALTRANSFER` |
| `INTERNALTRANSFERPENDING` |
| `INVOICEDEDUCTION` |
| `INVOICEDEDUCTIONPENDING` |
| `MANUALCORRECTIONPENDING` |
| `MANUALLYCORRECTED` |
| `MATCHEDSTATEMENT` |
| `MATCHEDSTATEMENTPENDING` |
| `MERCHANTPAYIN` |
| `MERCHANTPAYINPENDING` |
| `MERCHANTPAYINREVERSED` |
| `MERCHANTPAYINREVERSEDPENDING` |
| `MISCCOST` |
| `MISCCOSTPENDING` |
| `PAYMENTCOST` |
| `PAYMENTCOSTPENDING` |
| `PENDING` |
| `PENDINGAPPROVAL` |
| `PENDINGEXECUTION` |
| `RECEIVED` |
| `REFUNDPENDING` |
| `REFUNDREVERSALPENDING` |
| `REFUNDREVERSED` |
| `REFUNDED` |
| `REFUNDEDEXTERNALLY` |
| `REFUSED` |
| `REJECTED` |
| `RESERVEADJUSTMENT` |
| `RESERVEADJUSTMENTPENDING` |
| `RETURNED` |
| `REVERSED` |
| `SECONDCHARGEBACK` |
| `SECONDCHARGEBACKPENDING` |
| `UNDEFINED` |

## Example

```python
from adyen.models.status_51_enum import Status51Enum

status_51 = Status51Enum.FAILED
```

