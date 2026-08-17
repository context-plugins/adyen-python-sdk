
# Result Code 3 Enum

The result of the payment. Possible values:

* **Success** – The operation has been completed successfully.
* **Refused** – The operation was refused. The reason is given in the `refusalReason` field.
* **Error** – There was an error when the operation was processed. The reason is given in the `refusalReason` field.
* **NotEnoughBalance** – The amount on the payment method is lower than the amount given in the request. Only applicable to balance checks.

## Enumeration

`ResultCode3Enum`

## Fields

| Name |
|  --- |
| `SUCCESS` |
| `REFUSED` |
| `ERROR` |
| `NOTENOUGHBALANCE` |

## Example

```python
from adyen.models.result_code_3_enum import ResultCode3Enum

result_code_3 = ResultCode3Enum.ERROR
```

