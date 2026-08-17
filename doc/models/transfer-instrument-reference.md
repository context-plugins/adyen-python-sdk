
# Transfer Instrument Reference

## Structure

`TransferInstrumentReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_identifier` | `str` | Required | The masked IBAN or bank account number. |
| `id` | `str` | Required | The unique identifier of the resource. |
| `real_last_four` | `str` | Optional | Four last digits of the bank account number. If the transfer instrument is created using [instant bank account verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding), and it is a virtual bank account, these digits may be different from the last four digits of the masked account number. |
| `trusted_source` | `bool` | Optional, Read-only | Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding). |

## Example

```python
from adyen.models.transfer_instrument_reference import TransferInstrumentReference

transfer_instrument_reference = TransferInstrumentReference(
    account_identifier='accountIdentifier4',
    id='id2',
    real_last_four='realLastFour0'
)
```

