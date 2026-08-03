# Terminalactions-Companylevel

```python
terminalactions_companylevel_api = client.terminalactions_companylevel
```

## Class Name

`TerminalactionsCompanylevelApi`

## Methods

* [Get-Companies-Company Id-Terminal Actions](../../doc/controllers/terminalactions-companylevel.md#get-companies-company-id-terminal-actions)
* [Get-Companies-Company Id-Terminal Actions-Action Id](../../doc/controllers/terminalactions-companylevel.md#get-companies-company-id-terminal-actions-action-id)


# Get-Companies-Company Id-Terminal Actions

Returns the [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) that have been scheduled for the company identified in the path.The response doesn't include actions that are scheduled by Adyen.
To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal actions read
* Management API—Terminal actions read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_companies_company_id_terminal_actions(self,
                                             company_id,
                                             page_number=None,
                                             page_size=None,
                                             status=None,
                                             mtype=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `page_number` | `int` | Query, Optional | The number of the page to fetch. |
| `page_size` | `int` | Query, Optional | The number of items to have on a page, maximum 100. The default is 20 items on a page. |
| `status` | `str` | Query, Optional | Returns terminal actions with the specified status.<br>Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**. |
| `mtype` | `str` | Query, Optional | Returns terminal actions of the specified type.<br>Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListExternalTerminalActionsResponse`](../../doc/models/list-external-terminal-actions-response.md).

## Example Usage

```python
company_id = 'companyId0'

result = terminal_actions_company_level_api.get_companies_company_id_terminal_actions(company_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "actionType": "InstallAndroidApp",
      "config": "{\"apps\":\"com.adyen.android.calculator:103\"}",
      "confirmedAt": "2021-11-10T00:00:00+01:00",
      "id": "TRAC422T2223223K5GFMQHM6WQ4KB6",
      "result": "Cancelled manually by user USER@Psp.AdyenPspService",
      "scheduledAt": "2021-11-10T14:53:05+01:00",
      "status": "cancelled",
      "terminalId": "S1E-000150183300032"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Companies-Company Id-Terminal Actions-Action Id

Returns the details of the [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) identified in the path.
To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal actions read
* Management API—Terminal actions read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_companies_company_id_terminal_actions_action_id(self,
                                                       company_id,
                                                       action_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `action_id` | `str` | Template, Required | The unique identifier of the terminal action. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ExternalTerminalAction`](../../doc/models/external-terminal-action.md).

## Example Usage

```python
company_id = 'companyId0'

action_id = 'actionId0'

result = terminal_actions_company_level_api.get_companies_company_id_terminal_actions_action_id(
    company_id,
    action_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "actionType": "InstallAndroidCertificate",
  "config": "{\"certificates\":\"5dff6b...\"}",
  "confirmedAt": "2022-06-27T17:44:54+02:00",
  "id": "TRAC4224Z223223K5GD89RLBWQ6CWT",
  "result": "Ok",
  "scheduledAt": "2022-06-27T15:44:07+02:00",
  "status": "successful",
  "terminalId": "S1F2-000150183300034"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

