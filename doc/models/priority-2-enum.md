
# Priority 2 Enum

The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Possible values:

* **regular**: For normal, low-value transactions.

* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.

* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.

* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).

* **crossBorder**: For high-value transfers to a recipient in a different country.

* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

## Enumeration

`Priority2Enum`

## Fields

| Name |
|  --- |
| `CROSSBORDER` |
| `FAST` |
| `INSTANT` |
| `INTERNAL` |
| `REGULAR` |
| `WIRE` |

## Example

```python
from adyen.models.priority_2_enum import Priority2Enum

priority_2 = Priority2Enum.CROSSBORDER
```

