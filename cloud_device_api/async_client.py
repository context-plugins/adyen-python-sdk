from __future__ import annotations

from functools import cached_property
from types import TracebackType
from uuid import UUID, uuid4

from typing_extensions import Self

from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCloudDeviceApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ApiResult,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BaseRawResponse,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    RawError,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    no_auth,
    param,
    raw_error_response,
)
from .errors.get_merchants_merchant_account_connected_devices_error import (
    GetMerchantsMerchantAccountConnectedDevicesErrorBody,
    get_merchants_merchant_account_connected_devices_error_mapper,
)
from .errors.get_merchants_merchant_account_devices_device_id_status_error import (
    GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody,
    get_merchants_merchant_account_devices_device_id_status_error_mapper,
)
from .models.connected_devices_response import ConnectedDevicesResponse
from .models.device_status_response import DeviceStatusResponse
from .server.environment import Environment
from .server.server import Server


class AsyncCloudDeviceApiClient(BaseCloudDeviceApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_auth: str | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "CloudDeviceApiClient/1 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("X-API-Key", api_key_auth) if api_key_auth is not None else no_auth,
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth,
        )

    @cached_property
    def with_raw_response(self) -> AsyncApiWithRawResponse:
        return AsyncApiWithRawResponse(self._raw_client, self._server)

    async def get_merchants_merchant_account_connected_devices(
        self, merchant_account: str, *, store: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ConnectedDevicesResponse:
        """Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified
        merchant account that have an active cloud connection. The ``store`` query parameter limits the list of devices
        to those belonging to a specific store under the specified merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            store: The store ID of the store belonging to the merchant account specified in the path.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self.with_raw_response.get_merchants_merchant_account_connected_devices(
                merchant_account, store=store, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_account_devices_device_id_status(
        self, merchant_account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceStatusResponse:
        """Check if the specified payment terminal or SDK installation ID (in an IPP Mobile solution) has an active
        cloud connection.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the device. For a payment terminal, use the terminal ID in the format
                _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the
                installation ID of the SDK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful operation

        Raises:
            ApiError: Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self.with_raw_response.get_merchants_merchant_account_devices_device_id_status(
                merchant_account, device_id, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_account_devices_device_id_async(
        self,
        merchant_account: str,
        device_id: str,
        *,
        body: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Sends a Terminal API request and receives the response asynchronously.

        The request body is a JSON object containing a Terminal API request. For the structure, see the various request
        types under `Terminal API <https://docs.adyen.com/api-explorer/terminal-api/1/overview>`__.

        A HTTP status code of **200 OK** is returned when the payment device is online and our backend has sent the
        request. The actual Terminal API response is returned as an event notification webhook to your event
        notification endpoint. See `Receiving an asynchronous result
        <https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#async>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the payment device that you send this request to. Must be the same as
                the ``POIID`` in the ``MessageHeader`` of the Terminal API request. In an integration with payment
                terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example,
                **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.post_merchants_merchant_account_devices_device_id_async(
                merchant_account, device_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_account_devices_device_id_sync(
        self,
        merchant_account: str,
        device_id: str,
        *,
        body: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Sends a Terminal API request and receives the response synchronously.

        The request body is a JSON object containing a Terminal API request. For the structure, see the various request
        types under `Terminal API <https://docs.adyen.com/api-explorer/terminal-api/1/overview>`__.

        The response returns a Terminal API response. See `Receiving a synchronous result
        <https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#sync>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the payment device that you send this request to. Must be the same as
                the ``POIID`` in the ``MessageHeader`` of the Terminal API request. In an integration with payment
                terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example,
                **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self.with_raw_response.post_merchants_merchant_account_devices_device_id_sync(
                merchant_account, device_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


class AsyncApiWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_merchants_merchant_account_connected_devices(
        self, merchant_account: str, *, store: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConnectedDevicesResponse, GetMerchantsMerchantAccountConnectedDevicesErrorBody]:
        """Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified
        merchant account that have an active cloud connection. The ``store`` query parameter limits the list of devices
        to those belonging to a specific store under the specified merchant account.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            store: The store ID of the store belonging to the merchant account specified in the path.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/merchants/{merchantAccount}/connectedDevices"),
            path_params=[param[str]("merchantAccount", merchant_account)],
            query_params=[param[str | None]("store", store)],
            decoder=json_decoder[ConnectedDevicesResponse],
            error_mapper=get_merchants_merchant_account_connected_devices_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_account_devices_device_id_status(
        self, merchant_account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceStatusResponse, GetMerchantsMerchantAccountDevicesDeviceIdStatusErrorBody]:
        """Check if the specified payment terminal or SDK installation ID (in an IPP Mobile solution) has an active
        cloud connection.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the device. For a payment terminal, use the terminal ID in the format
                _[terminal model]-[serial number]_, for example, **P400‑123456789**. In a Mobile solution, use the
                installation ID of the SDK.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/merchants/{merchantAccount}/devices/{deviceId}/status"),
            path_params=[param[str]("merchantAccount", merchant_account), param[str]("deviceId", device_id)],
            decoder=json_decoder[DeviceStatusResponse],
            error_mapper=get_merchants_merchant_account_devices_device_id_status_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_account_devices_device_id_async(
        self,
        merchant_account: str,
        device_id: str,
        *,
        body: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, RawError]:
        """Sends a Terminal API request and receives the response asynchronously.

        The request body is a JSON object containing a Terminal API request. For the structure, see the various request
        types under `Terminal API <https://docs.adyen.com/api-explorer/terminal-api/1/overview>`__.

        A HTTP status code of **200 OK** is returned when the payment device is online and our backend has sent the
        request. The actual Terminal API response is returned as an event notification webhook to your event
        notification endpoint. See `Receiving an asynchronous result
        <https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#async>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the payment device that you send this request to. Must be the same as
                the ``POIID`` in the ``MessageHeader`` of the Terminal API request. In an integration with payment
                terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example,
                **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/merchants/{merchantAccount}/devices/{deviceId}/async"),
            path_params=[param[str]("merchantAccount", merchant_account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[str | None](body),
            decoder=json_decoder[str],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_merchants_merchant_account_devices_device_id_sync(
        self,
        merchant_account: str,
        device_id: str,
        *,
        body: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, RawError]:
        """Sends a Terminal API request and receives the response synchronously.

        The request body is a JSON object containing a Terminal API request. For the structure, see the various request
        types under `Terminal API <https://docs.adyen.com/api-explorer/terminal-api/1/overview>`__.

        The response returns a Terminal API response. See `Receiving a synchronous result
        <https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#sync>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:


        * **Cloud Device API role**

        Args:
            merchant_account: The unique identifier of the merchant account.
            device_id: The unique identifier of the payment device that you send this request to. Must be the same as
                the ``POIID`` in the ``MessageHeader`` of the Terminal API request. In an integration with payment
                terminals, use the terminal ID in the format _[terminal model]-[serial number]_, for example,
                **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/merchants/{merchantAccount}/devices/{deviceId}/sync"),
            path_params=[param[str]("merchantAccount", merchant_account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[str | None](body),
            decoder=json_decoder[str],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


AsyncClient = AsyncCloudDeviceApiClient
