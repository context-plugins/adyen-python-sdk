# PCI Compliance Questionnaire Page

```python
pci_compliance_questionnaire_page_api = client.pci_compliance_questionnaire_page
```

## Class Name

`PCIComplianceQuestionnairePageApi`


# Post-Get Pci Questionnaire Url

Returns a link to a PCI compliance questionnaire that you can send to your account holder.

> You should only use this endpoint if you have a [partner platform setup](https://docs.adyen.com/classic-platforms/platforms-for-partners).

```python
def post_get_pci_questionnaire_url(self,
                                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetPciUrlRequest`](../../doc/models/get-pci-url-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetPciUrlResponse`](../../doc/models/get-pci-url-response.md)

## Example Usage

```python
body = GetPciUrlRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    return_url='https://your.return-url.com/?submerchant=123'
)

result = pci_compliance_questionnaire_page_api.post_get_pci_questionnaire_url(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "invalidFields": [],
  "pspReference": "8315748692943050",
  "resultCode": "Success",
  "redirectUrl": "https://hop-test.adyen.com/hop/pci/?token=<token>"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |

