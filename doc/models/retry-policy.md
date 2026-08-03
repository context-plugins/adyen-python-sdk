
# Retry Policy

When set to true, you can retry for failed recurring payments. The default value is true.

## Enumeration

`RetryPolicy`

## Fields

| Name |
|  --- |
| `TRUE` |
| `FALSE` |

## Example

```python
from adyen.models.retry_policy import RetryPolicy

retry_policy = RetryPolicy.TRUE
```

