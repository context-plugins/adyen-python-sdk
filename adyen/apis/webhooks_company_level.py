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
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_companies_company_id_webhooks_webhook_id_error import (
    DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody,
    delete_companies_company_id_webhooks_webhook_id_error_mapper,
)
from ..errors.get_companies_company_id_webhooks_error import (
    GetCompaniesCompanyIdWebhooksErrorBody,
    get_companies_company_id_webhooks_error_mapper,
)
from ..errors.get_companies_company_id_webhooks_webhook_id_error import (
    GetCompaniesCompanyIdWebhooksWebhookIdErrorBody,
    get_companies_company_id_webhooks_webhook_id_error_mapper,
)
from ..errors.patch_companies_company_id_webhooks_webhook_id_error import (
    PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody,
    patch_companies_company_id_webhooks_webhook_id_error_mapper,
)
from ..errors.post_companies_company_id_webhooks_error import (
    PostCompaniesCompanyIdWebhooksErrorBody,
    post_companies_company_id_webhooks_error_mapper,
)
from ..errors.post_companies_company_id_webhooks_webhook_id_generate_hmac_error import (
    PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody,
    post_companies_company_id_webhooks_webhook_id_generate_hmac_error_mapper,
)
from ..errors.post_companies_company_id_webhooks_webhook_id_test_error import (
    PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody,
    post_companies_company_id_webhooks_webhook_id_test_error_mapper,
)
from ..models.create_company_webhook_request import CreateCompanyWebhookRequest, CreateCompanyWebhookRequestDict
from ..models.generate_hmac_key_response import GenerateHmacKeyResponse
from ..models.list_webhooks_response import ListWebhooksResponse
from ..models.test_company_webhook_request import TestCompanyWebhookRequest, TestCompanyWebhookRequestDict
from ..models.test_webhook_response import TestWebhookResponse
from ..models.update_company_webhook_request import UpdateCompanyWebhookRequest, UpdateCompanyWebhookRequestDict
from ..models.webhook import Webhook
from ..server.server import Server


class WebhooksCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhooksCompanyLevelWithRawResponse(client, server, auth)

    def delete_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.delete_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, request_options=request_options
            ),
        )

    def get_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhooksResponse:
        """Lists all webhook configurations for the company account.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_companies_company_id_webhooks(
                company_id, page_number=page_number, page_size=page_size, request_options=request_options
            ),
        )

    def get_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Webhook:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, request_options=request_options
            ),
        )

    def patch_companies_company_id_webhooks_webhook_id(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.patch_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, body=body, request_options=request_options
            ),
        )

    def post_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        body: CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Subscribe to receive webhook notifications about events related to your company account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_webhooks(
                company_id, body=body, request_options=request_options
            ),
        )

    def post_companies_company_id_webhooks_webhook_id_generate_hmac(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
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
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_webhooks_webhook_id_generate_hmac(
                company_id, webhook_id, request_options=request_options
            ),
        )

    def post_companies_company_id_webhooks_webhook_id_test(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookResponse:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the
        webhook is configured for more than 20 merchant accounts, use the ``merchantIds`` array to specify a subset of
        the merchant accounts for which to send test notifications.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other response fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_webhooks_webhook_id_test(
                company_id, webhook_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WebhooksCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncWebhooksCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhooksCompanyLevelWithRawResponse(client, server, auth)

    async def delete_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, request_options=request_options
            ),
        )

    async def get_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhooksResponse:
        """Lists all webhook configurations for the company account.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_companies_company_id_webhooks(
                company_id, page_number=page_number, page_size=page_size, request_options=request_options
            ),
        )

    async def get_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Webhook:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, request_options=request_options
            ),
        )

    async def patch_companies_company_id_webhooks_webhook_id(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_companies_company_id_webhooks_webhook_id(
                company_id, webhook_id, body=body, request_options=request_options
            ),
        )

    async def post_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        body: CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Webhook:
        """Subscribe to receive webhook notifications about events related to your company account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_webhooks(
                company_id, body=body, request_options=request_options
            ),
        )

    async def post_companies_company_id_webhooks_webhook_id_generate_hmac(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
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
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_webhooks_webhook_id_generate_hmac(
                company_id, webhook_id, request_options=request_options
            ),
        )

    async def post_companies_company_id_webhooks_webhook_id_test(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookResponse:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the
        webhook is configured for more than 20 merchant accounts, use the ``merchantIds`` array to specify a subset of
        the merchant accounts for which to send test notifications.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other response fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_webhooks_webhook_id_test(
                company_id, webhook_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWebhooksCompanyLevelWithRawResponse:
        return self._with_raw_response


class WebhooksCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhooksResponse, GetCompaniesCompanyIdWebhooksErrorBody]:
        """Lists all webhook configurations for the company account.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/webhooks"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListWebhooksResponse],
            error_mapper=get_companies_company_id_webhooks_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Webhook, GetCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=get_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def patch_companies_company_id_webhooks_webhook_id(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=patch_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        body: CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PostCompaniesCompanyIdWebhooksErrorBody]:
        """Subscribe to receive webhook notifications about events related to your company account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Webhook],
            error_mapper=post_companies_company_id_webhooks_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_webhooks_webhook_id_generate_hmac(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateHmacKeyResponse, PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody]:
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
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}/generateHmac"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateHmacKeyResponse],
            error_mapper=post_companies_company_id_webhooks_webhook_id_generate_hmac_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_webhooks_webhook_id_test(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookResponse, PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody]:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the
        webhook is configured for more than 20 merchant accounts, use the ``merchantIds`` array to specify a subset of
        the merchant accounts for which to send test notifications.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other response fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}/test"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TestWebhookResponse],
            error_mapper=post_companies_company_id_webhooks_webhook_id_test_error_mapper,
            request_options=request_options,
        )


class AsyncWebhooksCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Remove the configuration for the webhook identified in the path.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhooksResponse, GetCompaniesCompanyIdWebhooksErrorBody]:
        """Lists all webhook configurations for the company account.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/webhooks"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[param[int | None]("pageNumber", page_number), param[int | None]("pageSize", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ListWebhooksResponse],
            error_mapper=get_companies_company_id_webhooks_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_webhooks_webhook_id(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Webhook, GetCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Returns the configuration for the webhook identified in the path.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Webhook],
            error_mapper=get_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def patch_companies_company_id_webhooks_webhook_id(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PatchCompaniesCompanyIdWebhooksWebhookIdErrorBody]:
        """Make changes to the configuration of the webhook identified in the path. The request contains the new values
        you want to have in the webhook configuration. The response contains the full configuration for the webhook,
        which includes the new values from the request.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCompanyWebhookRequest | UpdateCompanyWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Webhook],
            error_mapper=patch_companies_company_id_webhooks_webhook_id_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_webhooks(
        self,
        company_id: str,
        *,
        body: CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Webhook, PostCompaniesCompanyIdWebhooksErrorBody]:
        """Subscribe to receive webhook notifications about events related to your company account. You can add basic
        authentication to make sure the data is secure.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: Unique identifier of the `company account
                <https://docs.adyen.com/account/account-structure#company-account>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCompanyWebhookRequest | CreateCompanyWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Webhook],
            error_mapper=post_companies_company_id_webhooks_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_webhooks_webhook_id_generate_hmac(
        self, company_id: str, webhook_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateHmacKeyResponse, PostCompaniesCompanyIdWebhooksWebhookIdGenerateHmacErrorBody]:
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
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}/generateHmac"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GenerateHmacKeyResponse],
            error_mapper=post_companies_company_id_webhooks_webhook_id_generate_hmac_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_webhooks_webhook_id_test(
        self,
        company_id: str,
        webhook_id: str,
        *,
        body: TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookResponse, PostCompaniesCompanyIdWebhooksWebhookIdTestErrorBody]:
        """Sends sample notifications to test if the webhook is set up correctly.

        We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the
        webhook is configured for more than 20 merchant accounts, use the ``merchantIds`` array to specify a subset of
        the merchant accounts for which to send test notifications.

        We send four test notifications for each event code you choose. They cover success and failure scenarios for the
        hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom
        notifications, we only send the specified custom notification.

        The response describes the result of the test. The ``status`` field tells you if the test was successful or not.
        You can use the other response fields to troubleshoot unsuccessful tests.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Webhooks read and write

        Args:
            company_id: The unique identifier of the company account.
            webhook_id: Unique identifier of the webhook configuration.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/webhooks/{webhookId}/test"),
            path_params=[param[str]("companyId", company_id), param[str]("webhookId", webhook_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestCompanyWebhookRequest | TestCompanyWebhookRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[TestWebhookResponse],
            error_mapper=post_companies_company_id_webhooks_webhook_id_test_error_mapper,
            request_options=request_options,
        )
