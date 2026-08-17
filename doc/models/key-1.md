
# Key 1

The key you share with Adyen to secure local communications when using Terminal API.

## Structure

`Key1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `identifier` | `str` | Optional | The unique identifier of the shared key. |
| `passphrase` | `str` | Optional | The secure passphrase to protect the shared key. Must consist of:<br><br>* At least 12 characters.<br><br>* At least 1 uppercase letter: `[A-Z]`.<br><br>* At least 1 lowercase letter: `[a-z]`.<br><br>* At least 1 digit: `[0-9]`.<br><br>* At least 1 special character. Limited to the following: `~`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `_`, `+`, `=`, `}`, `{`, `]`, `[`, `;`, `:`, `?`, `.`, `,`, `>`, `<`. |
| `version` | `int` | Optional | The version number of the shared key. |

## Example

```python
from adyen.models.key_1 import Key1

key_1 = Key1(
    identifier='identifier0',
    passphrase='passphrase2',
    version=220
)
```

