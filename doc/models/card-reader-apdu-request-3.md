
# Card Reader Apdu Request 3

*This model accepts additional fields of type Any.*

## Structure

`CardReaderApduRequest3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apdu_class` | `str` | Required | Class field of the APDU command (CLA). APDU request for Card Reader device request. For specific card like synchronous card, a private value should be used in accordance to ISO 7816- 4 (private range D0-FE).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_instruction` | `str` | Required | Instruction field of the APDU command (INS).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_par_1` | `str` | Required | Parameter 1 field of the APDU command (P1).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_par_2` | `str` | Required | Parameter 2 field of the APDU command(P2).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `apdu_data` | `str` | Optional | Data field of the APDU command (Lc + Data).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `apdu_expected_length` | `str` | Optional | Expected length of the data field of the APDU response to the command (Le).<br><br>**Constraints**: *Pattern*: `^.{1,1}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_reader_apdu_request_3 import CardReaderApduRequest3

card_reader_apdu_request_3 = CardReaderApduRequest3(
    apdu_class='APDUClass2',
    apdu_instruction='APDUInstruction0',
    apdu_par_1='APDUPar14',
    apdu_par_2='APDUPar26',
    apdu_data='APDUData8',
    apdu_expected_length='APDUExpectedLength2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

