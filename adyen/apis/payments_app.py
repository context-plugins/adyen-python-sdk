from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_merchants_merchant_id_payments_apps_error import (
    GetMerchantsMerchantIdPaymentsAppsErrorBody,
    get_merchants_merchant_id_payments_apps_error_mapper,
)
from ..errors.get_merchants_merchant_id_stores_store_id_payments_apps_error import (
    GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody,
    get_merchants_merchant_id_stores_store_id_payments_apps_error_mapper,
)
from ..errors.post_merchants_merchant_id_generate_payments_app_boarding_token_error import (
    PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody,
    post_merchants_merchant_id_generate_payments_app_boarding_token_error_mapper,
)
from ..errors.post_merchants_merchant_id_payments_apps_installation_id_revoke_error import (
    PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody,
    post_merchants_merchant_id_payments_apps_installation_id_revoke_error_mapper,
)
from ..errors.post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error import (
    PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody,
    post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error_mapper,
)
from ..models.boarding_token_request import BoardingTokenRequest, BoardingTokenRequestDict
from ..models.boarding_token_response import BoardingTokenResponse
from ..models.payments_app_response import PaymentsAppResponse
from ..server.server import Server


class PaymentsApp:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = PaymentsAppWithRawResponse(client, server)

    def get_merchants_merchant_id_payments_apps(
        self,
        merchant_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentsAppResponse:
        """Returns the list of Payments App instances for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payments_apps(
            merchant_id, statuses=statuses, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_stores_store_id_payments_apps(
        self,
        merchant_id: str,
        store_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentsAppResponse:
        """Returns the list of Payments App instances for the store identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_stores_store_id_payments_apps(
            merchant_id, store_id, statuses=statuses, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoardingTokenResponse:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the merchant
        account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_generate_payments_app_boarding_token(
            merchant_id, body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_payments_apps_installation_id_revoke(
        self, merchant_id: str, installation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Revokes the authentication of the Payments App instance for the ``installationId`` and merchant account
        identified in the path. This call revokes the authentication of the Payments App instance with the
        ``installationId`` identified in the path for both merchant accounts and stores.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            installation_id: The unique identifier of the Payments App instance on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_payments_apps_installation_id_revoke(
            merchant_id, installation_id, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        store_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoardingTokenResponse:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the store
        identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
            merchant_id, store_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentsAppWithRawResponse:
        return self._with_raw_response


class AsyncPaymentsApp:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncPaymentsAppWithRawResponse(client, server)

    async def get_merchants_merchant_id_payments_apps(
        self,
        merchant_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentsAppResponse:
        """Returns the list of Payments App instances for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payments_apps(
                merchant_id, statuses=statuses, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_stores_store_id_payments_apps(
        self,
        merchant_id: str,
        store_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentsAppResponse:
        """Returns the list of Payments App instances for the store identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_stores_store_id_payments_apps(
                merchant_id, store_id, statuses=statuses, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoardingTokenResponse:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the merchant
        account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_generate_payments_app_boarding_token(
                merchant_id, body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_payments_apps_installation_id_revoke(
        self, merchant_id: str, installation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Revokes the authentication of the Payments App instance for the ``installationId`` and merchant account
        identified in the path. This call revokes the authentication of the Payments App instance with the
        ``installationId`` identified in the path for both merchant accounts and stores.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            installation_id: The unique identifier of the Payments App instance on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_payments_apps_installation_id_revoke(
                merchant_id, installation_id, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        store_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BoardingTokenResponse:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the store
        identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
                merchant_id, store_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentsAppWithRawResponse:
        return self._with_raw_response


class PaymentsAppWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_merchants_merchant_id_payments_apps(
        self,
        merchant_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdPaymentsAppsErrorBody]:
        """Returns the list of Payments App instances for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default26("/merchants/{merchantId}/paymentsApps"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("statuses", statuses),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            decoder=json_decoder[PaymentsAppResponse],
            error_mapper=get_merchants_merchant_id_payments_apps_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_stores_store_id_payments_apps(
        self,
        merchant_id: str,
        store_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody]:
        """Returns the list of Payments App instances for the store identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default26("/merchants/{merchantId}/stores/{storeId}/paymentsApps"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            query_params=[
                param[str | None]("statuses", statuses),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            decoder=json_decoder[PaymentsAppResponse],
            error_mapper=get_merchants_merchant_id_stores_store_id_payments_apps_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoardingTokenResponse, PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody]:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the merchant
        account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default26("/merchants/{merchantId}/generatePaymentsAppBoardingToken"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BoardingTokenRequest | BoardingTokenRequestDict](body),
            decoder=json_decoder[BoardingTokenResponse],
            error_mapper=post_merchants_merchant_id_generate_payments_app_boarding_token_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_payments_apps_installation_id_revoke(
        self, merchant_id: str, installation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody]:
        """Revokes the authentication of the Payments App instance for the ``installationId`` and merchant account
        identified in the path. This call revokes the authentication of the Payments App instance with the
        ``installationId`` identified in the path for both merchant accounts and stores.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            installation_id: The unique identifier of the Payments App instance on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default26("/merchants/{merchantId}/paymentsApps/{installationId}/revoke"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("installationId", installation_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=post_merchants_merchant_id_payments_apps_installation_id_revoke_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        store_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        BoardingTokenResponse, PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody
    ]:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the store
        identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default26(
                "/merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BoardingTokenRequest | BoardingTokenRequestDict](body),
            decoder=json_decoder[BoardingTokenResponse],
            error_mapper=post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentsAppWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_merchants_merchant_id_payments_apps(
        self,
        merchant_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdPaymentsAppsErrorBody]:
        """Returns the list of Payments App instances for the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default26("/merchants/{merchantId}/paymentsApps"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("statuses", statuses),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            decoder=json_decoder[PaymentsAppResponse],
            error_mapper=get_merchants_merchant_id_payments_apps_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_stores_store_id_payments_apps(
        self,
        merchant_id: str,
        store_id: str,
        *,
        statuses: str | None = None,
        limit: int | None = 10,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentsAppResponse, GetMerchantsMerchantIdStoresStoreIdPaymentsAppsErrorBody]:
        """Returns the list of Payments App instances for the store identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            statuses: The status of the Payments App. Comma-separated list of one or more values. If no value is
                provided, the list returns all statuses. Possible values: * **BOARDING** * **BOARDED** * **REVOKED**
            limit: The number of items to return.
            offset: The number of items to skip.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default26("/merchants/{merchantId}/stores/{storeId}/paymentsApps"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            query_params=[
                param[str | None]("statuses", statuses),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            decoder=json_decoder[PaymentsAppResponse],
            error_mapper=get_merchants_merchant_id_stores_store_id_payments_apps_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BoardingTokenResponse, PostMerchantsMerchantIdGeneratePaymentsAppBoardingTokenErrorBody]:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the merchant
        account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default26("/merchants/{merchantId}/generatePaymentsAppBoardingToken"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BoardingTokenRequest | BoardingTokenRequestDict](body),
            decoder=json_decoder[BoardingTokenResponse],
            error_mapper=post_merchants_merchant_id_generate_payments_app_boarding_token_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_payments_apps_installation_id_revoke(
        self, merchant_id: str, installation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, PostMerchantsMerchantIdPaymentsAppsInstallationIdRevokeErrorBody]:
        """Revokes the authentication of the Payments App instance for the ``installationId`` and merchant account
        identified in the path. This call revokes the authentication of the Payments App instance with the
        ``installationId`` identified in the path for both merchant accounts and stores.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            installation_id: The unique identifier of the Payments App instance on a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default26("/merchants/{merchantId}/paymentsApps/{installationId}/revoke"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("installationId", installation_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=post_merchants_merchant_id_payments_apps_installation_id_revoke_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token(
        self,
        merchant_id: str,
        store_id: str,
        body: BoardingTokenRequest | BoardingTokenRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        BoardingTokenResponse, PostMerchantsMerchantIdStoresStoreIdGeneratePaymentsAppBoardingTokenErrorBody
    ]:
        """Creates a boarding token used to authenticate the installation of a Payments App instance on an Android
        device. The boarding token is created for the ``boardingRequestToken`` of the Payments App for the store
        identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Adyen Payments App role

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default26(
                "/merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("storeId", store_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BoardingTokenRequest | BoardingTokenRequestDict](body),
            decoder=json_decoder[BoardingTokenResponse],
            error_mapper=post_merchants_merchant_id_stores_store_id_generate_payments_app_boarding_token_error_mapper,
            request_options=request_options,
        )
