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
    json_body,
    json_decoder,
    param,
)
from ..errors.post_get_pci_questionnaire_url_error import (
    PostGetPciQuestionnaireUrlErrorBody,
    post_get_pci_questionnaire_url_error_mapper,
)
from ..models.get_pci_url_request import GetPciUrlRequest, GetPciUrlRequestDict
from ..models.get_pci_url_response import GetPciUrlResponse
from ..server.server import Server


class PciComplianceQuestionnairePage:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PciComplianceQuestionnairePageWithRawResponse(client, server, auth)

    def post_get_pci_questionnaire_url(
        self,
        *,
        body: GetPciUrlRequest | GetPciUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPciUrlResponse:
        """Returns a link to a PCI compliance questionnaire that you can send to your account holder.
         > You should only use this endpoint if you have a `partner platform setup
                <https://docs.adyen.com/classic-platforms/platforms-for-partners>`__.

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
        return self._with_raw_response.post_get_pci_questionnaire_url(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PciComplianceQuestionnairePageWithRawResponse:
        return self._with_raw_response


class AsyncPciComplianceQuestionnairePage:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPciComplianceQuestionnairePageWithRawResponse(client, server, auth)

    async def post_get_pci_questionnaire_url(
        self,
        *,
        body: GetPciUrlRequest | GetPciUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPciUrlResponse:
        """Returns a link to a PCI compliance questionnaire that you can send to your account holder.
         > You should only use this endpoint if you have a `partner platform setup
                <https://docs.adyen.com/classic-platforms/platforms-for-partners>`__.

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
        return (
            await self._with_raw_response.post_get_pci_questionnaire_url(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPciComplianceQuestionnairePageWithRawResponse:
        return self._with_raw_response


class PciComplianceQuestionnairePageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_get_pci_questionnaire_url(
        self,
        *,
        body: GetPciUrlRequest | GetPciUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPciUrlResponse, PostGetPciQuestionnaireUrlErrorBody]:
        """Returns a link to a PCI compliance questionnaire that you can send to your account holder.
         > You should only use this endpoint if you have a `partner platform setup
                <https://docs.adyen.com/classic-platforms/platforms-for-partners>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default19("/getPciQuestionnaireUrl"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetPciUrlRequest | GetPciUrlRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciUrlResponse],
            error_mapper=post_get_pci_questionnaire_url_error_mapper,
            request_options=request_options,
        )


class AsyncPciComplianceQuestionnairePageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_get_pci_questionnaire_url(
        self,
        *,
        body: GetPciUrlRequest | GetPciUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPciUrlResponse, PostGetPciQuestionnaireUrlErrorBody]:
        """Returns a link to a PCI compliance questionnaire that you can send to your account holder.
         > You should only use this endpoint if you have a `partner platform setup
                <https://docs.adyen.com/classic-platforms/platforms-for-partners>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default19("/getPciQuestionnaireUrl"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetPciUrlRequest | GetPciUrlRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciUrlResponse],
            error_mapper=post_get_pci_questionnaire_url_error_mapper,
            request_options=request_options,
        )
