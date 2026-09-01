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
    json_decoder,
    param,
)
from ..errors.get_companies_company_id_android_apps_error import (
    GetCompaniesCompanyIdAndroidAppsErrorBody,
    get_companies_company_id_android_apps_error_mapper,
)
from ..errors.get_companies_company_id_android_apps_id_error import (
    GetCompaniesCompanyIdAndroidAppsIdErrorBody,
    get_companies_company_id_android_apps_id_error_mapper,
)
from ..errors.get_companies_company_id_android_certificates_error import (
    GetCompaniesCompanyIdAndroidCertificatesErrorBody,
    get_companies_company_id_android_certificates_error_mapper,
)
from ..errors.patch_companies_company_id_android_apps_id_error import (
    PatchCompaniesCompanyIdAndroidAppsIdErrorBody,
    patch_companies_company_id_android_apps_id_error_mapper,
)
from ..errors.post_companies_company_id_android_apps_error import (
    PostCompaniesCompanyIdAndroidAppsErrorBody,
    post_companies_company_id_android_apps_error_mapper,
)
from ..errors.post_companies_company_id_android_certificates_error import (
    PostCompaniesCompanyIdAndroidCertificatesErrorBody,
    post_companies_company_id_android_certificates_error_mapper,
)
from ..models.android_app import AndroidApp
from ..models.android_apps_response import AndroidAppsResponse
from ..models.android_certificates_response import AndroidCertificatesResponse
from ..models.reprocess_android_app_response import ReprocessAndroidAppResponse
from ..models.upload_android_app_response import UploadAndroidAppResponse
from ..models.upload_android_certificate_response import UploadAndroidCertificateResponse
from ..server.server import Server


class AndroidFilesCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AndroidFilesCompanyLevelWithRawResponse(client, server, auth)

    def get_companies_company_id_android_apps(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        package_name: str | None = None,
        version_code: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AndroidAppsResponse:
        """Returns a list of the Android apps that are available for the company identified in the path. These apps have
        been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through `terminal
        actions <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            package_name: The package name that uniquely identifies the Android app.
            version_code: The version number of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_android_apps(
            company_id,
            page_number=page_number,
            page_size=page_size,
            package_name=package_name,
            version_code=version_code,
            request_options=request_options,
        ).unwrap()

    def get_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AndroidApp:
        """Returns the details of the Android app identified in the path. These apps have been uploaded to Adyen and can
        be installed or uninstalled on Android payment terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_android_apps_id(
            company_id, id, request_options=request_options
        ).unwrap()

    def get_companies_company_id_android_certificates(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        certificate_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AndroidCertificatesResponse:
        """Returns a list of the Android certificates that are available for the company identified in the path.
        Typically, these certificates enable running apps on Android payment terminals. The certificates in the list
        have been uploaded to Adyen and can be installed or uninstalled on Android terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            certificate_name: The name of the certificate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_android_certificates(
            company_id,
            page_number=page_number,
            page_size=page_size,
            certificate_name=certificate_name,
            request_options=request_options,
        ).unwrap()

    def patch_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReprocessAndroidAppResponse:
        """Reuploads the Android app identified in the path. To make this request, your API credential must have this
        `role <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_companies_company_id_android_apps_id(
            company_id, id, request_options=request_options
        ).unwrap()

    def post_companies_company_id_android_apps(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAndroidAppResponse:
        """Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API
        credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_companies_company_id_android_apps(
            company_id, request_options=request_options
        ).unwrap()

    def post_companies_company_id_android_certificates(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAndroidCertificateResponse:
        """Uploads an Android Certificate file to Adyen.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_companies_company_id_android_certificates(
            company_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AndroidFilesCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncAndroidFilesCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAndroidFilesCompanyLevelWithRawResponse(client, server, auth)

    async def get_companies_company_id_android_apps(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        package_name: str | None = None,
        version_code: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AndroidAppsResponse:
        """Returns a list of the Android apps that are available for the company identified in the path. These apps have
        been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through `terminal
        actions <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            package_name: The package name that uniquely identifies the Android app.
            version_code: The version number of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_android_apps(
                company_id,
                page_number=page_number,
                page_size=page_size,
                package_name=package_name,
                version_code=version_code,
                request_options=request_options,
            )
        ).unwrap()

    async def get_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AndroidApp:
        """Returns the details of the Android app identified in the path. These apps have been uploaded to Adyen and can
        be installed or uninstalled on Android payment terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_android_apps_id(
                company_id, id, request_options=request_options
            )
        ).unwrap()

    async def get_companies_company_id_android_certificates(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        certificate_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AndroidCertificatesResponse:
        """Returns a list of the Android certificates that are available for the company identified in the path.
        Typically, these certificates enable running apps on Android payment terminals. The certificates in the list
        have been uploaded to Adyen and can be installed or uninstalled on Android terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            certificate_name: The name of the certificate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_android_certificates(
                company_id,
                page_number=page_number,
                page_size=page_size,
                certificate_name=certificate_name,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReprocessAndroidAppResponse:
        """Reuploads the Android app identified in the path. To make this request, your API credential must have this
        `role <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_companies_company_id_android_apps_id(
                company_id, id, request_options=request_options
            )
        ).unwrap()

    async def post_companies_company_id_android_apps(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAndroidAppResponse:
        """Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API
        credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_companies_company_id_android_apps(
                company_id, request_options=request_options
            )
        ).unwrap()

    async def post_companies_company_id_android_certificates(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UploadAndroidCertificateResponse:
        """Uploads an Android Certificate file to Adyen.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_companies_company_id_android_certificates(
                company_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAndroidFilesCompanyLevelWithRawResponse:
        return self._with_raw_response


class AndroidFilesCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_companies_company_id_android_apps(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        package_name: str | None = None,
        version_code: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AndroidAppsResponse, GetCompaniesCompanyIdAndroidAppsErrorBody]:
        """Returns a list of the Android apps that are available for the company identified in the path. These apps have
        been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through `terminal
        actions <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            package_name: The package name that uniquely identifies the Android app.
            version_code: The version number of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidApps"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("packageName", package_name),
                param[int | None]("versionCode", version_code),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidAppsResponse],
            error_mapper=get_companies_company_id_android_apps_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AndroidApp, GetCompaniesCompanyIdAndroidAppsIdErrorBody]:
        """Returns the details of the Android app identified in the path. These apps have been uploaded to Adyen and can
        be installed or uninstalled on Android payment terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidApps/{id}"),
            path_params=[param[str]("companyId", company_id), param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidApp],
            error_mapper=get_companies_company_id_android_apps_id_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_android_certificates(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        certificate_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AndroidCertificatesResponse, GetCompaniesCompanyIdAndroidCertificatesErrorBody]:
        """Returns a list of the Android certificates that are available for the company identified in the path.
        Typically, these certificates enable running apps on Android payment terminals. The certificates in the list
        have been uploaded to Adyen and can be installed or uninstalled on Android terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            certificate_name: The name of the certificate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidCertificates"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("certificateName", certificate_name),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidCertificatesResponse],
            error_mapper=get_companies_company_id_android_certificates_error_mapper,
            request_options=request_options,
        )

    def patch_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReprocessAndroidAppResponse, PatchCompaniesCompanyIdAndroidAppsIdErrorBody]:
        """Reuploads the Android app identified in the path. To make this request, your API credential must have this
        `role <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/androidApps/{id}"),
            path_params=[param[str]("companyId", company_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ReprocessAndroidAppResponse],
            error_mapper=patch_companies_company_id_android_apps_id_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_android_apps(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAndroidAppResponse, PostCompaniesCompanyIdAndroidAppsErrorBody]:
        """Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API
        credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/androidApps"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UploadAndroidAppResponse],
            error_mapper=post_companies_company_id_android_apps_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_android_certificates(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAndroidCertificateResponse, PostCompaniesCompanyIdAndroidCertificatesErrorBody]:
        """Uploads an Android Certificate file to Adyen.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/androidCertificates"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UploadAndroidCertificateResponse],
            error_mapper=post_companies_company_id_android_certificates_error_mapper,
            request_options=request_options,
        )


class AsyncAndroidFilesCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_companies_company_id_android_apps(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        package_name: str | None = None,
        version_code: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AndroidAppsResponse, GetCompaniesCompanyIdAndroidAppsErrorBody]:
        """Returns a list of the Android apps that are available for the company identified in the path. These apps have
        been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through `terminal
        actions <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            package_name: The package name that uniquely identifies the Android app.
            version_code: The version number of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidApps"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("packageName", package_name),
                param[int | None]("versionCode", version_code),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidAppsResponse],
            error_mapper=get_companies_company_id_android_apps_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AndroidApp, GetCompaniesCompanyIdAndroidAppsIdErrorBody]:
        """Returns the details of the Android app identified in the path. These apps have been uploaded to Adyen and can
        be installed or uninstalled on Android payment terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidApps/{id}"),
            path_params=[param[str]("companyId", company_id), param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidApp],
            error_mapper=get_companies_company_id_android_apps_id_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_android_certificates(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        certificate_name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AndroidCertificatesResponse, GetCompaniesCompanyIdAndroidCertificatesErrorBody]:
        """Returns a list of the Android certificates that are available for the company identified in the path.
        Typically, these certificates enable running apps on Android payment terminals. The certificates in the list
        have been uploaded to Adyen and can be installed or uninstalled on Android terminals through `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read
        * Management API—Android files read and write
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            certificate_name: The name of the certificate.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/androidCertificates"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("certificateName", certificate_name),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AndroidCertificatesResponse],
            error_mapper=get_companies_company_id_android_certificates_error_mapper,
            request_options=request_options,
        )

    async def patch_companies_company_id_android_apps_id(
        self, company_id: str, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReprocessAndroidAppResponse, PatchCompaniesCompanyIdAndroidAppsIdErrorBody]:
        """Reuploads the Android app identified in the path. To make this request, your API credential must have this
        `role <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            id: The unique identifier of the app.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/androidApps/{id}"),
            path_params=[param[str]("companyId", company_id), param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ReprocessAndroidAppResponse],
            error_mapper=patch_companies_company_id_android_apps_id_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_android_apps(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAndroidAppResponse, PostCompaniesCompanyIdAndroidAppsErrorBody]:
        """Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API
        credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Android files read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.
        >By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept
        full responsibility and liability for any consequences of uploading, installing, or running any such
        applications.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/androidApps"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UploadAndroidAppResponse],
            error_mapper=post_companies_company_id_android_apps_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_android_certificates(
        self, company_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UploadAndroidCertificateResponse, PostCompaniesCompanyIdAndroidCertificatesErrorBody]:
        """Uploads an Android Certificate file to Adyen.

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/androidCertificates"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UploadAndroidCertificateResponse],
            error_mapper=post_companies_company_id_android_certificates_error_mapper,
            request_options=request_options,
        )
