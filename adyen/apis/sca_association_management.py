from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete_sca_associations_error import DeleteScaAssociationsErrorBody, delete_sca_associations_error_mapper
from ..errors.get_sca_associations_error import GetScaAssociationsErrorBody, get_sca_associations_error_mapper
from ..errors.patch_sca_associations_error import PatchScaAssociationsErrorBody, patch_sca_associations_error_mapper
from ..models.approve_association_request import ApproveAssociationRequest, ApproveAssociationRequestDict
from ..models.approve_association_response import ApproveAssociationResponse
from ..models.enums.sca_entity_type import ScaEntityTypeOrStr
from ..models.list_associations_response import ListAssociationsResponse
from ..models.remove_association_request import RemoveAssociationRequest, RemoveAssociationRequestDict
from ..server.server import Server


class ScaAssociationManagement:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = ScaAssociationManagementWithRawResponse(client, server)

    def delete_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: RemoveAssociationRequest | RemoveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes one or more SCA associations for a device.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - Successful association deletion.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - Insufficient permissions to process the
                request. Internal Server Error - The server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.delete_sca_associations(
            www_authenticate, body=body, request_options=request_options
        ).unwrap()

    def get_sca_associations(
        self,
        entity_type: ScaEntityTypeOrStr,
        entity_id: str,
        page_size: int,
        page_number: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAssociationsResponse:
        """Returns a paginated list of the SCA devices associated with a specific entity.

        Args:
            entity_type: The type of entity you want to retrieve a list of associations for. Possible values:
                **accountHolder**, **legalEntity** or **paymentInstrument**.
            entity_id: The unique identifier of the entity.
            page_size: The number of items to have on a page. Default: **5**.
            page_number: The index of the page to retrieve. The index of the first page is **0** (zero). Default: **0**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Internal Server
                Error - The server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.get_sca_associations(
            entity_type, entity_id, page_size, page_number, request_options=request_options
        ).unwrap()

    def patch_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: ApproveAssociationRequest | ApproveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApproveAssociationResponse:
        """Approves a previously created association that is in a pending state.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - Successful approval

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - Insufficient permissions to process the
                request. Internal Server Error - The server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_sca_associations(
            www_authenticate, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ScaAssociationManagementWithRawResponse:
        return self._with_raw_response


class AsyncScaAssociationManagement:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncScaAssociationManagementWithRawResponse(client, server)

    async def delete_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: RemoveAssociationRequest | RemoveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes one or more SCA associations for a device.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - Successful association deletion.

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - Insufficient permissions to process the
                request. Internal Server Error - The server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.delete_sca_associations(
                www_authenticate, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_sca_associations(
        self,
        entity_type: ScaEntityTypeOrStr,
        entity_id: str,
        page_size: int,
        page_number: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAssociationsResponse:
        """Returns a paginated list of the SCA devices associated with a specific entity.

        Args:
            entity_type: The type of entity you want to retrieve a list of associations for. Possible values:
                **accountHolder**, **legalEntity** or **paymentInstrument**.
            entity_id: The unique identifier of the entity.
            page_size: The number of items to have on a page. Default: **5**.
            page_number: The index of the page to retrieve. The index of the first page is **0** (zero). Default: **0**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Internal Server
                Error - The server could not process the request. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.get_sca_associations(
                entity_type, entity_id, page_size, page_number, request_options=request_options
            )
        ).unwrap()

    async def patch_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: ApproveAssociationRequest | ApproveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApproveAssociationResponse:
        """Approves a previously created association that is in a pending state.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - Successful approval

        Raises:
            ApiError: Unauthorized - Authentication required. Forbidden - Insufficient permissions to process the
                request. Internal Server Error - The server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_sca_associations(
                www_authenticate, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncScaAssociationManagementWithRawResponse:
        return self._with_raw_response


class ScaAssociationManagementWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: RemoveAssociationRequest | RemoveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteScaAssociationsErrorBody]:
        """Deletes one or more SCA associations for a device.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/scaAssociations"),
            headers=[param[str]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAssociationRequest | RemoveAssociationRequestDict | None](body),
            decoder=empty_response,
            error_mapper=delete_sca_associations_error_mapper,
            request_options=request_options,
        )

    def get_sca_associations(
        self,
        entity_type: ScaEntityTypeOrStr,
        entity_id: str,
        page_size: int,
        page_number: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAssociationsResponse, GetScaAssociationsErrorBody]:
        """Returns a paginated list of the SCA devices associated with a specific entity.

        Args:
            entity_type: The type of entity you want to retrieve a list of associations for. Possible values:
                **accountHolder**, **legalEntity** or **paymentInstrument**.
            entity_id: The unique identifier of the entity.
            page_size: The number of items to have on a page. Default: **5**.
            page_number: The index of the page to retrieve. The index of the first page is **0** (zero). Default: **0**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/scaAssociations"),
            query_params=[
                param[ScaEntityTypeOrStr]("entityType", entity_type),
                param[str]("entityId", entity_id),
                param[int]("pageSize", page_size),
                param[int]("pageNumber", page_number),
            ],
            decoder=json_decoder[ListAssociationsResponse],
            error_mapper=get_sca_associations_error_mapper,
            request_options=request_options,
        )

    def patch_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: ApproveAssociationRequest | ApproveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApproveAssociationResponse, PatchScaAssociationsErrorBody]:
        """Approves a previously created association that is in a pending state.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/scaAssociations"),
            headers=[param[str]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApproveAssociationRequest | ApproveAssociationRequestDict | None](body),
            decoder=json_decoder[ApproveAssociationResponse],
            error_mapper=patch_sca_associations_error_mapper,
            request_options=request_options,
        )


class AsyncScaAssociationManagementWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: RemoveAssociationRequest | RemoveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteScaAssociationsErrorBody]:
        """Deletes one or more SCA associations for a device.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/scaAssociations"),
            headers=[param[str]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveAssociationRequest | RemoveAssociationRequestDict | None](body),
            decoder=empty_response,
            error_mapper=delete_sca_associations_error_mapper,
            request_options=request_options,
        )

    async def get_sca_associations(
        self,
        entity_type: ScaEntityTypeOrStr,
        entity_id: str,
        page_size: int,
        page_number: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAssociationsResponse, GetScaAssociationsErrorBody]:
        """Returns a paginated list of the SCA devices associated with a specific entity.

        Args:
            entity_type: The type of entity you want to retrieve a list of associations for. Possible values:
                **accountHolder**, **legalEntity** or **paymentInstrument**.
            entity_id: The unique identifier of the entity.
            page_size: The number of items to have on a page. Default: **5**.
            page_number: The index of the page to retrieve. The index of the first page is **0** (zero). Default: **0**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/scaAssociations"),
            query_params=[
                param[ScaEntityTypeOrStr]("entityType", entity_type),
                param[str]("entityId", entity_id),
                param[int]("pageSize", page_size),
                param[int]("pageNumber", page_number),
            ],
            decoder=json_decoder[ListAssociationsResponse],
            error_mapper=get_sca_associations_error_mapper,
            request_options=request_options,
        )

    async def patch_sca_associations(
        self,
        www_authenticate: str,
        *,
        body: ApproveAssociationRequest | ApproveAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApproveAssociationResponse, PatchScaAssociationsErrorBody]:
        """Approves a previously created association that is in a pending state.

        Args:
            www_authenticate: The header for authenticating through SCA.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/scaAssociations"),
            headers=[param[str]("WWW-Authenticate", www_authenticate), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApproveAssociationRequest | ApproveAssociationRequestDict | None](body),
            decoder=json_decoder[ApproveAssociationResponse],
            error_mapper=patch_sca_associations_error_mapper,
            request_options=request_options,
        )
