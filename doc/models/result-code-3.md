
# Result Code 3

The result of the payment. Possible values:

* **Success** – The operation has been completed successfully.
* **Refused** – The operation was refused. The reason is given in the `refusalReason` field.
* **Error** – There was an error when the operation was processed. The reason is given in the `refusalReason` field.
* **NotEnoughBalance** – The amount on the payment method is lower than the amount given in the request. Only applicable to balance checks.

## Enumeration

`ResultCode3`

## Fields

| Name |
|  --- |
| `SUCCESS` |
| `REFUSED` |
| `ERROR` |
| `NOTENOUGHBALANCE` |

## Example

```python
from adyen.models.result_code_3 import ResultCode3

result_code_3 = ResultCode3.ERROR
```

