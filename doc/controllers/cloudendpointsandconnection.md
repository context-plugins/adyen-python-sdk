# Cloudendpointsandconnection

```python
cloudendpointsandconnection_api = client.cloudendpointsandconnection
```

## Class Name

`CloudendpointsandconnectionApi`

## Methods

* [Get-Merchants-Merchant Account-Connected Devices](../../doc/controllers/cloudendpointsandconnection.md#get-merchants-merchant-account-connected-devices)
* [Post-Merchants-Merchant Account-Devices-Device Id-Async](../../doc/controllers/cloudendpointsandconnection.md#post-merchants-merchant-account-devices-device-id-async)
* [Get-Merchants-Merchant Account-Devices-Device Id-Status](../../doc/controllers/cloudendpointsandconnection.md#get-merchants-merchant-account-devices-device-id-status)
* [Post-Merchants-Merchant Account-Devices-Device Id-Sync](../../doc/controllers/cloudendpointsandconnection.md#post-merchants-merchant-account-devices-device-id-sync)


# Get-Merchants-Merchant Account-Connected Devices

Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified merchant account that have an active cloud connection.  The `store` query parameter limits the list of devices to those belonging to a specific store under the specified merchant account.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* **Cloud Device API role**

:information_source: **Note** This endpoint does not require authentication.

```python
def get_merchants_merchant_account_connected_devices(self,
                                                    merchant_account,
                                                    store=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Template, Required | The unique identifier of the merchant account. |
| `store` | `str` | Query, Optional | The store ID of the store belonging to the merchant account specified in the path. |

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConnectedDevicesResponse`](../../doc/models/connected-devices-response.md).

## Example Usage

```python
merchant_account = 'merchantAccount8'

result = cloud_endpoints_and_connection_api.get_merchants_merchant_account_connected_devices(merchant_account)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "uniqueDeviceIds": [
    "S1F2-000158215131748",
    "S1F2-000158215131749",
    "S1F2-000158215131750",
    "M400-401972710",
    "M400-401972715",
    "M400-401972720"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`MerchantsConnectedDevices401ErrorException`](../../doc/models/merchants-connected-devices-401-error-exception.md) |
| 403 | Forbidden | [`MerchantsConnectedDevices403ErrorException`](../../doc/models/merchants-connected-devices-403-error-exception.md) |


# Post-Merchants-Merchant Account-Devices-Device Id-Async

Sends a Terminal API request and receives the response asynchronously.

The request body is a JSON object containing a Terminal API request. For the structure, see the various request types under [Terminal API](https://docs.adyen.com/api-explorer/terminal-api/1/overview).

A HTTP status code of **200 OK** is returned when the payment device is online and our backend has sent the request. The actual Terminal API response is returned as an event notification webhook to your event notification endpoint. See [Receiving an asynchronous result](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#async).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* **Cloud Device API role**

:information_source: **Note** This endpoint does not require authentication.

```python
def post_merchants_merchant_account_devices_device_id_async(self,
                                                           merchant_account,
                                                           device_id,
                                                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Template, Required | The unique identifier of the merchant account. |
| `device_id` | `str` | Template, Required | The unique identifier of the payment device that you send this request to. Must be the same as the `POIID` in the `MessageHeader` of the Terminal API request.<br><br>In an integration with payment terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK. |
| `body` | `str` | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
merchant_account = 'merchantAccount8'

device_id = 'deviceId0'

result = cloud_endpoints_and_connection_api.post_merchants_merchant_account_devices_device_id_async(
    merchant_account,
    device_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get-Merchants-Merchant Account-Devices-Device Id-Status

Check if the specified payment terminal or SDK installation ID (in an IPP Mobile solution) has an active cloud connection.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* **Cloud Device API role**

:information_source: **Note** This endpoint does not require authentication.

```python
def get_merchants_merchant_account_devices_device_id_status(self,
                                                           merchant_account,
                                                           device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Template, Required | The unique identifier of the merchant account. |
| `device_id` | `str` | Template, Required | The unique identifier of the device.<br><br>For a payment terminal, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**.<br>In a Mobile solution, use the installation ID of the SDK. |

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeviceStatusResponse`](../../doc/models/device-status-response.md).

## Example Usage

```python
merchant_account = 'merchantAccount8'

device_id = 'deviceId0'

result = cloud_endpoints_and_connection_api.get_merchants_merchant_account_devices_device_id_status(
    merchant_account,
    device_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "deviceId": "AMS1-000168242800763",
  "status": "ONLINE"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`MerchantsDevicesStatus401ErrorException`](../../doc/models/merchants-devices-status-401-error-exception.md) |
| 403 | Forbidden | [`MerchantsDevicesStatus403ErrorException`](../../doc/models/merchants-devices-status-403-error-exception.md) |


# Post-Merchants-Merchant Account-Devices-Device Id-Sync

Sends a Terminal API request and receives the response synchronously.

The request body is a JSON object containing a Terminal API request. For the structure, see the various request types under [Terminal API](https://docs.adyen.com/api-explorer/terminal-api/1/overview).

The response returns a Terminal API response. See [Receiving a synchronous result](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#sync).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* **Cloud Device API role**

:information_source: **Note** This endpoint does not require authentication.

```python
def post_merchants_merchant_account_devices_device_id_sync(self,
                                                          merchant_account,
                                                          device_id,
                                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Template, Required | The unique identifier of the merchant account. |
| `device_id` | `str` | Template, Required | The unique identifier of the payment device that you send this request to. Must be the same as the `POIID` in the `MessageHeader` of the Terminal API request.<br><br>In an integration with payment terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK. |
| `body` | `str` | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
merchant_account = 'merchantAccount8'

device_id = 'deviceId0'

result = cloud_endpoints_and_connection_api.post_merchants_merchant_account_devices_device_id_sync(
    merchant_account,
    device_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

