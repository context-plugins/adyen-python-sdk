
# Key

## Structure

`Key`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `identifier` | `str` | Optional | The unique identifier of the shared key. |
| `passphrase` | `str` | Optional | The secure passphrase to protect the shared key. Must consist of:<br><br>* At least 12 characters.<br><br>* At least 1 uppercase letter: `[A-Z]`.<br><br>* At least 1 lowercase letter: `[a-z]`.<br><br>* At least 1 digit: `[0-9]`.<br><br>* At least 1 special character. Limited to the following: `~`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `_`, `+`, `=`, `}`, `{`, `]`, `[`, `;`, `:`, `?`, `.`, `,`, `>`, `<`. |
| `version` | `int` | Optional | The version number of the shared key. |

## Example

```python
from adyen.models.key import Key

key = Key(
    identifier='identifier8',
    passphrase='passphrase0',
    version=204
)
```

