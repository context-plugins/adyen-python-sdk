
# Track Format

Magnetic track or magnetic ink characters line.
Possible values:

* **ISO**
* **JIS-I**
* **JIS-II**
* **AAMVA**
* **CMC-7**
* **E-13B**

## Enumeration

`TrackFormat`

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
from adyen.models.track_format import TrackFormat

track_format = TrackFormat.JISII
```

