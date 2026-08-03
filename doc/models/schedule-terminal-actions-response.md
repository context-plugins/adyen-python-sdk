
# Schedule Terminal Actions Response

*This model accepts additional fields of type Any.*

## Structure

`ScheduleTerminalActionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_details` | [ForceRebootDetails](../../doc/models/force-reboot-details.md) \| [InstallAndroidAppDetails](../../doc/models/install-android-app-details.md) \| [InstallAndroidCertificateDetails](../../doc/models/install-android-certificate-details.md) \| [ReleaseUpdateDetails](../../doc/models/release-update-details.md) \| [UninstallAndroidAppDetails](../../doc/models/uninstall-android-app-details.md) \| [UninstallAndroidCertificateDetails](../../doc/models/uninstall-android-certificate-details.md) \| None | Optional | This is a container for one-of cases. |
| `items` | [`List[TerminalActionScheduleDetail]`](../../doc/models/terminal-action-schedule-detail.md) | Optional | A list containing a terminal ID and an action ID for each terminal that the action was scheduled for. |
| `scheduled_at` | `str` | Optional | The date and time when the action should happen.<br>Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+0100**<br>The action is sent with the first [maintenance call](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api#when-actions-take-effect) after the specified date and time in the time zone of the terminal.<br>An empty value causes the action to be sent as soon as possible: at the next maintenance call. |
| `store_id` | `str` | Optional | The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the `terminalIds` list must be assigned to this store. |
| `terminals_with_errors` | `Dict[str, Any]` | Optional | The validation errors that occurred in the list of terminals, and for each error the IDs of the terminals that the error applies to. |
| `total_errors` | `int` | Optional | The number of terminals for which scheduling the action failed. |
| `total_scheduled` | `int` | Optional | The number of terminals for which the action was successfully scheduled. This doesn't mean the action has happened yet. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.force_reboot_details import ForceRebootDetails
from adyen.models.schedule_terminal_actions_response import ScheduleTerminalActionsResponse
from adyen.models.terminal_action_schedule_detail import TerminalActionScheduleDetail
from adyen.models.type_210 import Type210

schedule_terminal_actions_response = ScheduleTerminalActionsResponse(
    action_details=ForceRebootDetails(
        mtype=Type210.FORCEREBOOT,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    items=[
        TerminalActionScheduleDetail(
            id='id8',
            terminal_id='terminalId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TerminalActionScheduleDetail(
            id='id8',
            terminal_id='terminalId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    scheduled_at='scheduledAt8',
    store_id='storeId6',
    terminals_with_errors={
        'key0': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

