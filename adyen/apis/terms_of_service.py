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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference_error import (
    GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody,
    get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference_error_mapper,
)
from ..errors.get_legal_entities_id_terms_of_service_acceptance_infos_error import (
    GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody,
    get_legal_entities_id_terms_of_service_acceptance_infos_error_mapper,
)
from ..errors.get_legal_entities_id_terms_of_service_status_error import (
    GetLegalEntitiesIdTermsOfServiceStatusErrorBody,
    get_legal_entities_id_terms_of_service_status_error_mapper,
)
from ..errors.patch_legal_entities_id_terms_of_service_termsofservicedocumentid_error import (
    PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody,
    patch_legal_entities_id_terms_of_service_termsofservicedocumentid_error_mapper,
)
from ..errors.post_legal_entities_id_terms_of_service_error import (
    PostLegalEntitiesIdTermsOfServiceErrorBody,
    post_legal_entities_id_terms_of_service_error_mapper,
)
from ..models.accept_terms_of_service_request import AcceptTermsOfServiceRequest, AcceptTermsOfServiceRequestDict
from ..models.accept_terms_of_service_response import AcceptTermsOfServiceResponse
from ..models.calculate_terms_of_service_status_response import CalculateTermsOfServiceStatusResponse
from ..models.get_accepted_terms_of_service_document_response import GetAcceptedTermsOfServiceDocumentResponse
from ..models.get_terms_of_service_acceptance_infos_response import GetTermsOfServiceAcceptanceInfosResponse
from ..models.get_terms_of_service_document_request import (
    GetTermsOfServiceDocumentRequest,
    GetTermsOfServiceDocumentRequestDict,
)
from ..models.get_terms_of_service_document_response import GetTermsOfServiceDocumentResponse
from ..server.server import Server


class TermsOfService:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TermsOfServiceWithRawResponse(client, server, auth)

    def get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
        self,
        id_: str,
        termsofserviceacceptancereference: str,
        *,
        terms_of_service_document_format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAcceptedTermsOfServiceDocumentResponse:
        """Returns the accepted Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorship, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            termsofserviceacceptancereference: An Adyen-generated reference for the accepted Terms of Service.
            terms_of_service_document_format: The format of the Terms of Service document. Possible values: **JSON**,
                **PDF**, or **TXT**
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
            self._with_raw_response.get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
                id_,
                termsofserviceacceptancereference,
                terms_of_service_document_format=terms_of_service_document_format,
                request_options=request_options,
            ),
        )

    def get_legal_entities_id_terms_of_service_acceptance_infos(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTermsOfServiceAcceptanceInfosResponse:
        """Returns Terms of Service information for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            self._with_raw_response.get_legal_entities_id_terms_of_service_acceptance_infos(
                id_, request_options=request_options
            ),
        )

    def get_legal_entities_id_terms_of_service_status(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CalculateTermsOfServiceStatusResponse:
        """Returns the required types of Terms of Service that need to be accepted by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            self._with_raw_response.get_legal_entities_id_terms_of_service_status(id_, request_options=request_options)
        )

    def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
        self,
        id_: str,
        termsofservicedocumentid: str,
        *,
        body: AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcceptTermsOfServiceResponse:
        """Accepts Terms of Service.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization. For legal representatives
                of individuals, this is the ID of the individual.
            termsofservicedocumentid: The unique identifier of the Terms of Service document.
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
            self._with_raw_response.patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
                id_, termsofservicedocumentid, body=body, request_options=request_options
            ),
        )

    def post_legal_entities_id_terms_of_service(
        self,
        id_: str,
        *,
        body: GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTermsOfServiceDocumentResponse:
        """Returns the Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            self._with_raw_response.post_legal_entities_id_terms_of_service(
                id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TermsOfServiceWithRawResponse:
        return self._with_raw_response


class AsyncTermsOfService:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTermsOfServiceWithRawResponse(client, server, auth)

    async def get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
        self,
        id_: str,
        termsofserviceacceptancereference: str,
        *,
        terms_of_service_document_format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAcceptedTermsOfServiceDocumentResponse:
        """Returns the accepted Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorship, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            termsofserviceacceptancereference: An Adyen-generated reference for the accepted Terms of Service.
            terms_of_service_document_format: The format of the Terms of Service document. Possible values: **JSON**,
                **PDF**, or **TXT**
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
            await self._with_raw_response.get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
                id_,
                termsofserviceacceptancereference,
                terms_of_service_document_format=terms_of_service_document_format,
                request_options=request_options,
            ),
        )

    async def get_legal_entities_id_terms_of_service_acceptance_infos(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTermsOfServiceAcceptanceInfosResponse:
        """Returns Terms of Service information for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            await self._with_raw_response.get_legal_entities_id_terms_of_service_acceptance_infos(
                id_, request_options=request_options
            ),
        )

    async def get_legal_entities_id_terms_of_service_status(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CalculateTermsOfServiceStatusResponse:
        """Returns the required types of Terms of Service that need to be accepted by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            await self._with_raw_response.get_legal_entities_id_terms_of_service_status(
                id_, request_options=request_options
            ),
        )

    async def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
        self,
        id_: str,
        termsofservicedocumentid: str,
        *,
        body: AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcceptTermsOfServiceResponse:
        """Accepts Terms of Service.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization. For legal representatives
                of individuals, this is the ID of the individual.
            termsofservicedocumentid: The unique identifier of the Terms of Service document.
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
            await self._with_raw_response.patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
                id_, termsofservicedocumentid, body=body, request_options=request_options
            ),
        )

    async def post_legal_entities_id_terms_of_service(
        self,
        id_: str,
        *,
        body: GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetTermsOfServiceDocumentResponse:
        """Returns the Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
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
            await self._with_raw_response.post_legal_entities_id_terms_of_service(
                id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTermsOfServiceWithRawResponse:
        return self._with_raw_response


class TermsOfServiceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
        self,
        id_: str,
        termsofserviceacceptancereference: str,
        *,
        terms_of_service_document_format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        GetAcceptedTermsOfServiceDocumentResponse,
        GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody,
    ]:
        """Returns the accepted Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorship, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            termsofserviceacceptancereference: An Adyen-generated reference for the accepted Terms of Service.
            terms_of_service_document_format: The format of the Terms of Service document. Possible values: **JSON**,
                **PDF**, or **TXT**
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18(
                "/legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference}"
            ),
            path_params=[
                param[str]("id", id_),
                param[str]("termsofserviceacceptancereference", termsofserviceacceptancereference),
            ],
            query_params=[param[str | None]("termsOfServiceDocumentFormat", terms_of_service_document_format)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetAcceptedTermsOfServiceDocumentResponse],
            error_mapper=get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference_error_mapper,
            request_options=request_options,
        )

    def get_legal_entities_id_terms_of_service_acceptance_infos(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTermsOfServiceAcceptanceInfosResponse, GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody]:
        """Returns Terms of Service information for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/termsOfServiceAcceptanceInfos"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTermsOfServiceAcceptanceInfosResponse],
            error_mapper=get_legal_entities_id_terms_of_service_acceptance_infos_error_mapper,
            request_options=request_options,
        )

    def get_legal_entities_id_terms_of_service_status(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CalculateTermsOfServiceStatusResponse, GetLegalEntitiesIdTermsOfServiceStatusErrorBody]:
        """Returns the required types of Terms of Service that need to be accepted by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/termsOfServiceStatus"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CalculateTermsOfServiceStatusResponse],
            error_mapper=get_legal_entities_id_terms_of_service_status_error_mapper,
            request_options=request_options,
        )

    def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
        self,
        id_: str,
        termsofservicedocumentid: str,
        *,
        body: AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcceptTermsOfServiceResponse, PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody]:
        """Accepts Terms of Service.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization. For legal representatives
                of individuals, this is the ID of the individual.
            termsofservicedocumentid: The unique identifier of the Terms of Service document.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/legalEntities/{id}/termsOfService/{termsofservicedocumentid}"),
            path_params=[param[str]("id", id_), param[str]("termsofservicedocumentid", termsofservicedocumentid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AcceptTermsOfServiceResponse],
            error_mapper=patch_legal_entities_id_terms_of_service_termsofservicedocumentid_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_terms_of_service(
        self,
        id_: str,
        *,
        body: GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTermsOfServiceDocumentResponse, PostLegalEntitiesIdTermsOfServiceErrorBody]:
        """Returns the Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/termsOfService"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetTermsOfServiceDocumentResponse],
            error_mapper=post_legal_entities_id_terms_of_service_error_mapper,
            request_options=request_options,
        )


class AsyncTermsOfServiceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference(
        self,
        id_: str,
        termsofserviceacceptancereference: str,
        *,
        terms_of_service_document_format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        GetAcceptedTermsOfServiceDocumentResponse,
        GetLegalEntitiesIdAcceptedTermsOfServiceDocumentTermsofserviceacceptancereferenceErrorBody,
    ]:
        """Returns the accepted Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorship, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            termsofserviceacceptancereference: An Adyen-generated reference for the accepted Terms of Service.
            terms_of_service_document_format: The format of the Terms of Service document. Possible values: **JSON**,
                **PDF**, or **TXT**
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18(
                "/legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference}"
            ),
            path_params=[
                param[str]("id", id_),
                param[str]("termsofserviceacceptancereference", termsofserviceacceptancereference),
            ],
            query_params=[param[str | None]("termsOfServiceDocumentFormat", terms_of_service_document_format)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetAcceptedTermsOfServiceDocumentResponse],
            error_mapper=get_legal_entities_id_accepted_terms_of_service_document_termsofserviceacceptancereference_error_mapper,
            request_options=request_options,
        )

    async def get_legal_entities_id_terms_of_service_acceptance_infos(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTermsOfServiceAcceptanceInfosResponse, GetLegalEntitiesIdTermsOfServiceAcceptanceInfosErrorBody]:
        """Returns Terms of Service information for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/termsOfServiceAcceptanceInfos"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetTermsOfServiceAcceptanceInfosResponse],
            error_mapper=get_legal_entities_id_terms_of_service_acceptance_infos_error_mapper,
            request_options=request_options,
        )

    async def get_legal_entities_id_terms_of_service_status(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CalculateTermsOfServiceStatusResponse, GetLegalEntitiesIdTermsOfServiceStatusErrorBody]:
        """Returns the required types of Terms of Service that need to be accepted by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/termsOfServiceStatus"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[CalculateTermsOfServiceStatusResponse],
            error_mapper=get_legal_entities_id_terms_of_service_status_error_mapper,
            request_options=request_options,
        )

    async def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(
        self,
        id_: str,
        termsofservicedocumentid: str,
        *,
        body: AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcceptTermsOfServiceResponse, PatchLegalEntitiesIdTermsOfServiceTermsofservicedocumentidErrorBody]:
        """Accepts Terms of Service.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization. For legal representatives
                of individuals, this is the ID of the individual.
            termsofservicedocumentid: The unique identifier of the Terms of Service document.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/legalEntities/{id}/termsOfService/{termsofservicedocumentid}"),
            path_params=[param[str]("id", id_), param[str]("termsofservicedocumentid", termsofservicedocumentid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcceptTermsOfServiceRequest | AcceptTermsOfServiceRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[AcceptTermsOfServiceResponse],
            error_mapper=patch_legal_entities_id_terms_of_service_termsofservicedocumentid_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_terms_of_service(
        self,
        id_: str,
        *,
        body: GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetTermsOfServiceDocumentResponse, PostLegalEntitiesIdTermsOfServiceErrorBody]:
        """Returns the Terms of Service document for a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal
                entity ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/termsOfService"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetTermsOfServiceDocumentRequest | GetTermsOfServiceDocumentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GetTermsOfServiceDocumentResponse],
            error_mapper=post_legal_entities_id_terms_of_service_error_mapper,
            request_options=request_options,
        )
