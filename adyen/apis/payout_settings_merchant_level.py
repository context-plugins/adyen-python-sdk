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
from ..errors.delete_merchants_merchant_id_payout_settings_payout_settings_id_error import (
    DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody,
    delete_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_payout_settings_error import (
    GetMerchantsMerchantIdPayoutSettingsErrorBody,
    get_merchants_merchant_id_payout_settings_error_mapper,
)
from ..errors.get_merchants_merchant_id_payout_settings_payout_settings_id_error import (
    GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody,
    get_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
)
from ..errors.patch_merchants_merchant_id_payout_settings_payout_settings_id_error import (
    PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody,
    patch_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_payout_settings_error import (
    PostMerchantsMerchantIdPayoutSettingsErrorBody,
    post_merchants_merchant_id_payout_settings_error_mapper,
)
from ..models.payout_settings import PayoutSettings
from ..models.payout_settings_request import PayoutSettingsRequest, PayoutSettingsRequestDict
from ..models.payout_settings_response import PayoutSettingsResponse
from ..models.update_payout_settings_request import UpdatePayoutSettingsRequest, UpdatePayoutSettingsRequestDict
from ..server.server import Server


class PayoutSettingsMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PayoutSettingsMerchantLevelWithRawResponse(client, server, auth)

    def delete_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_merchants_merchant_id_payout_settings_payout_settings_id(
            merchant_id, payout_settings_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_payout_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PayoutSettingsResponse:
        """Returns the list of payout settings for the merchant account identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payout_settings(
            merchant_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PayoutSettings:
        """Returns the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payout_settings_payout_settings_id(
            merchant_id, payout_settings_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_payout_settings_payout_settings_id(
        self,
        merchant_id: str,
        payout_settings_id: str,
        *,
        body: UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutSettings:
        """Updates the payout setting identified in the path. You can enable or disable the payout setting.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_payout_settings_payout_settings_id(
            merchant_id, payout_settings_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_payout_settings(
        self,
        merchant_id: str,
        *,
        body: PayoutSettingsRequest | PayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutSettings:
        """Sends a request to add a payout setting for the merchant account specified in the path. A payout setting
        links the merchant account to the `transfer instrument
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details
        of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.

        If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant
        account.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_payout_settings(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PayoutSettingsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncPayoutSettingsMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPayoutSettingsMerchantLevelWithRawResponse(client, server, auth)

    async def delete_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_merchants_merchant_id_payout_settings_payout_settings_id(
                merchant_id, payout_settings_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_payout_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PayoutSettingsResponse:
        """Returns the list of payout settings for the merchant account identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payout_settings(
                merchant_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PayoutSettings:
        """Returns the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payout_settings_payout_settings_id(
                merchant_id, payout_settings_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_payout_settings_payout_settings_id(
        self,
        merchant_id: str,
        payout_settings_id: str,
        *,
        body: UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutSettings:
        """Updates the payout setting identified in the path. You can enable or disable the payout setting.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_merchants_merchant_id_payout_settings_payout_settings_id(
                merchant_id, payout_settings_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_payout_settings(
        self,
        merchant_id: str,
        *,
        body: PayoutSettingsRequest | PayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutSettings:
        """Sends a request to add a payout setting for the merchant account specified in the path. A payout setting
        links the merchant account to the `transfer instrument
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details
        of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.

        If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant
        account.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_payout_settings(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPayoutSettingsMerchantLevelWithRawResponse:
        return self._with_raw_response


class PayoutSettingsMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Deletes the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_payout_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutSettingsResponse, GetMerchantsMerchantIdPayoutSettingsErrorBody]:
        """Returns the list of payout settings for the merchant account identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettingsResponse],
            error_mapper=get_merchants_merchant_id_payout_settings_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutSettings, GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Returns the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=get_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_payout_settings_payout_settings_id(
        self,
        merchant_id: str,
        payout_settings_id: str,
        *,
        body: UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutSettings, PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Updates the payout setting identified in the path. You can enable or disable the payout setting.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=patch_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_payout_settings(
        self,
        merchant_id: str,
        *,
        body: PayoutSettingsRequest | PayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutSettings, PostMerchantsMerchantIdPayoutSettingsErrorBody]:
        """Sends a request to add a payout setting for the merchant account specified in the path. A payout setting
        links the merchant account to the `transfer instrument
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details
        of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.

        If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant
        account.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutSettingsRequest | PayoutSettingsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=post_merchants_merchant_id_payout_settings_error_mapper,
            request_options=request_options,
        )


class AsyncPayoutSettingsMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Deletes the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_payout_settings(
        self, merchant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutSettingsResponse, GetMerchantsMerchantIdPayoutSettingsErrorBody]:
        """Returns the list of payout settings for the merchant account identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettingsResponse],
            error_mapper=get_merchants_merchant_id_payout_settings_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_payout_settings_payout_settings_id(
        self, merchant_id: str, payout_settings_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutSettings, GetMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Returns the payout setting identified in the path.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payout account settings read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=get_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_payout_settings_payout_settings_id(
        self,
        merchant_id: str,
        payout_settings_id: str,
        *,
        body: UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutSettings, PatchMerchantsMerchantIdPayoutSettingsPayoutSettingsIdErrorBody]:
        """Updates the payout setting identified in the path. You can enable or disable the payout setting.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payout_settings_id: The unique identifier of the payout setting.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("payoutSettingsId", payout_settings_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePayoutSettingsRequest | UpdatePayoutSettingsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=patch_merchants_merchant_id_payout_settings_payout_settings_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_payout_settings(
        self,
        merchant_id: str,
        *,
        body: PayoutSettingsRequest | PayoutSettingsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutSettings, PostMerchantsMerchantIdPayoutSettingsErrorBody]:
        """Sends a request to add a payout setting for the merchant account specified in the path. A payout setting
        links the merchant account to the `transfer instrument
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details
        of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.

        If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant
        account.

        Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will
        set up your access.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:

        * Management API—Payout account settings read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/payoutSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayoutSettingsRequest | PayoutSettingsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PayoutSettings],
            error_mapper=post_merchants_merchant_id_payout_settings_error_mapper,
            request_options=request_options,
        )
