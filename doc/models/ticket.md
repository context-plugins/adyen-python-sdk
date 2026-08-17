
# Ticket

## Structure

`Ticket`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `issue_address` | `str` | Optional | The address of the organization that issued the ticket.<br><br>* minLength: 0 characters<br>* maxLength: 16 characters<br>* **additionalData key:** `airline.ticket_issue_address` |
| `issue_date` | `date` | Optional | The date that the ticket was issued to the passenger.<br><br>* minLength: 10 characters<br>* maxLength: 10 characters<br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `airline.issue_date` |
| `number` | `str` | Optional | The ticket's unique identifier.<br><br>* minLength: 1 character<br>* maxLength: 15 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `airline.ticket_number` |

## Example

```python
import dateutil.parser

from adyen.models.ticket import Ticket

ticket = Ticket(
    issue_address='issueAddress8',
    issue_date=dateutil.parser.parse('2016-03-13').date(),
    number='number8'
)
```

