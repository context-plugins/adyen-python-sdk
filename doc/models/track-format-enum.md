
# Track Format Enum

Magnetic track or magnetic ink characters line.
Possible values:

* **ISO**
* **JIS-I**
* **JIS-II**
* **AAMVA**
* **CMC-7**
* **E-13B**

## Enumeration

`TrackFormatEnum`

## Fields

| Name |
|  --- |
| `ISO` |
| `JISI` |
| `JISII` |
| `AAMVA` |
| `CMC7` |
| `E13B` |

## Example

```python
from adyen.models.track_format_enum import TrackFormatEnum

track_format = TrackFormatEnum.JISII
```

