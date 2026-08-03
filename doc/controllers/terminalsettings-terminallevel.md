# Terminalsettings-Terminallevel

```python
terminalsettings_terminallevel_api = client.terminalsettings_terminallevel
```

## Class Name

`TerminalsettingsTerminallevelApi`

## Methods

* [Get-Terminals-Terminal Id-Terminal Logos](../../doc/controllers/terminalsettings-terminallevel.md#get-terminals-terminal-id-terminal-logos)
* [Patch-Terminals-Terminal Id-Terminal Logos](../../doc/controllers/terminalsettings-terminallevel.md#patch-terminals-terminal-id-terminal-logos)
* [Get-Terminals-Terminal Id-Terminal Settings](../../doc/controllers/terminalsettings-terminallevel.md#get-terminals-terminal-id-terminal-settings)
* [Patch-Terminals-Terminal Id-Terminal Settings](../../doc/controllers/terminalsettings-terminallevel.md#patch-terminals-terminal-id-terminal-settings)


# Get-Terminals-Terminal Id-Terminal Logos

Returns the logo that is configured for the payment terminal identified in the path.
The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal settings read
* Management API—Terminal settings read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_terminals_terminal_id_terminal_logos(self,
                                            terminal_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_id` | `str` | Template, Required | The unique identifier of the payment terminal. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Logo`](../../doc/models/logo.md).

## Example Usage

```python
terminal_id = 'terminalId2'

result = terminal_settings_terminal_level_api.get_terminals_terminal_id_terminal_logos(terminal_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": "BASE-64_ENCODED_STRING"
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


# Patch-Terminals-Terminal Id-Terminal Logos

Updates the logo for the payment terminal identified in the path.

* To change the logo, specify the image file as a Base64-encoded string.
* To restore the logo inherited from a higher level (store, merchant account, or company account), specify an empty logo value.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal settings read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def patch_terminals_terminal_id_terminal_logos(self,
                                              terminal_id,
                                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_id` | `str` | Template, Required | The unique identifier of the payment terminal. |
| `body` | [`Logo`](../../doc/models/logo.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Logo`](../../doc/models/logo.md).

## Example Usage

```python
terminal_id = 'terminalId2'

body = Logo(
    data=''
)

result = terminal_settings_terminal_level_api.patch_terminals_terminal_id_terminal_logos(
    terminal_id,
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
  "data": "LOGO_INHERITED_FROM_HIGHER_LEVEL_BASE-64_ENCODED_STRING"
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


# Get-Terminals-Terminal Id-Terminal Settings

Returns the settings that are configured for the payment terminal identified in the path.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal settings read
* Management API—Terminal settings read and write

For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role:

* Management API—Terminal settings Advanced read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_terminals_terminal_id_terminal_settings(self,
                                               terminal_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_id` | `str` | Template, Required | The unique identifier of the payment terminal. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalSettings`](../../doc/models/terminal-settings.md).

## Example Usage

```python
terminal_id = 'terminalId2'

result = terminal_settings_terminal_level_api.get_terminals_terminal_id_terminal_settings(terminal_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "cardholderReceipt": {
    "headerForAuthorizedReceipt": "header1,header2,filler"
  },
  "gratuities": [
    {
      "currency": "EUR",
      "usePredefinedTipEntries": true,
      "predefinedTipEntries": [
        "100",
        "1%",
        "5%"
      ],
      "allowCustomAmount": true
    }
  ],
  "nexo": {
    "displayUrls": {
      "localUrls": [
        {
          "password": "BASIC_AUTH_PASSWORD",
          "url": "https://your-display-notifications-endpoint.com",
          "username": "BASIC_AUTH_USERNAME"
        }
      ]
    },
    "encryptionKey": {
      "identifier": "KEY_IDENTIFIER",
      "passphrase": "KEY_PASSPHRASE",
      "version": 1
    },
    "eventUrls": {
      "eventPublicUrls": [
        {
          "password": "BASIC_AUTH_PASSWORD",
          "url": "https://your-event-notifications-endpoint.com",
          "username": "BASIC_AUTH_USERNAME"
        }
      ]
    },
    "notification": {
      "showButton": true
    }
  },
  "opi": {
    "enablePayAtTable": true,
    "payAtTableStoreNumber": "1",
    "payAtTableURL": "https:/your-pay-at-table-endpoint.com"
  },
  "offlineProcessing": {
    "chipFloorLimit": 0
  },
  "receiptOptions": {
    "qrCodeData": "http://www.example.com/order/${pspreference}/${merchantreference}"
  },
  "receiptPrinting": {
    "shopperApproved": true,
    "shopperRefused": true,
    "shopperCancelled": true,
    "shopperRefundApproved": true,
    "shopperRefundRefused": true,
    "shopperVoid": true
  },
  "signature": {
    "askSignatureOnScreen": true,
    "skipSignature": false,
    "deviceName": "Amsterdam-236203386"
  },
  "wifiProfiles": {
    "profiles": [
      {
        "authType": "wpa-psk",
        "autoWifi": false,
        "bssType": "infra",
        "channel": 0,
        "defaultProfile": true,
        "hiddenSsid": false,
        "name": "Guest Wi-Fi",
        "psk": "4R8R2R3V456X",
        "ssid": "G470P37660D4G",
        "wsec": "ccmp"
      }
    ],
    "settings": {
      "band": "All",
      "roaming": true
    }
  },
  "timeouts": {
    "fromActiveToSleep": 30
  },
  "hardware": {
    "displayMaximumBackLight": 75,
    "restartHour": 5
  },
  "passcodes": {
    "adminMenuPin": "1234",
    "txMenuPin": "1234",
    "refundPin": "123456",
    "screenLockPin": "1234"
  },
  "connectivity": {
    "simcardStatus": "INVENTORY"
  },
  "storeAndForward": {
    "maxAmount": [
      {
        "amount": 10000,
        "currencyCode": "EUR"
      }
    ],
    "maxPayments": 10,
    "supportedCardTypes": {
      "credit": true,
      "debit": true,
      "deferredDebit": true,
      "prepaid": true,
      "unknown": false
    }
  },
  "terminalInstructions": {
    "adyenAppRestart": true
  }
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


# Patch-Terminals-Terminal Id-Terminal Settings

Updates the settings that are configured for the payment terminal identified in the path.

* To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object.
* To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter.
* Objects that are not included in the request are not updated.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal settings read and write

For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role:

* Management API—Terminal settings Advanced read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def patch_terminals_terminal_id_terminal_settings(self,
                                                 terminal_id,
                                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_id` | `str` | Template, Required | The unique identifier of the payment terminal. |
| `body` | [`TerminalSettings`](../../doc/models/terminal-settings.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalSettings`](../../doc/models/terminal-settings.md).

## Example Usage

```python
terminal_id = 'terminalId2'

body = TerminalSettings(
    wifi_profiles=WifiProfiles(
        profiles=[
            Profile(
                auth_type='wpa-eap',
                bss_type='infra',
                ssid='your-network',
                wsec='ccmp',
                auto_wifi=False,
                channel=0,
                default_profile=True,
                eap='peap',
                eap_ca_cert=File(
                    data='MD1rKS05M2JqRVFNQ...RTtLH1tLWo=',
                    name='eap-peap-ca.pem'
                ),
                eap_identity='admin',
                eap_intermediate_cert=File(
                    data='PD3tUS1CRDdJTiGDR...EFoLS0tLQg=',
                    name='eap-peap-client.pem'
                ),
                eap_pwd='EAP_PEAP_PASSWORD',
                hidden_ssid=False,
                name='Profile-eap-peap-1'
            ),
            Profile(
                auth_type='wpa-psk',
                bss_type='infra',
                ssid='your-network',
                wsec='ccmp',
                auto_wifi=False,
                channel=0,
                default_profile=False,
                hidden_ssid=False,
                name='Profile-guest-wifi',
                psk='WIFI_PASSWORD'
            )
        ],
        settings=Settings(
            band='2.4GHz',
            roaming=True,
            timeout=5
        )
    )
)

result = terminal_settings_terminal_level_api.patch_terminals_terminal_id_terminal_settings(
    terminal_id,
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
  "cardholderReceipt": {
    "headerForAuthorizedReceipt": "header1,header2,filler"
  },
  "gratuities": [
    {
      "currency": "EUR",
      "usePredefinedTipEntries": true,
      "predefinedTipEntries": [
        "100",
        "1%",
        "5%"
      ],
      "allowCustomAmount": true
    }
  ],
  "nexo": {
    "displayUrls": {
      "localUrls": [
        {
          "password": "BASIC_AUTH_PASSWORD",
          "url": "https://your-display-notifications-endpoint.com",
          "username": "BASIC_AUTH_USERNAME"
        }
      ]
    },
    "encryptionKey": {
      "identifier": "KEY_IDENTIFIER",
      "passphrase": "KEY_PASSPHRASE",
      "version": 1
    },
    "eventUrls": {
      "eventPublicUrls": [
        {
          "password": "BASIC_AUTH_PASSWORD",
          "url": "https://your-event-notifications-endpoint.com",
          "username": "BASIC_AUTH_USERNAME"
        }
      ]
    },
    "notification": {
      "showButton": true
    }
  },
  "opi": {
    "enablePayAtTable": true,
    "payAtTableStoreNumber": "1",
    "payAtTableURL": "https:/your-pay-at-table-endpoint.com"
  },
  "offlineProcessing": {
    "chipFloorLimit": 0
  },
  "receiptOptions": {
    "qrCodeData": "http://www.example.com/order/${pspreference}/${merchantreference}"
  },
  "receiptPrinting": {
    "shopperApproved": true,
    "shopperRefused": true,
    "shopperCancelled": true,
    "shopperRefundApproved": true,
    "shopperRefundRefused": true,
    "shopperVoid": true
  },
  "signature": {
    "askSignatureOnScreen": true,
    "skipSignature": false,
    "deviceName": "Amsterdam-236203386"
  },
  "wifiProfiles": {
    "profiles": [
      {
        "authType": "wpa-eap",
        "autoWifi": false,
        "bssType": "infra",
        "channel": 0,
        "defaultProfile": true,
        "eap": "peap",
        "eapCaCert": {
          "data": "MD1rKS05M2JqRVFNQ...RTtLH1tLWo=",
          "name": "eap-peap-ca.pem"
        },
        "eapIdentity": "admin",
        "eapIntermediateCert": {
          "data": "PD3tUS1CRDdJTiGDR...EFoLS0tLQg=",
          "name": "eap-peap-client.pem"
        },
        "eapPwd": "EAP_PEAP_PASSWORD",
        "hiddenSsid": false,
        "name": "Profile-eap-peap-1",
        "ssid": "your-network",
        "wsec": "ccmp"
      },
      {
        "authType": "wpa-psk",
        "autoWifi": false,
        "bssType": "infra",
        "channel": 0,
        "defaultProfile": false,
        "hiddenSsid": false,
        "name": "Profile-guest-wifi",
        "psk": "WIFI_PASSWORD",
        "ssid": "your-network",
        "wsec": "ccmp"
      }
    ],
    "settings": {
      "band": "2.4GHz",
      "roaming": true,
      "timeout": 5
    }
  },
  "timeouts": {
    "fromActiveToSleep": 30
  },
  "hardware": {
    "displayMaximumBackLight": 75,
    "restartHour": 5
  },
  "passcodes": {
    "adminMenuPin": "1234",
    "txMenuPin": "1234",
    "refundPin": "123456",
    "screenLockPin": "1111"
  },
  "connectivity": {
    "simcardStatus": "INVENTORY"
  }
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

