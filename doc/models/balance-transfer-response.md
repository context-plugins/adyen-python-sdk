
# Balance Transfer Response

## Structure

`BalanceTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Required | The date when the balance transfer was performed. |
| `psp_reference` | `str` | Required | Adyen's 16-character string reference associated with the balance transfer. |

## Example

```python
import dateutil.parser

from adyen.models.balance_transfer_response import BalanceTransferResponse

balance_transfer_response = BalanceTransferResponse(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    psp_reference='pspReference4'
)
```

