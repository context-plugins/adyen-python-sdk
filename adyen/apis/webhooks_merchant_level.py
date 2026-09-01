from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete_merchants_merchant_id_webhooks_webhook_id_error import (
    DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody,
    delete_merchants_merchant_id_webhooks_webhook_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_webhooks_error import (
    GetMerchantsMerchantIdWebhooksErrorBody,
    get_merchants_merchant_id_webhooks_error_mapper,
)
from ..errors.get_merchants_merchant_id_webhooks_webhook_id_error import (
    GetMerchantsMerchantIdWebhooksWebhookIdErrorBody,
    get_merchants_merchant_id_webhooks_webhook_id_error_mapper,
)
from ..errors.patch_merchants_merchant_id_webhooks_webhook_id_error import (
    PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody,
    patch_merchants_merchant_id_webhooks_webhook_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_webhooks_error import (
    PostMerchantsMerchantIdWebhooksErrorBody,
    post_merchants_merchant_id_webhooks_error_mapper,
)
from ..errors.post_merchants_merchant_id_webhooks_webhook_id_generate_hmac_error import (
    PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody,
    post_merchants_merchant_id_webhooks_webhook_id_generate_hmac_error_mapper,
)
from ..errors.post_merchants_merchant_id_webhooks_webhook_id_test_error import (
    PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody,
    post_merchants_merchant_id_webhooks_webhook_id_test_error_mapper,
)
from ..models.create_merchant_webhook_request import CreateMerchantWebhookRequest, CreateMerchantWebhookRequestDict
from ..models.generate_hmac_key_response import GenerateHmacKeyResponse
from ..models.list_webhooks_response import ListWebhooksResponse
from ..models.test_webhook_request import TestWebhookRequest, TestWebhookRequestDict
from ..models.test_webhook_response import TestWebhookResponse
from ..models.update_merchant_webhook_request import UpdateMerchantWebhookRequest, UpdateMerchantWebhookRequestDict
from ..models.webhook import Webhook
from ..server.server import Server


class WebhooksMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhooksMerchantLevelWithRawResponse(client, server, auth)

    def delete_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_merchants_merchant_id_webhooks_webhook_id(
            merchant_id, webhook_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhooksResponse:
        """Lists all webhook configurations for the merchant account.

        > This call does not return webhook configurations for the company account to which the specified merchant
            account belongs. You can see these in your Customer Area under **Developers** > **Webhooks**.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_webhooks(
            merchant_id, page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Webhook:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_webhooks_webhook_id(
            merchant_id, webhook_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_webhooks_webhook_id(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_webhooks_webhook_id(
            merchant_id, webhook_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Subscribe to receive webhook notifications about events related to your merchant account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

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
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_webhooks(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateHmacKeyResponse:
        """Returns an `HMAC key <https://en.wikipedia.org/wiki/HMAC>`__ for the webhook identified in the path. This key
        allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you
        start receiving `HMAC-signed notifications
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures>`__ from
        Adyen. Find out more about how to `verify HMAC signatures
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
            merchant_id, webhook_id, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_webhooks_webhook_id_test(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: TestWebhookRequest | TestWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookResponse:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_webhooks_webhook_id_test(
            merchant_id, webhook_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> WebhooksMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncWebhooksMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhooksMerchantLevelWithRawResponse(client, server, auth)

    async def delete_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_merchants_merchant_id_webhooks_webhook_id(
                merchant_id, webhook_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhooksResponse:
        """Lists all webhook configurations for the merchant account.

        > This call does not return webhook configurations for the company account to which the specified merchant
            account belongs. You can see these in your Customer Area under **Developers** > **Webhooks**.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_webhooks(
                merchant_id, page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Webhook:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_webhooks_webhook_id(
                merchant_id, webhook_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_webhooks_webhook_id(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_merchants_merchant_id_webhooks_webhook_id(
                merchant_id, webhook_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Subscribe to receive webhook notifications about events related to your merchant account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

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
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_webhooks(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateHmacKeyResponse:
        """Returns an `HMAC key <https://en.wikipedia.org/wiki/HMAC>`__ for the webhook identified in the path. This key
        allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you
        start receiving `HMAC-signed notifications
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures>`__ from
        Adyen. Find out more about how to `verify HMAC signatures
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
                merchant_id, webhook_id, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_webhooks_webhook_id_test(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: TestWebhookRequest | TestWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookResponse:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_webhooks_webhook_id_test(
                merchant_id, webhook_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWebhooksMerchantLevelWithRawResponse:
        return self._with_raw_response


class WebhooksMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhooksResponse, GetMerchantsMerchantIdWebhooksErrorBody]:
        """Lists all webhook configurations for the merchant account.

        > This call does not return webhook configurations for the company account to which the specified merchant
            account belongs. You can see these in your Customer Area under **Developers** > **Webhooks**.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListWebhooksResponse],
            error_mapper=get_merchants_merchant_id_webhooks_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Webhook, GetMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=get_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_webhooks_webhook_id(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=patch_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PostMerchantsMerchantIdWebhooksErrorBody]:
        """Subscribe to receive webhook notifications about events related to your merchant account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=post_merchants_merchant_id_webhooks_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateHmacKeyResponse, PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody]:
        """Returns an `HMAC key <https://en.wikipedia.org/wiki/HMAC>`__ for the webhook identified in the path. This key
        allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you
        start receiving `HMAC-signed notifications
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures>`__ from
        Adyen. Find out more about how to `verify HMAC signatures
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}/generateHmac"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateHmacKeyResponse],
            error_mapper=post_merchants_merchant_id_webhooks_webhook_id_generate_hmac_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_webhooks_webhook_id_test(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: TestWebhookRequest | TestWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookResponse, PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody]:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}/test"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestWebhookRequest | TestWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TestWebhookResponse],
            error_mapper=post_merchants_merchant_id_webhooks_webhook_id_test_error_mapper,
            request_options=request_options,
        )


class AsyncWebhooksMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhooksResponse, GetMerchantsMerchantIdWebhooksErrorBody]:
        """Lists all webhook configurations for the merchant account.

        > This call does not return webhook configurations for the company account to which the specified merchant
            account belongs. You can see these in your Customer Area under **Developers** > **Webhooks**.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListWebhooksResponse],
            error_mapper=get_merchants_merchant_id_webhooks_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_webhooks_webhook_id(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Webhook, GetMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=get_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_webhooks_webhook_id(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PatchMerchantsMerchantIdWebhooksWebhookIdErrorBody]:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantWebhookRequest | UpdateMerchantWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=patch_merchants_merchant_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_webhooks(
        self,
        merchant_id: str,
        *,
        body: CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PostMerchantsMerchantIdWebhooksErrorBody]:
        """Subscribe to receive webhook notifications about events related to your merchant account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMerchantWebhookRequest | CreateMerchantWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=post_merchants_merchant_id_webhooks_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(
        self, merchant_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateHmacKeyResponse, PostMerchantsMerchantIdWebhooksWebhookIdGenerateHmacErrorBody]:
        """Returns an `HMAC key <https://en.wikipedia.org/wiki/HMAC>`__ for the webhook identified in the path. This key
        allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you
        start receiving `HMAC-signed notifications
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures>`__ from
        Adyen. Find out more about how to `verify HMAC signatures
        <https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures>`__.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}/generateHmac"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateHmacKeyResponse],
            error_mapper=post_merchants_merchant_id_webhooks_webhook_id_generate_hmac_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_webhooks_webhook_id_test(
        self,
        merchant_id: str,
        webhook_id: str,
        *,
        body: TestWebhookRequest | TestWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookResponse, PostMerchantsMerchantIdWebhooksWebhookIdTestErrorBody]:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/webhooks/{webhookId}/test"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestWebhookRequest | TestWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TestWebhookResponse],
            error_mapper=post_merchants_merchant_id_webhooks_webhook_id_test_error_mapper,
            request_options=request_options,
        )
