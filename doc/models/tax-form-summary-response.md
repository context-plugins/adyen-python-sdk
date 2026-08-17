
# Tax Form Summary Response

## Structure

`TaxFormSummaryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Summary]`](../../doc/models/summary.md) | Required | A list of tax form summaries, where each summary consists of the legal entity and the tax years in which the legal entity has a tax form. |

## Example

```python
from adyen.models.summary import Summary
from adyen.models.tax_form_summary_response import TaxFormSummaryResponse

tax_form_summary_response = TaxFormSummaryResponse(
    data=[
        Summary(
            legal_entity_id='legalEntityId6',
            tax_years=[
                221,
                222,
                223
            ]
        )
    ]
)
```

