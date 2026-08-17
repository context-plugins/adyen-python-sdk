
# Card Reader APDU Request 2

Content of the Card Reader APDU Request message.

## Structure

`CardReaderAPDURequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apdu_class` | `str` | Required | Class field of the APDU command (CLA). APDU request for Card Reader device request. For specific card like synchronous card, a private value should be used in accordance to ISO 7816- 4 (private range D0-FE).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_instruction` | `str` | Required | Instruction field of the APDU command (INS).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_par_1` | `str` | Required | Parameter 1 field of the APDU command (P1).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_par_2` | `str` | Required | Parameter 2 field of the APDU command(P2).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_data` | `str` | Optional | Data field of the APDU command (Lc + Data).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `apdu_expected_length` | `str` | Optional | Expected length of the data field of the APDU response to the command (Le).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |

## Example

```python
from adyen.models.card_reader_apdu_request_2 import CardReaderAPDURequest2

card_reader_apdu_request_2 = CardReaderAPDURequest2(
    apdu_class='APDUClass0',
    apdu_instruction='APDUInstruction2',
    apdu_par_1='APDUPar16',
    apdu_par_2='APDUPar24',
    apdu_data='APDUData0',
    apdu_expected_length='APDUExpectedLength4'
)
```

