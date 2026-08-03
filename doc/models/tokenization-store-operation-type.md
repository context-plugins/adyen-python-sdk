
# Tokenization Store Operation Type

The operation performed on the token. Possible values:

* **created**: the token has been created.
* **updated**: the existing token has been updated.
* **alreadyExisting**: the details have already been stored.

## Enumeration

`TokenizationStoreOperationType`

## Fields

| Name |
|  --- |
| `CREATED` |
| `UPDATED` |
| `ALREADYEXISTING` |

## Example

```python
from adyen.models.tokenization_store_operation_type import TokenizationStoreOperationType

tokenization_store_operation_type = TokenizationStoreOperationType.UPDATED
```

