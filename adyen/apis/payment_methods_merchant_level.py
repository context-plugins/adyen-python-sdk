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
from ..errors.get_merchants_merchant_id_payment_method_settings_error import (
    GetMerchantsMerchantIdPaymentMethodSettingsErrorBody,
    get_merchants_merchant_id_payment_method_settings_error_mapper,
)
from ..errors.get_merchants_merchant_id_payment_method_settings_payment_method_id_error import (
    GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody,
    get_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
)
from ..errors.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error import (
    GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody,
    get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error_mapper,
)
from ..errors.patch_merchants_merchant_id_payment_method_settings_payment_method_id_error import (
    PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody,
    patch_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
)
from ..errors.post_merchants_merchant_id_payment_method_settings_error import (
    PostMerchantsMerchantIdPaymentMethodSettingsErrorBody,
    post_merchants_merchant_id_payment_method_settings_error_mapper,
)
from ..errors.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error import (
    PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody,
    post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error_mapper,
)
from ..models.apple_pay_info import ApplePayInfo, ApplePayInfoDict
from ..models.apple_pay_response_info import ApplePayResponseInfo
from ..models.management_payment_method import ManagementPaymentMethod
from ..models.payment_method_response import PaymentMethodResponse
from ..models.payment_method_setup_info import PaymentMethodSetupInfo, PaymentMethodSetupInfoDict
from ..models.update_payment_method_info import UpdatePaymentMethodInfo, UpdatePaymentMethodInfoDict
from ..server.server import Server


class PaymentMethodsMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentMethodsMerchantLevelWithRawResponse(client, server, auth)

    def get_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        store_id: str | None = None,
        business_line_id: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodResponse:
        """Returns details for all payment methods of the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store for which to return the payment methods.
            business_line_id: The unique identifier of the Business Line for which to return the payment methods.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            page_number: The number of the page to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payment_method_settings(
            merchant_id,
            store_id=store_id,
            business_line_id=business_line_id,
            page_size=page_size,
            page_number=page_number,
            request_options=request_options,
        ).unwrap()

    def get_merchants_merchant_id_payment_method_settings_payment_method_id(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManagementPaymentMethod:
        """Returns details for the merchant account and the payment method identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payment_method_settings_payment_method_id(
            merchant_id, payment_method_id, request_options=request_options
        ).unwrap()

    def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApplePayResponseInfo:
        """Returns all Apple Pay domains that are registered with the merchant account and the payment method identified
        in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
            merchant_id, payment_method_id, request_options=request_options
        ).unwrap()

    def patch_merchants_merchant_id_payment_method_settings_payment_method_id(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagementPaymentMethod:
        """Updates payment method details for the merchant account and the payment method identified in the path.
        Depending the payment method
        https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_merchants_merchant_id_payment_method_settings_payment_method_id(
            merchant_id, payment_method_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        body: PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagementPaymentMethod:
        """Sends a request to add a new payment method to the merchant account identified in the path. Depending the
        payment method
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

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
        return self._with_raw_response.post_merchants_merchant_id_payment_method_settings(
            merchant_id, body=body, request_options=request_options
        ).unwrap()

    def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: ApplePayInfo | ApplePayInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the
        payment method identified in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in/?tab=adyen-certificate-live_1#going-live>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
            merchant_id, payment_method_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentMethodsMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncPaymentMethodsMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentMethodsMerchantLevelWithRawResponse(client, server, auth)

    async def get_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        store_id: str | None = None,
        business_line_id: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentMethodResponse:
        """Returns details for all payment methods of the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store for which to return the payment methods.
            business_line_id: The unique identifier of the Business Line for which to return the payment methods.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            page_number: The number of the page to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payment_method_settings(
                merchant_id,
                store_id=store_id,
                business_line_id=business_line_id,
                page_size=page_size,
                page_number=page_number,
                request_options=request_options,
            )
        ).unwrap()

    async def get_merchants_merchant_id_payment_method_settings_payment_method_id(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManagementPaymentMethod:
        """Returns details for the merchant account and the payment method identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payment_method_settings_payment_method_id(
                merchant_id, payment_method_id, request_options=request_options
            )
        ).unwrap()

    async def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApplePayResponseInfo:
        """Returns all Apple Pay domains that are registered with the merchant account and the payment method identified
        in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
                merchant_id, payment_method_id, request_options=request_options
            )
        ).unwrap()

    async def patch_merchants_merchant_id_payment_method_settings_payment_method_id(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagementPaymentMethod:
        """Updates payment method details for the merchant account and the payment method identified in the path.
        Depending the payment method
        https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
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
            await self._with_raw_response.patch_merchants_merchant_id_payment_method_settings_payment_method_id(
                merchant_id, payment_method_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        body: PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagementPaymentMethod:
        """Sends a request to add a new payment method to the merchant account identified in the path. Depending the
        payment method
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

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
            await self._with_raw_response.post_merchants_merchant_id_payment_method_settings(
                merchant_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: ApplePayInfo | ApplePayInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the
        payment method identified in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in/?tab=adyen-certificate-live_1#going-live>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
                merchant_id, payment_method_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentMethodsMerchantLevelWithRawResponse:
        return self._with_raw_response


class PaymentMethodsMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        store_id: str | None = None,
        business_line_id: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodResponse, GetMerchantsMerchantIdPaymentMethodSettingsErrorBody]:
        """Returns details for all payment methods of the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store for which to return the payment methods.
            business_line_id: The unique identifier of the Business Line for which to return the payment methods.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            page_number: The number of the page to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("storeId", store_id),
                param[str | None]("businessLineId", business_line_id),
                param[int | None]("pageSize", page_size),
                param[int | None]("pageNumber", page_number),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentMethodResponse],
            error_mapper=get_merchants_merchant_id_payment_method_settings_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_payment_method_settings_payment_method_id(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManagementPaymentMethod, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]:
        """Returns details for the merchant account and the payment method identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=get_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
            request_options=request_options,
        )

    def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        ApplePayResponseInfo, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody
    ]:
        """Returns all Apple Pay domains that are registered with the merchant account and the payment method identified
        in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApplePayResponseInfo],
            error_mapper=get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error_mapper,
            request_options=request_options,
        )

    def patch_merchants_merchant_id_payment_method_settings_payment_method_id(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagementPaymentMethod, PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]:
        """Updates payment method details for the merchant account and the payment method identified in the path.
        Depending the payment method
        https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=patch_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        body: PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagementPaymentMethod, PostMerchantsMerchantIdPaymentMethodSettingsErrorBody]:
        """Sends a request to add a new payment method to the merchant account identified in the path. Depending the
        payment method
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=post_merchants_merchant_id_payment_method_settings_error_mapper,
            request_options=request_options,
        )

    def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: ApplePayInfo | ApplePayInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody]:
        """Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the
        payment method identified in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in/?tab=adyen-certificate-live_1#going-live>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApplePayInfo | ApplePayInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentMethodsMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        store_id: str | None = None,
        business_line_id: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentMethodResponse, GetMerchantsMerchantIdPaymentMethodSettingsErrorBody]:
        """Returns details for all payment methods of the merchant account identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            store_id: The unique identifier of the store for which to return the payment methods.
            business_line_id: The unique identifier of the Business Line for which to return the payment methods.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            page_number: The number of the page to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            query_params=[
                param[str | None]("storeId", store_id),
                param[str | None]("businessLineId", business_line_id),
                param[int | None]("pageSize", page_size),
                param[int | None]("pageNumber", page_number),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentMethodResponse],
            error_mapper=get_merchants_merchant_id_payment_method_settings_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_payment_method_settings_payment_method_id(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManagementPaymentMethod, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]:
        """Returns details for the merchant account and the payment method identified in the path.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=get_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
            request_options=request_options,
        )

    async def get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(
        self, merchant_id: str, payment_method_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        ApplePayResponseInfo, GetMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdGetApplePayDomainsErrorBody
    ]:
        """Returns all Apple Pay domains that are registered with the merchant account and the payment method identified
        in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApplePayResponseInfo],
            error_mapper=get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains_error_mapper,
            request_options=request_options,
        )

    async def patch_merchants_merchant_id_payment_method_settings_payment_method_id(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagementPaymentMethod, PatchMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdErrorBody]:
        """Updates payment method details for the merchant account and the payment method identified in the path.
        Depending the payment method
        https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}"),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentMethodInfo | UpdatePaymentMethodInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=patch_merchants_merchant_id_payment_method_settings_payment_method_id_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_payment_method_settings(
        self,
        merchant_id: str,
        *,
        body: PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagementPaymentMethod, PostMerchantsMerchantIdPaymentMethodSettingsErrorBody]:
        """Sends a request to add a new payment method to the merchant account identified in the path. Depending the
        payment method
        https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings#request-type,
        you may need to send an additional object required for the payment method.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/merchants/{merchantId}/paymentMethodSettings"),
            path_params=[param[str]("merchantId", merchant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentMethodSetupInfo | PaymentMethodSetupInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ManagementPaymentMethod],
            error_mapper=post_merchants_merchant_id_payment_method_settings_error_mapper,
            request_options=request_options,
        )

    async def post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(
        self,
        merchant_id: str,
        payment_method_id: str,
        *,
        body: ApplePayInfo | ApplePayInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostMerchantsMerchantIdPaymentMethodSettingsPaymentMethodIdAddApplePayDomainsErrorBody]:
        """Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the
        payment method identified in the path. For more information, see `Apple Pay documentation
        <https://docs.adyen.com/payment-methods/apple-pay/web-drop-in/?tab=adyen-certificate-live_1#going-live>`__.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Payment methods read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            payment_method_id: The unique identifier of the payment method.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("paymentMethodId", payment_method_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApplePayInfo | ApplePayInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains_error_mapper,
            request_options=request_options,
        )
