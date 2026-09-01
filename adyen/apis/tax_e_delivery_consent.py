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
from ..errors.post_legal_entities_id_check_tax_electronic_delivery_consent_error import (
    PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody,
    post_legal_entities_id_check_tax_electronic_delivery_consent_error_mapper,
)
from ..errors.post_legal_entities_id_set_tax_electronic_delivery_consent_error import (
    PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody,
    post_legal_entities_id_set_tax_electronic_delivery_consent_error_mapper,
)
from ..models.check_tax_electronic_delivery_consent_response import CheckTaxElectronicDeliveryConsentResponse
from ..models.set_tax_electronic_delivery_consent_request import (
    SetTaxElectronicDeliveryConsentRequest,
    SetTaxElectronicDeliveryConsentRequestDict,
)
from ..server.server import Server


class TaxEDeliveryConsent:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaxEDeliveryConsentWithRawResponse(client, server, auth)

    def post_legal_entities_id_check_tax_electronic_delivery_consent(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CheckTaxElectronicDeliveryConsentResponse:
        """Returns the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_legal_entities_id_check_tax_electronic_delivery_consent(
            id, request_options=request_options
        ).unwrap()

    def post_legal_entities_id_set_tax_electronic_delivery_consent(
        self,
        id: str,
        *,
        body: SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Set the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_legal_entities_id_set_tax_electronic_delivery_consent(
            id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TaxEDeliveryConsentWithRawResponse:
        return self._with_raw_response


class AsyncTaxEDeliveryConsent:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaxEDeliveryConsentWithRawResponse(client, server, auth)

    async def post_legal_entities_id_check_tax_electronic_delivery_consent(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CheckTaxElectronicDeliveryConsentResponse:
        """Returns the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_legal_entities_id_check_tax_electronic_delivery_consent(
                id, request_options=request_options
            )
        ).unwrap()

    async def post_legal_entities_id_set_tax_electronic_delivery_consent(
        self,
        id: str,
        *,
        body: SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Set the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_legal_entities_id_set_tax_electronic_delivery_consent(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTaxEDeliveryConsentWithRawResponse:
        return self._with_raw_response


class TaxEDeliveryConsentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_legal_entities_id_check_tax_electronic_delivery_consent(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        CheckTaxElectronicDeliveryConsentResponse, PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody
    ]:
        """Returns the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/checkTaxElectronicDeliveryConsent"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CheckTaxElectronicDeliveryConsentResponse],
            error_mapper=post_legal_entities_id_check_tax_electronic_delivery_consent_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_set_tax_electronic_delivery_consent(
        self,
        id: str,
        *,
        body: SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody]:
        """Set the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/setTaxElectronicDeliveryConsent"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None](
                body
            ),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_legal_entities_id_set_tax_electronic_delivery_consent_error_mapper,
            request_options=request_options,
        )


class AsyncTaxEDeliveryConsentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_legal_entities_id_check_tax_electronic_delivery_consent(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        CheckTaxElectronicDeliveryConsentResponse, PostLegalEntitiesIdCheckTaxElectronicDeliveryConsentErrorBody
    ]:
        """Returns the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/checkTaxElectronicDeliveryConsent"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CheckTaxElectronicDeliveryConsentResponse],
            error_mapper=post_legal_entities_id_check_tax_electronic_delivery_consent_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_set_tax_electronic_delivery_consent(
        self,
        id: str,
        *,
        body: SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostLegalEntitiesIdSetTaxElectronicDeliveryConsentErrorBody]:
        """Set the consent status for electronic delivery of tax forms.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity
                ID of the owner. For organizations, this is the ID of the organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/setTaxElectronicDeliveryConsent"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetTaxElectronicDeliveryConsentRequest | SetTaxElectronicDeliveryConsentRequestDict | None](
                body
            ),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_legal_entities_id_set_tax_electronic_delivery_consent_error_mapper,
            request_options=request_options,
        )
