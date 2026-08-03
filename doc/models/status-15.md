
# Status 15

The status of the app. Possible values:

* `processing`: the app is being signed and converted to a format that the terminal can handle.
* `error`: something went wrong. Check that the app matches the [requirements](https://docs.adyen.com/point-of-sale/android-terminals/app-requirements).
* `invalid`: there is something wrong with the APK file of the app.
* `ready`: the app has been signed and converted.
* `archived`: the app is no longer available.

## Enumeration

`Status15`

## Fields

| Name |
|  --- |
| `ARCHIVED` |
| `ERROR` |
| `INVALID` |
| `PROCESSING` |
| `READY` |

## Example

```python
from adyen.models.status_15 import Status15

status_15 = Status15.ERROR
```

