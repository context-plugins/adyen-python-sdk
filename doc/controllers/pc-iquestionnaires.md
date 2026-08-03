# PC Iquestionnaires

```python
pc_iquestionnaires_api = client.pc_iquestionnaires
```

## Class Name

`PcIquestionnairesApi`

## Methods

* [Get-Legal Entities-Id-Pci Questionnaires](../../doc/controllers/pc-iquestionnaires.md#get-legal-entities-id-pci-questionnaires)
* [Post-Legal Entities-Id-Pci Questionnaires-Generate Pci Templates](../../doc/controllers/pc-iquestionnaires.md#post-legal-entities-id-pci-questionnaires-generate-pci-templates)
* [Post-Legal Entities-Id-Pci Questionnaires-Sign Pci Templates](../../doc/controllers/pc-iquestionnaires.md#post-legal-entities-id-pci-questionnaires-sign-pci-templates)
* [Post-Legal Entities-Id-Pci Questionnaires-Signing Required](../../doc/controllers/pc-iquestionnaires.md#post-legal-entities-id-pci-questionnaires-signing-required)
* [Get-Legal Entities-Id-Pci Questionnaires-Pciid](../../doc/controllers/pc-iquestionnaires.md#get-legal-entities-id-pci-questionnaires-pciid)


# Get-Legal Entities-Id-Pci Questionnaires

Get a list of signed PCI questionnaires.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_legal_entities_id_pci_questionnaires(self,
                                            id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity to get PCI questionnaire information. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPciQuestionnaireInfosResponse`](../../doc/models/get-pci-questionnaire-infos-response.md).

## Example Usage

```python
id = 'id0'

result = pci_questionnaires_api.get_legal_entities_id_pci_questionnaires(id)

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
      "createdAt": "2023-03-02T17:54:19.538365Z",
      "id": "PCID422GZ22322565HHMH48CW63CPH",
      "validUntil": "2024-03-01T17:54:19.538365Z"
    },
    {
      "createdAt": "2023-03-02T17:54:19.538365Z",
      "id": "PCID422GZ22322565HHMH49CW75Z9H",
      "validUntil": "2024-03-01T17:54:19.538365Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Legal Entities-Id-Pci Questionnaires-Generate Pci Templates

Generates the required PCI questionnaires based on the user's [salesChannel](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels).

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_pci_questionnaires_generate_pci_templates(self,
                                                                    id,
                                                                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity to get PCI questionnaire information. |
| `body` | [`GeneratePciDescriptionRequest`](../../doc/models/generate-pci-description-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GeneratePciDescriptionResponse`](../../doc/models/generate-pci-description-response.md).

## Example Usage

```python
id = 'id0'

body = GeneratePciDescriptionRequest(
    language='fr'
)

result = pci_questionnaires_api.post_legal_entities_id_pci_questionnaires_generate_pci_templates(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC==",
  "language": "fr",
  "pciTemplateReferences": [
    "PCIT-T7KC6VGL",
    "PCIT-PKB6DKS4"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Legal Entities-Id-Pci Questionnaires-Sign Pci Templates

Signs the required PCI questionnaire.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_pci_questionnaires_sign_pci_templates(self,
                                                                id,
                                                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The legal entity ID of the user that has a contractual relationship with your platform. |
| `body` | [`PciSigningRequest`](../../doc/models/pci-signing-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PciSigningResponse`](../../doc/models/pci-signing-response.md).

## Example Usage

```python
id = 'id0'

body = PciSigningRequest(
    pci_template_references=[
        'PCIT-T7KC6VGL',
        'PCIT-PKB6DKS4'
    ],
    signed_by='LE00000000000000000000002'
)

result = pci_questionnaires_api.post_legal_entities_id_pci_questionnaires_sign_pci_templates(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pciQuestionnaireIds": [
    "PCID422GZ22322565HHMH48CW63CPH",
    "PCID422GZ22322565HHMH49CW75Z9H"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Legal Entities-Id-Pci Questionnaires-Signing Required

Calculate PCI status of a legal entity.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_pci_questionnaires_signing_required(self,
                                                              id,
                                                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity to calculate PCI status. |
| `body` | [`CalculatePciStatusRequest`](../../doc/models/calculate-pci-status-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CalculatePciStatusResponse`](../../doc/models/calculate-pci-status-response.md).

## Example Usage

```python
id = 'id0'

result = pci_questionnaires_api.post_legal_entities_id_pci_questionnaires_signing_required(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Get-Legal Entities-Id-Pci Questionnaires-Pciid

Returns the signed PCI questionnaire.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_legal_entities_id_pci_questionnaires_pciid(self,
                                                  id,
                                                  pciid)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The legal entity ID of the individual who signed the PCI questionnaire. |
| `pciid` | `str` | Template, Required | The unique identifier of the signed PCI questionnaire. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPciQuestionnaireResponse`](../../doc/models/get-pci-questionnaire-response.md).

## Example Usage

```python
id = 'id0'

pciid = 'pciid8'

result = pci_questionnaires_api.get_legal_entities_id_pci_questionnaires_pciid(
    id,
    pciid
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC==",
  "createdAt": "2023-03-02T17:54:19.538365Z",
  "id": "PCID422GZ22322565HHMH48CW63CPH",
  "validUntil": "2024-03-01T17:54:19.538365Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |

