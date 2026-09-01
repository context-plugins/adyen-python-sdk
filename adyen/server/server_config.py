from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate


class DefaultConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://checkout-test.adyen.com/v72"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class DefaultConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default1Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/servlet/Payment/v68"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default1ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/servlet/Recurring/v68"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default2ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default3Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/servlet/Payout/v68"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default3ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default4Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/servlet/BinLookup/v54"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default4ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default5Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/servlet/StoredValue/v46"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default5ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default6Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://ca-test.adyen.com/ca/services/DataProtectionService/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default6ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default7Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/fx/api/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default7ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default8Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://pal-test.adyen.com/pal/services/TestCard/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default8ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default9Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://management-test.adyen.com/v3"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default9ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default10Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://cal-test.adyen.com/cal/services/Account/v6"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default10ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default11Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balance-control-test.adyen.com/balance-control/api/v2"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default11ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default12Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://cal-test.adyen.com/cal/services/Notification/v6"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default12ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default13Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default13ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default14Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/btl/v4"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default14ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default15Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/capital/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default15ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default16Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://cal-test.adyen.com/cal/services/Fund/v6"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default16ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default17Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://test.adyen.com/authe/api/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default17ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default18Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://kyc-test.adyen.com/lem/v4"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default18ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default19Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://cal-test.adyen.com/cal/services/Hop/v6"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default19ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default20Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/a2aissuer-api/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default20ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default21Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://obgateway-test.adyen.com/obgateway/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default21ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default22Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://ca-test.adyen.com/ca/services/DisputeService/v30"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default22ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default23Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://balanceplatform-api-test.adyen.com/btl/api/v4"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default23ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default24Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-test.adyen.com/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default24ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default25Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://softposconfig-test.adyen.com/softposconfig/v3"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default25ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default26Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://management-test.adyen.com/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default26ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default27Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://checkout-test.adyen.com/checkout/possdk/v68"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default27ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default28Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://postfmapi-test.adyen.com/postfmapi/terminal/v1"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default28ConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    default: DefaultConfig = Field(default_factory=DefaultConfig)
    default1: Default1Config = Field(default_factory=Default1Config)
    default2: Default2Config = Field(default_factory=Default2Config)
    default3: Default3Config = Field(default_factory=Default3Config)
    default4: Default4Config = Field(default_factory=Default4Config)
    default5: Default5Config = Field(default_factory=Default5Config)
    default6: Default6Config = Field(default_factory=Default6Config)
    default7: Default7Config = Field(default_factory=Default7Config)
    default8: Default8Config = Field(default_factory=Default8Config)
    default9: Default9Config = Field(default_factory=Default9Config)
    default10: Default10Config = Field(default_factory=Default10Config)
    default11: Default11Config = Field(default_factory=Default11Config)
    default12: Default12Config = Field(default_factory=Default12Config)
    default13: Default13Config = Field(default_factory=Default13Config)
    default14: Default14Config = Field(default_factory=Default14Config)
    default15: Default15Config = Field(default_factory=Default15Config)
    default16: Default16Config = Field(default_factory=Default16Config)
    default17: Default17Config = Field(default_factory=Default17Config)
    default18: Default18Config = Field(default_factory=Default18Config)
    default19: Default19Config = Field(default_factory=Default19Config)
    default20: Default20Config = Field(default_factory=Default20Config)
    default21: Default21Config = Field(default_factory=Default21Config)
    default22: Default22Config = Field(default_factory=Default22Config)
    default23: Default23Config = Field(default_factory=Default23Config)
    default24: Default24Config = Field(default_factory=Default24Config)
    default25: Default25Config = Field(default_factory=Default25Config)
    default26: Default26Config = Field(default_factory=Default26Config)
    default27: Default27Config = Field(default_factory=Default27Config)
    default28: Default28Config = Field(default_factory=Default28Config)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    default: NotRequired[DefaultConfigDict]
    default1: NotRequired[Default1ConfigDict]
    default2: NotRequired[Default2ConfigDict]
    default3: NotRequired[Default3ConfigDict]
    default4: NotRequired[Default4ConfigDict]
    default5: NotRequired[Default5ConfigDict]
    default6: NotRequired[Default6ConfigDict]
    default7: NotRequired[Default7ConfigDict]
    default8: NotRequired[Default8ConfigDict]
    default9: NotRequired[Default9ConfigDict]
    default10: NotRequired[Default10ConfigDict]
    default11: NotRequired[Default11ConfigDict]
    default12: NotRequired[Default12ConfigDict]
    default13: NotRequired[Default13ConfigDict]
    default14: NotRequired[Default14ConfigDict]
    default15: NotRequired[Default15ConfigDict]
    default16: NotRequired[Default16ConfigDict]
    default17: NotRequired[Default17ConfigDict]
    default18: NotRequired[Default18ConfigDict]
    default19: NotRequired[Default19ConfigDict]
    default20: NotRequired[Default20ConfigDict]
    default21: NotRequired[Default21ConfigDict]
    default22: NotRequired[Default22ConfigDict]
    default23: NotRequired[Default23ConfigDict]
    default24: NotRequired[Default24ConfigDict]
    default25: NotRequired[Default25ConfigDict]
    default26: NotRequired[Default26ConfigDict]
    default27: NotRequired[Default27ConfigDict]
    default28: NotRequired[Default28ConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
