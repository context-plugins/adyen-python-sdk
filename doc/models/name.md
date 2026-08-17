
# Name

Name of the person., The shopper's full name., the name of the person, The name of the shopper., The shopper's full name., The shopper's name.

When the `entityType` is `Company`, the `shopperName.lastName` must contain the company name., The shopper's name.

In case the `entityType` is `Company`, the `shopperName.lastName` must contain the company name.

> This field is required to update the existing `shopperName` associated with a recurring contract., Name of the person., The user's full name.

Allowed length: 1—80 characters., The user's full name., The name of the contact.

## Structure

`Name`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name import Name

name = Name(
    first_name='firstName4',
    last_name='lastName4'
)
```

