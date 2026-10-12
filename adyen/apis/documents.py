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
from ..errors.delete_documents_id_error import DeleteDocumentsIdErrorBody, delete_documents_id_error_mapper
from ..errors.get_documents_id_error import GetDocumentsIdErrorBody, get_documents_id_error_mapper
from ..errors.patch_documents_id_error import PatchDocumentsIdErrorBody, patch_documents_id_error_mapper
from ..errors.post_documents_error import PostDocumentsErrorBody, post_documents_error_mapper
from ..models.document import Document, DocumentDict
from ..server.server import Server


class Documents:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DocumentsWithRawResponse(client, server, auth)

    def delete_documents_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.delete_documents_id(id_, request_options=request_options))

    def get_documents_id(
        self, id_: str, *, skip_content: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Document:
        """Returns a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document.
            skip_content: Do not load document content while fetching the document.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_documents_id(id_, skip_content=skip_content, request_options=request_options)
        )

    def patch_documents_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Document:
        """Updates a document.

        >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be updated.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the document. Requested verification codes can only be used in your test environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.patch_documents_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    def post_documents(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Document:
        """Uploads a document for verification checks.

        Adyen uses the information from the `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__ to run automated verification
        checks. If these checks fail, you will be notified to provide additional documents.

         You should only upload documents when Adyen requests additional information for the legal entity.

         >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_documents(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> DocumentsWithRawResponse:
        return self._with_raw_response


class AsyncDocuments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDocumentsWithRawResponse(client, server, auth)

    async def delete_documents_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.delete_documents_id(id_, request_options=request_options))

    async def get_documents_id(
        self, id_: str, *, skip_content: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Document:
        """Returns a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document.
            skip_content: Do not load document content while fetching the document.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_documents_id(
                id_, skip_content=skip_content, request_options=request_options
            ),
        )

    async def patch_documents_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Document:
        """Updates a document.

        >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be updated.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the document. Requested verification codes can only be used in your test environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_documents_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    async def post_documents(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Document:
        """Uploads a document for verification checks.

        Adyen uses the information from the `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__ to run automated verification
        checks. If these checks fail, you will be notified to provide additional documents.

         You should only upload documents when Adyen requests additional information for the legal entity.

         >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_documents(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncDocumentsWithRawResponse:
        return self._with_raw_response


class DocumentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_documents_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteDocumentsIdErrorBody]:
        """Deletes a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_documents_id_error_mapper,
            request_options=request_options,
        )

    def get_documents_id(
        self, id_: str, *, skip_content: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Document, GetDocumentsIdErrorBody]:
        """Returns a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document.
            skip_content: Do not load document content while fetching the document.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[bool | None]("skipContent", skip_content)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Document],
            error_mapper=get_documents_id_error_mapper,
            request_options=request_options,
        )

    def patch_documents_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Document, PatchDocumentsIdErrorBody]:
        """Updates a document.

        >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be updated.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the document. Requested verification codes can only be used in your test environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Document | DocumentDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Document],
            error_mapper=patch_documents_id_error_mapper,
            request_options=request_options,
        )

    def post_documents(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Document, PostDocumentsErrorBody]:
        """Uploads a document for verification checks.

        Adyen uses the information from the `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__ to run automated verification
        checks. If these checks fail, you will be notified to provide additional documents.

         You should only upload documents when Adyen requests additional information for the legal entity.

         >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/documents"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Document | DocumentDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[Document],
            error_mapper=post_documents_error_mapper,
            request_options=request_options,
        )


class AsyncDocumentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_documents_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteDocumentsIdErrorBody]:
        """Deletes a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_documents_id_error_mapper,
            request_options=request_options,
        )

    async def get_documents_id(
        self, id_: str, *, skip_content: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Document, GetDocumentsIdErrorBody]:
        """Returns a document.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document.
            skip_content: Do not load document content while fetching the document.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            query_params=[param[bool | None]("skipContent", skip_content)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Document],
            error_mapper=get_documents_id_error_mapper,
            request_options=request_options,
        )

    async def patch_documents_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Document, PatchDocumentsIdErrorBody]:
        """Updates a document.

        >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the document to be updated.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the document. Requested verification codes can only be used in your test environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/documents/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Document | DocumentDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Document],
            error_mapper=patch_documents_id_error_mapper,
            request_options=request_options,
        )

    async def post_documents(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: Document | DocumentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Document, PostDocumentsErrorBody]:
        """Uploads a document for verification checks.

        Adyen uses the information from the `legal entity
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities>`__ to run automated verification
        checks. If these checks fail, you will be notified to provide additional documents.

         You should only upload documents when Adyen requests additional information for the legal entity.

         >You can upload a maximum of 15 pages for photo IDs.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            x_requested_verification_code: Use a suberror code as your requested verification code. You can include one
                code at a time in your request header. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/documents"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Document | DocumentDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[Document],
            error_mapper=post_documents_error_mapper,
            request_options=request_options,
        )
