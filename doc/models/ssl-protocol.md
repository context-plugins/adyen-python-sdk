
# Ssl Protocol

The SSL protocol employed by the endpoint.

> Permitted values: `TLSv12`, `TLSv13`.

## Enumeration

`SslProtocol`

## Fields

| Name |
|  --- |
| `TLSV12` |
| `TLSV13` |

## Example

```python
from adyen.models.ssl_protocol import SslProtocol

ssl_protocol = SslProtocol.TLSV12
```

