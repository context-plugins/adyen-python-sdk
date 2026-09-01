# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [CloudDeviceApiClient](cloud_device_api/client.py)

<details>
<summary><code>def get_merchants_merchant_account_connected_devices(merchant_account: str, *, store: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConnectedDevicesResponse</code></summary>

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
try:
    response = client.get_merchants_merchant_account_connected_devices(merchant_account)
    # TODO: Handle 'response' of type ConnectedDevicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMerchantsMerchantAccountConnectedDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.get_merchants_merchant_account_connected_devices(merchant_account)
    # TODO: Handle 'response' of type ConnectedDevicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMerchantsMerchantAccountConnectedDevicesErrorBody
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

**OnSuccess**: <code>[ConnectedDevicesResponse](cloud_device_api/models/connected_devices_response.py)</code> -- Successful operation

**OnError**: <code>[ApiError](cloud_device_api/core/exceptions.py)&#91;[GetMerchantsMerchantAccountConnectedDevicesErrorBody](cloud_device_api/errors/get_merchants_merchant_account_connected_devices_error.py)&#93;</code>

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
<summary><code>def get_merchants_merchant_account_devices_device_id_status(merchant_account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceStatusResponse</code></summary>

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
try:
    response = client.get_merchants_merchant_account_devices_device_id_status(merchant_account, device_id)
    # TODO: Handle 'response' of type DeviceStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.get_merchants_merchant_account_devices_device_id_status(merchant_account, device_id)
    # TODO: Handle 'response' of type DeviceStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody
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

**OnSuccess**: <code>[DeviceStatusResponse](cloud_device_api/models/device_status_response.py)</code> -- Successful operation

**OnError**: <code>[ApiError](cloud_device_api/core/exceptions.py)&#91;[GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody](cloud_device_api/errors/get_merchants_merchant_account_devices_device_id_status_error.py)&#93;</code>

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
<summary><code>def post_merchants_merchant_account_devices_device_id_async(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.post_merchants_merchant_account_devices_device_id_async(merchant_account, device_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.post_merchants_merchant_account_devices_device_id_async(merchant_account, device_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>str</code> -- OK - the request has succeeded.

**OnError**: <code>[ApiError](cloud_device_api/core/exceptions.py)&#91;[RawError](cloud_device_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_merchants_merchant_account_devices_device_id_sync(merchant_account: str, device_id: str, *, body: str | None = None, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.post_merchants_merchant_account_devices_device_id_sync(merchant_account, device_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.post_merchants_merchant_account_devices_device_id_sync(merchant_account, device_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>str</code> -- OK - the request has succeeded.

**OnError**: <code>[ApiError](cloud_device_api/core/exceptions.py)&#91;[RawError](cloud_device_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

