# Cloud device API SDK

[![Built with APIMatic][apimatic-badge]][apimatic-url] [![License: MIT][license-badge]][license-url] [![Python 3.10+][python-badge]][python-url]

The Cloud device API SDK for Python provides access to the Cloud device API REST APIs from Python applications.

> [!TIP]
> **Looking for a specific signature, model, enum, or error type?** This SDK ships a generated
> **[SDK map](sdk-map.md)** -- a lookup index of the SDK's entire Python surface. Consult it before
> scanning the source tree; details under [SDK map](#sdk-map).

With the Cloud device API you can: 
* **Send Terminal API requests to a cloud endpoint**. 
  You can use this communication method when it is not an option to send Terminal API requests over your local network directly to a payment terminal.
* **Check the cloud connection** of a payment terminal or of a device used in a Mobile solution for in-person payments.

## Authentication
Each request to the Cloud device API must be signed with an API key that has the **Cloud Device API** role. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in your test Customer Area and then set this key to the X-API-Key header value. For example:

```
curl
-H 'Content-Type: application/json' 
-H 'X-API-Key: ADYEN_API_KEY' 
...
```

## Usage with Terminal API
When using [cloud communications](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/) for sending and receiving [Terminal API requests](https://docs.adyen.com/api-explorer/terminal-api/latest/overview), your POS system uses the internet to access the cloud and send your Terminal API request to Adyen. Adyen then forwards the request to the payment device. 

The Cloud device API has different endpoints for synchronous or asynchronous cloud communications:
* If your POS system is designed to keep the connection open to wait for the response, use the endpoints ending in `/sync`.

  In the test environment the endpoint for synchronous communication is `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` 

* If your POS system is designed to close the connection so that it can initiate a new request, use the endpoints ending in `/async`. 
  You will then receive the Terminal API response asynchronously in an event notification, which is sent as a webhook to an endpoint set up by you.

  In the test environment the endpoint for asynchronous communication is `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/async`
## Going live
To access the live endpoints, you must generate a new API key with the **Cloud Device API** role in your live Customer Area. 

You must use the data center and live endpoint that is geographically closest to your location: 
* In your Customer Area, go to **Developers** > **API URLs** > **Select a data center** and select the closest data center. 
* Switch to the live endpoint that is geographically closest to your location. See the base URLs below.
### Australia:
https://device-api-live-au.adyen.com

### East Asia:
https://device-api-live-apse.adyen.com

### Europe:
https://device-api-live.adyen.com

### United States:
https://device-api-live-us.adyen.com

## Methods

---

## Installation

Install the Python SDK from PyPI, with whichever package manager your project uses:

```bash
pip install cloud-device-api
```

```bash
uv add cloud-device-api
```

```bash
poetry add cloud-device-api
```

---

## Quick Start

### Synchronous client

Construct `CloudDeviceApiClient` with keyword arguments, and call `close()` when you are done. Every argument is optional; the full list is in the [SDK map](sdk-map.md).

```python
from cloud_device_api import CloudDeviceApiClient
from cloud_device_api.core import BasicAuthCredentials

client = CloudDeviceApiClient(
    api_key_auth="YOUR_API_KEY",
    basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it -- `with CloudDeviceApiClient(...) as client:` closes the pool on exit; see [Best Practices](#best-practices).

`Client` is exported as an alias of `CloudDeviceApiClient`, so `from cloud_device_api import Client` also works.

The SDK accepts every model-typed input in two interchangeable spellings, both type-checked: the typed model, or a plain dict with the same keys -- the `OrDict` and `Model | ModelDict` unions in the [SDK map](sdk-map.md). Pick whichever suits the call site: the dict form needs no import, while the model form adds a keyword-checked constructor and editor completion.

### Asynchronous client

`AsyncCloudDeviceApiClient` mirrors `CloudDeviceApiClient` with **identical method names**, and every endpoint method is a coroutine. It takes the same arguments, with some differences -- for example, the transport argument is `custom_async_http_client`.

```python
from asyncio import run

from cloud_device_api import AsyncCloudDeviceApiClient
from cloud_device_api.core import BasicAuthCredentials


async def main() -> None:
    client = AsyncCloudDeviceApiClient(
        api_key_auth="YOUR_API_KEY",
        basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it -- `async with AsyncCloudDeviceApiClient(...) as client:` closes the pool on exit. Only the async spelling is `aclose`, matching httpx; see [Best Practices](#best-practices).

`AsyncClient` is the exported alias. Each client accepts **only** its own transport argument; passing the other's is a `TypeError` at runtime and an error under mypy.

---

## Usage

Two generated references cover the SDK; each answers a different question:

| Reference | For |
| --- | --- |
| **[API Reference](api-reference.md)** | Usage guidance for a single **parsed** operation: `client.<group>.<operation>(...)` returns the typed payload and raises `ApiError` on any non-2xx, with `.error` the typed error body, or `RawError` for a status the operation does not document. |
| **[Raw API Reference](raw-api-reference.md)** | The same for the **raw** variant: `client.<group>.with_raw_response.<operation>(...)` returns `ApiResult[T, E]` and never raises for an API error. |

Both API references carry every one of the 4 operations, with a sync and an async sample and a parameter table each.

## SDK map

This SDK ships a generated **SDK map** -- [`sdk-map.md`](sdk-map.md) -- a deterministic, lookup-oriented table of contents of the SDK's Python surface, generated by APIMatic alongside this SDK.

Consult the map before scanning or grepping the source: it answers call-level contract questions by lookup, and for anything it does not carry -- model shapes, enum values, an endpoint's route or behavioural prose -- it names the one source file to read. How to read the map itself, including the SDK-wide defaults its rows rely on, is stated at the top of [`sdk-map.md`](sdk-map.md).

## Best Practices

> [!TIP]
> Use a **single `CloudDeviceApiClient` instance** for the lifetime of your application and reuse it across
> all requests. Each instance owns its own connection pool, so an instance per request forfeits
> connection reuse and leaks pools that are never closed.

Match the disposal to the client's lifetime: an application-lifetime client is closed once at shutdown with `close()` / `aclose()`; where the lifetime fits a block, `with CloudDeviceApiClient() as client:` / `async with AsyncCloudDeviceApiClient() as client:` releases it automatically. Both are idempotent, but a closed client is not reusable: the next call raises. The client closes **whatever transport it holds**, including one you supplied via `custom_http_client` / `custom_async_http_client`; if you intend to reuse your own transport across clients, don't hand its lifetime to a `with` block.

## License

This SDK is distributed under the [MIT License][license-url].

---

## Support

Refer to the [API reference](api-reference.md) for detailed information on available operations with code samples.

---

[license-url]: LICENSE
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[apimatic-url]: https://www.apimatic.io
[apimatic-badge]: https://www.apimatic.io/hubfs/Built-with-APIMatic-badge.svg
[python-url]: https://www.python.org/downloads/
[python-badge]: https://img.shields.io/badge/python-3.10%2B-blue.svg
