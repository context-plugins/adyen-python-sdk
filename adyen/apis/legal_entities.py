from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.get_legal_entities_id_business_lines_error import (
    GetLegalEntitiesIdBusinessLinesErrorBody,
    get_legal_entities_id_business_lines_error_mapper,
)
from ..errors.get_legal_entities_id_error import GetLegalEntitiesIdErrorBody, get_legal_entities_id_error_mapper
from ..errors.patch_legal_entities_id_error import PatchLegalEntitiesIdErrorBody, patch_legal_entities_id_error_mapper
from ..errors.post_legal_entities_error import PostLegalEntitiesErrorBody, post_legal_entities_error_mapper
from ..errors.post_legal_entities_id_check_verification_errors_error import (
    PostLegalEntitiesIdCheckVerificationErrorsErrorBody,
    post_legal_entities_id_check_verification_errors_error_mapper,
)
from ..errors.post_legal_entities_id_confirm_data_review_error import (
    PostLegalEntitiesIdConfirmDataReviewErrorBody,
    post_legal_entities_id_confirm_data_review_error_mapper,
)
from ..models.business_lines import BusinessLines
from ..models.data_review_confirmation_response import DataReviewConfirmationResponse
from ..models.legal_entity3 import LegalEntity3
from ..models.legal_entity_info import LegalEntityInfo, LegalEntityInfoDict
from ..models.legal_entity_info_required_type import LegalEntityInfoRequiredType, LegalEntityInfoRequiredTypeDict
from ..models.verification_errors import VerificationErrors
from ..server.server import Server


class LegalEntities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LegalEntitiesWithRawResponse(client, server, auth)

    def get_legal_entities_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> LegalEntity3:
        """Returns a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.get_legal_entities_id(id_, request_options=request_options))

    def get_legal_entities_id_business_lines(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BusinessLines:
        """Returns the business lines owned by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            self._with_raw_response.get_legal_entities_id_business_lines(id_, request_options=request_options)
        )

    def patch_legal_entities_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfo | LegalEntityInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LegalEntity3:
        """Updates a legal entity.

        >To change the legal entity type, include only the new ``type`` in your request.

        If you need to update information for the legal entity, make a separate request. To update the
        ``entityAssociations`` array, you need to replace the entire array.For example, if the array has 3 entries and
        you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the legal entity. Requested verification codes can only be used in your test
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
            self._with_raw_response.patch_legal_entities_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    def post_legal_entities(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LegalEntity3:
        """Creates a legal entity.

        This resource contains information about the user that will be onboarded in your platform. Adyen uses this
        information to perform verification checks as required by payment industry regulations. Adyen informs you of the
        verification results through webhooks or API responses.

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
            self._with_raw_response.post_legal_entities(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    def post_legal_entities_id_check_verification_errors(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerificationErrors:
        """Returns the verification errors for a legal entity and its supporting entities.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            self._with_raw_response.post_legal_entities_id_check_verification_errors(
                id_, request_options=request_options
            ),
        )

    def post_legal_entities_id_confirm_data_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DataReviewConfirmationResponse:
        """Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint
        to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the
        timestamp of when Adyen received the request.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            self._with_raw_response.post_legal_entities_id_confirm_data_review(id_, request_options=request_options)
        )

    def post_legal_entities_id_request_periodic_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Requests a periodic data review for the legal entity of the user specified in the path.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.post_legal_entities_id_request_periodic_review(id_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> LegalEntitiesWithRawResponse:
        return self._with_raw_response


class AsyncLegalEntities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLegalEntitiesWithRawResponse(client, server, auth)

    async def get_legal_entities_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LegalEntity3:
        """Returns a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.get_legal_entities_id(id_, request_options=request_options))

    async def get_legal_entities_id_business_lines(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BusinessLines:
        """Returns the business lines owned by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            await self._with_raw_response.get_legal_entities_id_business_lines(id_, request_options=request_options)
        )

    async def patch_legal_entities_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfo | LegalEntityInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LegalEntity3:
        """Updates a legal entity.

        >To change the legal entity type, include only the new ``type`` in your request.

        If you need to update information for the legal entity, make a separate request. To update the
        ``entityAssociations`` array, you need to replace the entire array.For example, if the array has 3 entries and
        you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the legal entity. Requested verification codes can only be used in your test
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
            await self._with_raw_response.patch_legal_entities_id(
                id_,
                x_requested_verification_code=x_requested_verification_code,
                body=body,
                request_options=request_options,
            ),
        )

    async def post_legal_entities(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LegalEntity3:
        """Creates a legal entity.

        This resource contains information about the user that will be onboarded in your platform. Adyen uses this
        information to perform verification checks as required by payment industry regulations. Adyen informs you of the
        verification results through webhooks or API responses.

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
            await self._with_raw_response.post_legal_entities(
                x_requested_verification_code=x_requested_verification_code, body=body, request_options=request_options
            ),
        )

    async def post_legal_entities_id_check_verification_errors(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VerificationErrors:
        """Returns the verification errors for a legal entity and its supporting entities.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            await self._with_raw_response.post_legal_entities_id_check_verification_errors(
                id_, request_options=request_options
            ),
        )

    async def post_legal_entities_id_confirm_data_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DataReviewConfirmationResponse:
        """Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint
        to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the
        timestamp of when Adyen received the request.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
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
            await self._with_raw_response.post_legal_entities_id_confirm_data_review(
                id_, request_options=request_options
            ),
        )

    async def post_legal_entities_id_request_periodic_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Requests a periodic data review for the legal entity of the user specified in the path.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.post_legal_entities_id_request_periodic_review(
                id_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLegalEntitiesWithRawResponse:
        return self._with_raw_response


class LegalEntitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_legal_entities_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LegalEntity3, GetLegalEntitiesIdErrorBody]:
        """Returns a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[LegalEntity3],
            error_mapper=get_legal_entities_id_error_mapper,
            request_options=request_options,
        )

    def get_legal_entities_id_business_lines(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BusinessLines, GetLegalEntitiesIdBusinessLinesErrorBody]:
        """Returns the business lines owned by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/businessLines"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[BusinessLines],
            error_mapper=get_legal_entities_id_business_lines_error_mapper,
            request_options=request_options,
        )

    def patch_legal_entities_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfo | LegalEntityInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LegalEntity3, PatchLegalEntitiesIdErrorBody]:
        """Updates a legal entity.

        >To change the legal entity type, include only the new ``type`` in your request.

        If you need to update information for the legal entity, make a separate request. To update the
        ``entityAssociations`` array, you need to replace the entire array.For example, if the array has 3 entries and
        you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the legal entity. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/legalEntities/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[LegalEntityInfo | LegalEntityInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[LegalEntity3],
            error_mapper=patch_legal_entities_id_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LegalEntity3, PostLegalEntitiesErrorBody]:
        """Creates a legal entity.

        This resource contains information about the user that will be onboarded in your platform. Adyen uses this
        information to perform verification checks as required by payment industry regulations. Adyen informs you of the
        verification results through webhooks or API responses.

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
            url_template=self._server.default18("/legalEntities"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[LegalEntity3],
            error_mapper=post_legal_entities_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_check_verification_errors(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerificationErrors, PostLegalEntitiesIdCheckVerificationErrorsErrorBody]:
        """Returns the verification errors for a legal entity and its supporting entities.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/checkVerificationErrors"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[VerificationErrors],
            error_mapper=post_legal_entities_id_check_verification_errors_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_confirm_data_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DataReviewConfirmationResponse, PostLegalEntitiesIdConfirmDataReviewErrorBody]:
        """Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint
        to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the
        timestamp of when Adyen received the request.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/confirmDataReview"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DataReviewConfirmationResponse],
            error_mapper=post_legal_entities_id_confirm_data_review_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_request_periodic_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Requests a periodic data review for the legal entity of the user specified in the path.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/requestPeriodicReview"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLegalEntitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_legal_entities_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LegalEntity3, GetLegalEntitiesIdErrorBody]:
        """Returns a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[LegalEntity3],
            error_mapper=get_legal_entities_id_error_mapper,
            request_options=request_options,
        )

    async def get_legal_entities_id_business_lines(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BusinessLines, GetLegalEntitiesIdBusinessLinesErrorBody]:
        """Returns the business lines owned by a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/businessLines"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[BusinessLines],
            error_mapper=get_legal_entities_id_business_lines_error_mapper,
            request_options=request_options,
        )

    async def patch_legal_entities_id(
        self,
        id_: str,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfo | LegalEntityInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LegalEntity3, PatchLegalEntitiesIdErrorBody]:
        """Updates a legal entity.

        >To change the legal entity type, include only the new ``type`` in your request.

        If you need to update information for the legal entity, make a separate request. To update the
        ``entityAssociations`` array, you need to replace the entire array.For example, if the array has 3 entries and
        you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors
                associated with the legal entity. Requested verification codes can only be used in your test
                environment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default18("/legalEntities/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[LegalEntityInfo | LegalEntityInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[LegalEntity3],
            error_mapper=patch_legal_entities_id_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities(
        self,
        *,
        x_requested_verification_code: str | None = None,
        body: LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LegalEntity3, PostLegalEntitiesErrorBody]:
        """Creates a legal entity.

        This resource contains information about the user that will be onboarded in your platform. Adyen uses this
        information to perform verification checks as required by payment industry regulations. Adyen informs you of the
        verification results through webhooks or API responses.

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
            url_template=self._server.default18("/legalEntities"),
            headers=[
                param[str | None]("x-requested-verification-code", x_requested_verification_code),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[LegalEntityInfoRequiredType | LegalEntityInfoRequiredTypeDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[LegalEntity3],
            error_mapper=post_legal_entities_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_check_verification_errors(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VerificationErrors, PostLegalEntitiesIdCheckVerificationErrorsErrorBody]:
        """Returns the verification errors for a legal entity and its supporting entities.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/checkVerificationErrors"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[VerificationErrors],
            error_mapper=post_legal_entities_id_check_verification_errors_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_confirm_data_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DataReviewConfirmationResponse, PostLegalEntitiesIdConfirmDataReviewErrorBody]:
        """Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint
        to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the
        timestamp of when Adyen received the request.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/confirmDataReview"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DataReviewConfirmationResponse],
            error_mapper=post_legal_entities_id_confirm_data_review_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_request_periodic_review(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Requests a periodic data review for the legal entity of the user specified in the path.

        Args:
            id_: The unique identifier of the legal entity.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/requestPeriodicReview"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
