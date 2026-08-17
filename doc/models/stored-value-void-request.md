
# Stored Value Void Request

## Structure

`StoredValueVoidRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `original_reference` | `str` | Required | The original pspReference of the payment to modify. |
| `reference` | `str` | Optional | Your reference for the payment modification. This reference is visible in Customer Area and in reports.<br>Maximum length: 80 characters. |
| `store` | `str` | Optional | The physical store, for which this payment is processed.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `tender_reference` | `str` | Optional | The reference of the tender. |
| `unique_terminal_id` | `str` | Optional | The unique ID of a POS terminal. |

## Example

```python
from adyen.models.stored_value_void_request import StoredValueVoidRequest

stored_value_void_request = StoredValueVoidRequest(
    merchant_account='merchantAccount6',
    original_reference='originalReference2',
    reference='reference0',
    store='store4',
    tender_reference='tenderReference6',
    unique_terminal_id='uniqueTerminalId4'
)
```

