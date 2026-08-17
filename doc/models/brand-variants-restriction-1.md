
# Brand Variants Restriction 1

List of card brand variants and the operation.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`BrandVariantsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of card brand variants.<br><br>Possible values:<br><br>- **mc**, **mccredit**, **mccommercialcredit_b2b**, **mcdebit**, **mcbusinessdebit**, **mcbusinessworlddebit**, **mcprepaid**, **mcmaestro**<br><br>- **visa**, **visacredit**, **visadebit**, **visaprepaid**.<br><br>You can specify a rule for a generic variant. For example, to create a rule for all Mastercard payment instruments, use **mc**. The rule is applied to all payment instruments under **mc**, such as **mcbusinessdebit** and **mcdebit**. |

## Example

```python
from adyen.models.brand_variants_restriction_1 import BrandVariantsRestriction1

brand_variants_restriction_1 = BrandVariantsRestriction1(
    operation='operation0',
    value=[
        'value4',
        'value5',
        'value6'
    ]
)
```

