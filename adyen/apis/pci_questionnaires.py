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
from ..errors.get_legal_entities_id_pci_questionnaires_error import (
    GetLegalEntitiesIdPciQuestionnairesErrorBody,
    get_legal_entities_id_pci_questionnaires_error_mapper,
)
from ..errors.get_legal_entities_id_pci_questionnaires_pciid_error import (
    GetLegalEntitiesIdPciQuestionnairesPciidErrorBody,
    get_legal_entities_id_pci_questionnaires_pciid_error_mapper,
)
from ..errors.post_legal_entities_id_pci_questionnaires_generate_pci_templates_error import (
    PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody,
    post_legal_entities_id_pci_questionnaires_generate_pci_templates_error_mapper,
)
from ..errors.post_legal_entities_id_pci_questionnaires_sign_pci_templates_error import (
    PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody,
    post_legal_entities_id_pci_questionnaires_sign_pci_templates_error_mapper,
)
from ..errors.post_legal_entities_id_pci_questionnaires_signing_required_error import (
    PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody,
    post_legal_entities_id_pci_questionnaires_signing_required_error_mapper,
)
from ..models.calculate_pci_status_request import CalculatePciStatusRequest, CalculatePciStatusRequestDict
from ..models.calculate_pci_status_response import CalculatePciStatusResponse
from ..models.generate_pci_description_request import GeneratePciDescriptionRequest, GeneratePciDescriptionRequestDict
from ..models.generate_pci_description_response import GeneratePciDescriptionResponse
from ..models.get_pci_questionnaire_infos_response import GetPciQuestionnaireInfosResponse
from ..models.get_pci_questionnaire_response import GetPciQuestionnaireResponse
from ..models.pci_signing_request import PciSigningRequest, PciSigningRequestDict
from ..models.pci_signing_response import PciSigningResponse
from ..server.server import Server


class PciQuestionnaires:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PciQuestionnairesWithRawResponse(client, server, auth)

    def get_legal_entities_id_pci_questionnaires(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPciQuestionnaireInfosResponse:
        """Get a list of signed PCI questionnaires.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.get_legal_entities_id_pci_questionnaires(
            id, request_options=request_options
        ).unwrap()

    def get_legal_entities_id_pci_questionnaires_pciid(
        self, id: str, pciid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPciQuestionnaireResponse:
        """Returns the signed PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the individual who signed the PCI questionnaire.
            pciid: The unique identifier of the signed PCI questionnaire.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.get_legal_entities_id_pci_questionnaires_pciid(
            id, pciid, request_options=request_options
        ).unwrap()

    def post_legal_entities_id_pci_questionnaires_generate_pci_templates(
        self,
        id: str,
        *,
        body: GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeneratePciDescriptionResponse:
        """Generates the required PCI questionnaires based on the user's `salesChannel
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_legal_entities_id_pci_questionnaires_generate_pci_templates(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_legal_entities_id_pci_questionnaires_sign_pci_templates(
        self,
        id: str,
        *,
        body: PciSigningRequest | PciSigningRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PciSigningResponse:
        """Signs the required PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the user that has a contractual relationship with your platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_legal_entities_id_pci_questionnaires_sign_pci_templates(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_legal_entities_id_pci_questionnaires_signing_required(
        self,
        id: str,
        *,
        body: CalculatePciStatusRequest | CalculatePciStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculatePciStatusResponse:
        """Calculate PCI status of a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to calculate PCI status.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_legal_entities_id_pci_questionnaires_signing_required(
            id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PciQuestionnairesWithRawResponse:
        return self._with_raw_response


class AsyncPciQuestionnaires:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPciQuestionnairesWithRawResponse(client, server, auth)

    async def get_legal_entities_id_pci_questionnaires(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPciQuestionnaireInfosResponse:
        """Get a list of signed PCI questionnaires.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.get_legal_entities_id_pci_questionnaires(id, request_options=request_options)
        ).unwrap()

    async def get_legal_entities_id_pci_questionnaires_pciid(
        self, id: str, pciid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPciQuestionnaireResponse:
        """Returns the signed PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the individual who signed the PCI questionnaire.
            pciid: The unique identifier of the signed PCI questionnaire.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.get_legal_entities_id_pci_questionnaires_pciid(
                id, pciid, request_options=request_options
            )
        ).unwrap()

    async def post_legal_entities_id_pci_questionnaires_generate_pci_templates(
        self,
        id: str,
        *,
        body: GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeneratePciDescriptionResponse:
        """Generates the required PCI questionnaires based on the user's `salesChannel
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
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
            await self._with_raw_response.post_legal_entities_id_pci_questionnaires_generate_pci_templates(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_legal_entities_id_pci_questionnaires_sign_pci_templates(
        self,
        id: str,
        *,
        body: PciSigningRequest | PciSigningRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PciSigningResponse:
        """Signs the required PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the user that has a contractual relationship with your platform.
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
            await self._with_raw_response.post_legal_entities_id_pci_questionnaires_sign_pci_templates(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_legal_entities_id_pci_questionnaires_signing_required(
        self,
        id: str,
        *,
        body: CalculatePciStatusRequest | CalculatePciStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculatePciStatusResponse:
        """Calculate PCI status of a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to calculate PCI status.
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
            await self._with_raw_response.post_legal_entities_id_pci_questionnaires_signing_required(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPciQuestionnairesWithRawResponse:
        return self._with_raw_response


class PciQuestionnairesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_legal_entities_id_pci_questionnaires(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPciQuestionnaireInfosResponse, GetLegalEntitiesIdPciQuestionnairesErrorBody]:
        """Get a list of signed PCI questionnaires.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciQuestionnaireInfosResponse],
            error_mapper=get_legal_entities_id_pci_questionnaires_error_mapper,
            request_options=request_options,
        )

    def get_legal_entities_id_pci_questionnaires_pciid(
        self, id: str, pciid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPciQuestionnaireResponse, GetLegalEntitiesIdPciQuestionnairesPciidErrorBody]:
        """Returns the signed PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the individual who signed the PCI questionnaire.
            pciid: The unique identifier of the signed PCI questionnaire.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/{pciid}"),
            path_params=[param[str]("id", id), param[str]("pciid", pciid)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciQuestionnaireResponse],
            error_mapper=get_legal_entities_id_pci_questionnaires_pciid_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_pci_questionnaires_generate_pci_templates(
        self,
        id: str,
        *,
        body: GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeneratePciDescriptionResponse, PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody]:
        """Generates the required PCI questionnaires based on the user's `salesChannel
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/generatePciTemplates"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GeneratePciDescriptionResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_generate_pci_templates_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_pci_questionnaires_sign_pci_templates(
        self,
        id: str,
        *,
        body: PciSigningRequest | PciSigningRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PciSigningResponse, PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody]:
        """Signs the required PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the user that has a contractual relationship with your platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/signPciTemplates"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PciSigningRequest | PciSigningRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PciSigningResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_sign_pci_templates_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_pci_questionnaires_signing_required(
        self,
        id: str,
        *,
        body: CalculatePciStatusRequest | CalculatePciStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculatePciStatusResponse, PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody]:
        """Calculate PCI status of a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to calculate PCI status.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/signingRequired"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculatePciStatusRequest | CalculatePciStatusRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CalculatePciStatusResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_signing_required_error_mapper,
            request_options=request_options,
        )


class AsyncPciQuestionnairesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_legal_entities_id_pci_questionnaires(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPciQuestionnaireInfosResponse, GetLegalEntitiesIdPciQuestionnairesErrorBody]:
        """Get a list of signed PCI questionnaires.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciQuestionnaireInfosResponse],
            error_mapper=get_legal_entities_id_pci_questionnaires_error_mapper,
            request_options=request_options,
        )

    async def get_legal_entities_id_pci_questionnaires_pciid(
        self, id: str, pciid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPciQuestionnaireResponse, GetLegalEntitiesIdPciQuestionnairesPciidErrorBody]:
        """Returns the signed PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the individual who signed the PCI questionnaire.
            pciid: The unique identifier of the signed PCI questionnaire.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/{pciid}"),
            path_params=[param[str]("id", id), param[str]("pciid", pciid)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetPciQuestionnaireResponse],
            error_mapper=get_legal_entities_id_pci_questionnaires_pciid_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_pci_questionnaires_generate_pci_templates(
        self,
        id: str,
        *,
        body: GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeneratePciDescriptionResponse, PostLegalEntitiesIdPciQuestionnairesGeneratePciTemplatesErrorBody]:
        """Generates the required PCI questionnaires based on the user's `salesChannel
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to get PCI questionnaire information.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/generatePciTemplates"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePciDescriptionRequest | GeneratePciDescriptionRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GeneratePciDescriptionResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_generate_pci_templates_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_pci_questionnaires_sign_pci_templates(
        self,
        id: str,
        *,
        body: PciSigningRequest | PciSigningRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PciSigningResponse, PostLegalEntitiesIdPciQuestionnairesSignPciTemplatesErrorBody]:
        """Signs the required PCI questionnaire.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The legal entity ID of the user that has a contractual relationship with your platform.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/signPciTemplates"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PciSigningRequest | PciSigningRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PciSigningResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_sign_pci_templates_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_pci_questionnaires_signing_required(
        self,
        id: str,
        *,
        body: CalculatePciStatusRequest | CalculatePciStatusRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculatePciStatusResponse, PostLegalEntitiesIdPciQuestionnairesSigningRequiredErrorBody]:
        """Calculate PCI status of a legal entity.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id: The unique identifier of the legal entity to calculate PCI status.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/pciQuestionnaires/signingRequired"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculatePciStatusRequest | CalculatePciStatusRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CalculatePciStatusResponse],
            error_mapper=post_legal_entities_id_pci_questionnaires_signing_required_error_mapper,
            request_options=request_options,
        )
