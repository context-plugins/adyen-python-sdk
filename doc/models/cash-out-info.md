
# Cash Out Info

## Structure

`CashOutInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the amount of the cashout, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `counterparty` | [`CashOutInfoCounterparty1`](../../doc/models/cash-out-info-counterparty-1.md) | Optional | Contains information about the counterparty of the cashout transfer. |
| `description` | `str` | Optional | Allowed and returned only when you provide the `counterparty.transferInstrumentId` field.<br><br>Your description of the cashout transfer. This description is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.<br><br>If you do not provide a description, Adyen generates a description automatically. This generated description is not returned in the response.<br><br>Supported characters: **[a-z] [A-Z] [0-9] / - ? : ( ) . , ' + Space**. |
| `fee` | [`Fee21`](../../doc/models/fee-21.md) | Optional | Contains the currency and value of the cashout fee, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `id` | `str` | Optional, Read-only | The ID of the resource. |
| `instructing_balance_account_id` | `str` | Required | The unique identifier of the balance account that initiates the cashout request. |
| `reference_for_beneficiary` | `str` | Optional | Allowed and returned only when you provide the `counterparty.transferInstrumentId` field.<br><br>The reference that is sent to the recipient of a cashout transfer. This reference is also sent in all webhooks related to the cashout transfer, so you can use it to track the status of the transfer.<br><br>If you do not provide a reference for the beneficiary, Adyen generates one automatically. This generated reference for the beneficiary is not returned in the response.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**. |
| `transfer_instrument_id` | `str` | Optional | **Use `counterparty.transferInstrumentId` instead.**<br><br>The unique identifier of the counterparty transfer instrument. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.cash_out_info import CashOutInfo
from adyen.models.cash_out_info_counterparty_1 import CashOutInfoCounterparty1
from adyen.models.fee_21 import Fee21

cash_out_info = CashOutInfo(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    instructing_balance_account_id='instructingBalanceAccountId2',
    counterparty=CashOutInfoCounterparty1(
        transfer_instrument_id='transferInstrumentId4'
    ),
    description='description0',
    fee=Fee21(
        amount=Amount17(
            currency='currency2',
            value=110
        )
    ),
    reference_for_beneficiary='referenceForBeneficiary0'
)
```

