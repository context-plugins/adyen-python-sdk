from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_grants2_error import GetGrants2ErrorBody, get_grants2_error_mapper
from ..errors.get_grants_grant_id_disbursements_disbursement_id_error import (
    GetGrantsGrantIdDisbursementsDisbursementIdErrorBody,
    get_grants_grant_id_disbursements_disbursement_id_error_mapper,
)
from ..errors.get_grants_grant_id_disbursements_error import (
    GetGrantsGrantIdDisbursementsErrorBody,
    get_grants_grant_id_disbursements_error_mapper,
)
from ..errors.get_grants_grant_id_error import GetGrantsGrantIdErrorBody, get_grants_grant_id_error_mapper
from ..errors.patch_grants_grant_id_disbursements_disbursement_id_error import (
    PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody,
    patch_grants_grant_id_disbursements_disbursement_id_error_mapper,
)
from ..errors.post_grants2_error import PostGrants2ErrorBody, post_grants2_error_mapper
from ..models.capital_grant_info import CapitalGrantInfo, CapitalGrantInfoDict
from ..models.disbursement import Disbursement
from ..models.disbursement_info_update import DisbursementInfoUpdate, DisbursementInfoUpdateDict
from ..models.disbursements import Disbursements
from ..models.grant import Grant
from ..models.grants import Grants
from ..server.server import Server


class GrantsApi:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = GrantsApiWithRawResponse(client, server)

    def get_grants_grant_id(self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Grant:
        """Returns the details of the specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grants_grant_id(grant_id, request_options=request_options).unwrap()

    def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Disbursements:
        """Returns the disbursements of a specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grants_grant_id_disbursements(
            grant_id, request_options=request_options
        ).unwrap()

    def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Disbursement:
        """Returns the details of a disbursement specified in the path.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, request_options=request_options
        ).unwrap()

    def get_grants2(
        self, counterparty_account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Grants:
        """Returns a list of all the grants of a specific account holder.

        Args:
            counterparty_account_holder_id: The unique identifier of the account holder that received the grants.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grants2(
            counterparty_account_holder_id, request_options=request_options
        ).unwrap()

    def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        body: DisbursementInfoUpdate | DisbursementInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Disbursement:
        """Update the percentage of your user's net income that is deducted for repaying the grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.patch_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, body, request_options=request_options
        ).unwrap()

    def post_grants2(
        self,
        *,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Grant:
        """Make a request for a grant on behalf of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.post_grants2(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GrantsApiWithRawResponse:
        return self._with_raw_response


class AsyncGrantsApi:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncGrantsApiWithRawResponse(client, server)

    async def get_grants_grant_id(self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Grant:
        """Returns the details of the specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.get_grants_grant_id(grant_id, request_options=request_options)).unwrap()

    async def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Disbursements:
        """Returns the disbursements of a specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_grants_grant_id_disbursements(grant_id, request_options=request_options)
        ).unwrap()

    async def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Disbursement:
        """Returns the details of a disbursement specified in the path.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_grants_grant_id_disbursements_disbursement_id(
                grant_id, disbursement_id, request_options=request_options
            )
        ).unwrap()

    async def get_grants2(
        self, counterparty_account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Grants:
        """Returns a list of all the grants of a specific account holder.

        Args:
            counterparty_account_holder_id: The unique identifier of the account holder that received the grants.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_grants2(counterparty_account_holder_id, request_options=request_options)
        ).unwrap()

    async def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        body: DisbursementInfoUpdate | DisbursementInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Disbursement:
        """Update the percentage of your user's net income that is deducted for repaying the grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.patch_grants_grant_id_disbursements_disbursement_id(
                grant_id, disbursement_id, body, request_options=request_options
            )
        ).unwrap()

    async def post_grants2(
        self,
        *,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Grant:
        """Make a request for a grant on behalf of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (await self._with_raw_response.post_grants2(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGrantsApiWithRawResponse:
        return self._with_raw_response


class GrantsApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_grants_grant_id(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Grant, GetGrantsGrantIdErrorBody]:
        """Returns the details of the specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}"),
            path_params=[param[str]("grantId", grant_id)],
            decoder=json_decoder[Grant],
            error_mapper=get_grants_grant_id_error_mapper,
            request_options=request_options,
        )

    def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Disbursements, GetGrantsGrantIdDisbursementsErrorBody]:
        """Returns the disbursements of a specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}/disbursements"),
            path_params=[param[str]("grantId", grant_id)],
            decoder=json_decoder[Disbursements],
            error_mapper=get_grants_grant_id_disbursements_error_mapper,
            request_options=request_options,
        )

    def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Disbursement, GetGrantsGrantIdDisbursementsDisbursementIdErrorBody]:
        """Returns the details of a disbursement specified in the path.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}/disbursements/{disbursementId}"),
            path_params=[param[str]("grantId", grant_id), param[str]("disbursementId", disbursement_id)],
            decoder=json_decoder[Disbursement],
            error_mapper=get_grants_grant_id_disbursements_disbursement_id_error_mapper,
            request_options=request_options,
        )

    def get_grants2(
        self, counterparty_account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Grants, GetGrants2ErrorBody]:
        """Returns a list of all the grants of a specific account holder.

        Args:
            counterparty_account_holder_id: The unique identifier of the account holder that received the grants.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants"),
            query_params=[param[str]("counterpartyAccountHolderId", counterparty_account_holder_id)],
            decoder=json_decoder[Grants],
            error_mapper=get_grants2_error_mapper,
            request_options=request_options,
        )

    def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        body: DisbursementInfoUpdate | DisbursementInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Disbursement, PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody]:
        """Update the percentage of your user's net income that is deducted for repaying the grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default15("/grants/{grantId}/disbursements/{disbursementId}"),
            path_params=[param[str]("grantId", grant_id), param[str]("disbursementId", disbursement_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisbursementInfoUpdate | DisbursementInfoUpdateDict](body),
            decoder=json_decoder[Disbursement],
            error_mapper=patch_grants_grant_id_disbursements_disbursement_id_error_mapper,
            request_options=request_options,
        )

    def post_grants2(
        self,
        *,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Grant, PostGrants2ErrorBody]:
        """Make a request for a grant on behalf of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/grants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CapitalGrantInfo | CapitalGrantInfoDict | None](body),
            decoder=json_decoder[Grant],
            error_mapper=post_grants2_error_mapper,
            request_options=request_options,
        )


class AsyncGrantsApiWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_grants_grant_id(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Grant, GetGrantsGrantIdErrorBody]:
        """Returns the details of the specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}"),
            path_params=[param[str]("grantId", grant_id)],
            decoder=json_decoder[Grant],
            error_mapper=get_grants_grant_id_error_mapper,
            request_options=request_options,
        )

    async def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Disbursements, GetGrantsGrantIdDisbursementsErrorBody]:
        """Returns the disbursements of a specified grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}/disbursements"),
            path_params=[param[str]("grantId", grant_id)],
            decoder=json_decoder[Disbursements],
            error_mapper=get_grants_grant_id_disbursements_error_mapper,
            request_options=request_options,
        )

    async def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Disbursement, GetGrantsGrantIdDisbursementsDisbursementIdErrorBody]:
        """Returns the details of a disbursement specified in the path.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants/{grantId}/disbursements/{disbursementId}"),
            path_params=[param[str]("grantId", grant_id), param[str]("disbursementId", disbursement_id)],
            decoder=json_decoder[Disbursement],
            error_mapper=get_grants_grant_id_disbursements_disbursement_id_error_mapper,
            request_options=request_options,
        )

    async def get_grants2(
        self, counterparty_account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Grants, GetGrants2ErrorBody]:
        """Returns a list of all the grants of a specific account holder.

        Args:
            counterparty_account_holder_id: The unique identifier of the account holder that received the grants.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grants"),
            query_params=[param[str]("counterpartyAccountHolderId", counterparty_account_holder_id)],
            decoder=json_decoder[Grants],
            error_mapper=get_grants2_error_mapper,
            request_options=request_options,
        )

    async def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        body: DisbursementInfoUpdate | DisbursementInfoUpdateDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Disbursement, PatchGrantsGrantIdDisbursementsDisbursementIdErrorBody]:
        """Update the percentage of your user's net income that is deducted for repaying the grant.

        Args:
            grant_id: The unique identifier of the grant reference.
            disbursement_id: The unique identifier of the disbursement.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default15("/grants/{grantId}/disbursements/{disbursementId}"),
            path_params=[param[str]("grantId", grant_id), param[str]("disbursementId", disbursement_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisbursementInfoUpdate | DisbursementInfoUpdateDict](body),
            decoder=json_decoder[Disbursement],
            error_mapper=patch_grants_grant_id_disbursements_disbursement_id_error_mapper,
            request_options=request_options,
        )

    async def post_grants2(
        self,
        *,
        body: CapitalGrantInfo | CapitalGrantInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Grant, PostGrants2ErrorBody]:
        """Make a request for a grant on behalf of an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/grants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CapitalGrantInfo | CapitalGrantInfoDict | None](body),
            decoder=json_decoder[Grant],
            error_mapper=post_grants2_error_mapper,
            request_options=request_options,
        )
