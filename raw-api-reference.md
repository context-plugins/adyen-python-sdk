# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [CloudDeviceApiClient](cloud_device_api/client.py)

<details>
<summary><code>def get_merchants_merchant_account_connected_devices(merchant_account: str, *, store: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectedDevicesResponse, GetMerchantsMerchantAccountConnectedDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified merchant account that have an active cloud connection.  The `store` query parameter limits the list of devices to those belonging to a specific store under the specified merchant account. 

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):


* **Cloud Device API role**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_merchants_merchant_account_connected_devices(merchant_account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectedDevicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMerchantsMerchantAccountConnectedDevicesErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.get_merchants_merchant_account_connected_devices(merchant_account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectedDevicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMerchantsMerchantAccountConnectedDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_account</code> | <code>str</code> | The unique identifier of the merchant account. |
| <code>store</code> | <code>str \| None</code> | The store ID of the store belonging to the merchant account specified in the path.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cloud_device_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cloud_device_api/core/results.py)&#91;[ConnectedDevicesResponse](cloud_device_api/models/connected_devices_response.py), [GetMerchantsMerchantAccountConnectedDevicesErrorBody](cloud_device_api/errors/get_merchants_merchant_account_connected_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectedDevicesResponse](cloud_device_api/models/connected_devices_response.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[GetMerchantsMerchantAccountConnectedDevicesErrorBody](cloud_device_api/errors/get_merchants_merchant_account_connected_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403 | <code>[DefaultErrorResponseEntity](cloud_device_api/models/default_error_response_entity.py)</code> |
| anything unmapped | <code>[RawError](cloud_device_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_merchants_merchant_account_devices_device_id_status(merchant_account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceStatusResponse, GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check if the specified payment terminal or SDK installation ID (in an IPP Mobile solution) has an active cloud connection.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):


* **Cloud Device API role**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.get_merchants_merchant_account_devices_device_id_status(merchant_account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody
```

**Async**

```python
result = await async_client.with_raw_response.get_merchants_merchant_account_devices_device_id_status(
    merchant_account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_account</code> | <code>str</code> | The unique identifier of the merchant account. |
| <code>device_id</code> | <code>str</code> | The unique identifier of the device. <br><br>For a payment terminal, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**. <br>In a Mobile solution, use the installation ID of the SDK. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cloud_device_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cloud_device_api/core/results.py)&#91;[DeviceStatusResponse](cloud_device_api/models/device_status_response.py), [GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody](cloud_device_api/errors/get_merchants_merchant_account_devices_device_id_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceStatusResponse](cloud_device_api/models/device_status_response.py)</code> -- Successful operation

**On `Failure`**: `error` is <code>[GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody](cloud_device_api/errors/get_merchants_merchant_account_devices_device_id_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403 | <code>[DefaultErrorResponseEntity](cloud_device_api/models/default_error_response_entity.py)</code> |
| anything unmapped | <code>[RawError](cloud_device_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_merchants_merchant_account_devices_device_id_async(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a Terminal API request and receives the response asynchronously.

The request body is a JSON object containing a Terminal API request. For the structure, see the various request types under [Terminal API](https://docs.adyen.com/api-explorer/terminal-api/1/overview).

A HTTP status code of **200 OK** is returned when the payment device is online and our backend has sent the request. The actual Terminal API response is returned as an event notification webhook to your event notification endpoint. See [Receiving an asynchronous result](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#async).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):


* **Cloud Device API role**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.post_merchants_merchant_account_devices_device_id_async(merchant_account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.post_merchants_merchant_account_devices_device_id_async(
    merchant_account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_account</code> | <code>str</code> | The unique identifier of the merchant account. |
| <code>device_id</code> | <code>str</code> | The unique identifier of the payment device that you send this request to. Must be the same as the `POIID` in the `MessageHeader` of the Terminal API request. <br><br>In an integration with payment terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK. |
| <code>body</code> | <code>str \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cloud_device_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cloud_device_api/core/results.py)&#91;str, [RawError](cloud_device_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- OK - the request has succeeded.

**On `Failure`**: `error` is <code>[RawError](cloud_device_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_merchants_merchant_account_devices_device_id_sync(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a Terminal API request and receives the response synchronously.

The request body is a JSON object containing a Terminal API request. For the structure, see the various request types under [Terminal API](https://docs.adyen.com/api-explorer/terminal-api/1/overview).

The response returns a Terminal API response. See [Receiving a synchronous result](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#sync).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):


* **Cloud Device API role**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.with_raw_response.post_merchants_merchant_account_devices_device_id_sync(merchant_account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.post_merchants_merchant_account_devices_device_id_sync(
    merchant_account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_account</code> | <code>str</code> | The unique identifier of the merchant account. |
| <code>device_id</code> | <code>str</code> | The unique identifier of the payment device that you send this request to. Must be the same as the `POIID` in the `MessageHeader` of the Terminal API request. <br><br>In an integration with payment terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK. |
| <code>body</code> | <code>str \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cloud_device_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cloud_device_api/core/results.py)&#91;str, [RawError](cloud_device_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- OK - the request has succeeded.

**On `Failure`**: `error` is <code>[RawError](cloud_device_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

