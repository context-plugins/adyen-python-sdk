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
from ..errors.delete_business_lines_id_error import (
    DeleteBusinessLinesIdErrorBody,
    delete_business_lines_id_error_mapper,
)
from ..errors.get_business_lines_id_error import GetBusinessLinesIdErrorBody, get_business_lines_id_error_mapper
from ..errors.patch_business_lines_id_error import PatchBusinessLinesIdErrorBody, patch_business_lines_id_error_mapper
from ..errors.post_business_lines_error import PostBusinessLinesErrorBody, post_business_lines_error_mapper
from ..models.business_line import BusinessLine
from ..models.business_line_info import BusinessLineInfo, BusinessLineInfoDict
from ..models.business_line_info_update import BusinessLineInfoUpdate, BusinessLineInfoUpdateDict
from ..server.server import Server


class BusinessLinesApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BusinessLinesApiWithRawResponse(client, server, auth)

    def delete_business_lines_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a business line.

        >If you delete a business line linked to a `payment method
        <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__, it can affect your
        merchant account's ability to use the `payment method
        <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings>`__.
        The business line is removed from all linked merchant accounts.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.delete_business_lines_id(id, request_options=request_options).unwrap()

    def get_business_lines_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> BusinessLine:
        """Returns the detail of a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.get_business_lines_id(id, request_options=request_options).unwrap()

    def patch_business_lines_id(
        self,
        id: str,
        *,
        body: BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BusinessLine:
        """Updates a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.patch_business_lines_id(id, body=body, request_options=request_options).unwrap()

    def post_business_lines(
        self,
        *,
        body: BusinessLineInfo | BusinessLineInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BusinessLine:
        """Creates a business line.

        This resource contains information about your user's line of business, including their industry and their source
        of funds. Adyen uses this information to verify your users as required by payment industry regulations.Adyen
        informs you of the verification results through webhooks or API responses.

        You can create a maximum of 200 business lines per legal entity for payment processing.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_business_lines(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BusinessLinesApiWithRawResponse:
        return self._with_raw_response


class AsyncBusinessLinesApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBusinessLinesApiWithRawResponse(client, server, auth)

    async def delete_business_lines_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a business line.

        >If you delete a business line linked to a `payment method
        <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__, it can affect your
        merchant account's ability to use the `payment method
        <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings>`__.
        The business line is removed from all linked merchant accounts.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (await self._with_raw_response.delete_business_lines_id(id, request_options=request_options)).unwrap()

    async def get_business_lines_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BusinessLine:
        """Returns the detail of a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (await self._with_raw_response.get_business_lines_id(id, request_options=request_options)).unwrap()

    async def patch_business_lines_id(
        self,
        id: str,
        *,
        body: BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BusinessLine:
        """Updates a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.patch_business_lines_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_business_lines(
        self,
        *,
        body: BusinessLineInfo | BusinessLineInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BusinessLine:
        """Creates a business line.

        This resource contains information about your user's line of business, including their industry and their source
        of funds. Adyen uses this information to verify your users as required by payment industry regulations.Adyen
        informs you of the verification results through webhooks or API responses.

        You can create a maximum of 200 business lines per legal entity for payment processing.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (await self._with_raw_response.post_business_lines(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBusinessLinesApiWithRawResponse:
        return self._with_raw_response


class BusinessLinesApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_business_lines_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBusinessLinesIdErrorBody]:
        """Deletes a business line.

        >If you delete a business line linked to a `payment method
        <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__, it can affect your
        merchant account's ability to use the `payment method
        <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings>`__.
        The business line is removed from all linked merchant accounts.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_business_lines_id_error_mapper,
            request_options=request_options,
        )

    def get_business_lines_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BusinessLine, GetBusinessLinesIdErrorBody]:
        """Returns the detail of a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=get_business_lines_id_error_mapper,
            request_options=request_options,
        )

    def patch_business_lines_id(
        self,
        id: str,
        *,
        body: BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BusinessLine, PatchBusinessLinesIdErrorBody]:
        """Updates a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=patch_business_lines_id_error_mapper,
            request_options=request_options,
        )

    def post_business_lines(
        self,
        *,
        body: BusinessLineInfo | BusinessLineInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BusinessLine, PostBusinessLinesErrorBody]:
        """Creates a business line.

        This resource contains information about your user's line of business, including their industry and their source
        of funds. Adyen uses this information to verify your users as required by payment industry regulations.Adyen
        informs you of the verification results through webhooks or API responses.

        You can create a maximum of 200 business lines per legal entity for payment processing.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/businessLines"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BusinessLineInfo | BusinessLineInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=post_business_lines_error_mapper,
            request_options=request_options,
        )


class AsyncBusinessLinesApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_business_lines_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteBusinessLinesIdErrorBody]:
        """Deletes a business line.

        >If you delete a business line linked to a `payment method
        <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__, it can affect your
        merchant account's ability to use the `payment method
        <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings>`__.
        The business line is removed from all linked merchant accounts.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_business_lines_id_error_mapper,
            request_options=request_options,
        )

    async def get_business_lines_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BusinessLine, GetBusinessLinesIdErrorBody]:
        """Returns the detail of a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=get_business_lines_id_error_mapper,
            request_options=request_options,
        )

    async def patch_business_lines_id(
        self,
        id: str,
        *,
        body: BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BusinessLine, PatchBusinessLinesIdErrorBody]:
        """Updates a business line.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the business line.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/businessLines/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BusinessLineInfoUpdate | BusinessLineInfoUpdateDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=patch_business_lines_id_error_mapper,
            request_options=request_options,
        )

    async def post_business_lines(
        self,
        *,
        body: BusinessLineInfo | BusinessLineInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BusinessLine, PostBusinessLinesErrorBody]:
        """Creates a business line.

        This resource contains information about your user's line of business, including their industry and their source
        of funds. Adyen uses this information to verify your users as required by payment industry regulations.Adyen
        informs you of the verification results through webhooks or API responses.

        You can create a maximum of 200 business lines per legal entity for payment processing.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/businessLines"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BusinessLineInfo | BusinessLineInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLine],
            error_mapper=post_business_lines_error_mapper,
            request_options=request_options,
        )
