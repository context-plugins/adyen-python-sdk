from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..core import UrlTemplate
from .environment import Environment


class ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-test.adyen.com/v1"


class Environment2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-live-au.adyen.com/v1"


class Environment3Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-live-apse.adyen.com/v1"


class Environment4Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-live.adyen.com/v1"


class Environment5Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://device-api-live-us.adyen.com/v1"


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ProductionConfig = Field(default_factory=ProductionConfig)
    environment2: Environment2Config = Field(default_factory=Environment2Config)
    environment3: Environment3Config = Field(default_factory=Environment3Config)
    environment4: Environment4Config = Field(default_factory=Environment4Config)
    environment5: Environment5Config = Field(default_factory=Environment5Config)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "environment2":
            environment2 = self.environment2
            return UrlTemplate(base_url=environment2.base_url, path=path)
        if environment == "environment3":
            environment3 = self.environment3
            return UrlTemplate(base_url=environment3.base_url, path=path)
        if environment == "environment4":
            environment4 = self.environment4
            return UrlTemplate(base_url=environment4.base_url, path=path)
        environment5 = self.environment5
        return UrlTemplate(base_url=environment5.base_url, path=path)
