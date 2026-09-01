from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.ssl_protocol import SslProtocolOrStr
from .notification_event_configuration import NotificationEventConfiguration, NotificationEventConfigurationDict


class NotificationConfigurationDetails2(SdkBaseModel):
    """Details of the notification subscription configuration."""

    active: Optional[bool] = UNSET
    """Indicates whether the notification subscription is active."""

    api_version: Optional[int] = Field(default=UNSET, alias="apiVersion")
    """The version of the notification to which you are subscribing. To make sure that your integration can properly
    process the notification, subscribe to the same version as the API that you're using."""

    description: Optional[str] = UNSET
    """A description of the notification subscription configuration."""

    event_configs: Optional[list[NotificationEventConfiguration]] = Field(default=UNSET, alias="eventConfigs")
    """Contains objects that define event types and their subscription settings."""

    hmac_signature_key: Optional[str] = Field(default=UNSET, alias="hmacSignatureKey")
    """A string with which to salt the notification(s) before hashing. If this field is provided, a hash value will be
    included under the notification header ``HmacSignature`` and the hash protocol will be included under the
    notification header ``Protocol``. A notification body along with its ``hmacSignatureKey`` and ``Protocol`` can be
    used to calculate a hash value; matching this hash value with the ``HmacSignature`` will ensure that the
    notification body has not been tampered with or corrupted.

    >Must be a 32-byte hex-encoded string (i.e. a string containing 64 hexadecimal characters; e.g.
    "b0ea55c2fe60d4d1d605e9c385e0e7f7e6cafbb939ce07010f31a327a0871f27").

    The omission of this field will preclude the provision of the ``HmacSignature`` and ``Protocol`` headers in
    notification(s)."""

    notification_id: Optional[int] = Field(default=UNSET, alias="notificationId")
    """Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required
    when updating an existing configuration using
    https://docs.adyen.com/api-explorer/#/NotificationConfigurationService/latest/post/updateNotificationConfiguration."""

    notify_password: Optional[str] = Field(default=UNSET, alias="notifyPassword")
    """The password to use when accessing the notifyURL with the specified username."""

    notify_url: Optional[str] = Field(default=UNSET, alias="notifyURL")
    """The URL to which the notifications are to be sent."""

    notify_username: Optional[str] = Field(default=UNSET, alias="notifyUsername")
    """The username to use when accessing the notifyURL."""

    ssl_protocol: Optional[SslProtocolOrStr] = Field(default=UNSET, alias="sslProtocol")
    """The SSL protocol employed by the endpoint. >Permitted values: ``TLSv12``, ``TLSv13``."""


class NotificationConfigurationDetails2Dict(TypedDict):
    active: NotRequired[bool]
    api_version: NotRequired[int]
    description: NotRequired[str]
    event_configs: NotRequired[list[NotificationEventConfiguration | NotificationEventConfigurationDict]]
    hmac_signature_key: NotRequired[str]
    notification_id: NotRequired[int]
    notify_password: NotRequired[str]
    notify_url: NotRequired[str]
    notify_username: NotRequired[str]
    ssl_protocol: NotRequired[SslProtocolOrStr]
