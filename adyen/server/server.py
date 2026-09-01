from __future__ import annotations

from dataclasses import dataclass

from ..core import UrlTemplate
from .server_config import ServerConfig


@dataclass(frozen=True, slots=True)
class Server:
    config: ServerConfig

    def default(self, path: str) -> UrlTemplate:
        return self.config.default.resolve(path)

    def default1(self, path: str) -> UrlTemplate:
        return self.config.default1.resolve(path)

    def default2(self, path: str) -> UrlTemplate:
        return self.config.default2.resolve(path)

    def default3(self, path: str) -> UrlTemplate:
        return self.config.default3.resolve(path)

    def default4(self, path: str) -> UrlTemplate:
        return self.config.default4.resolve(path)

    def default5(self, path: str) -> UrlTemplate:
        return self.config.default5.resolve(path)

    def default6(self, path: str) -> UrlTemplate:
        return self.config.default6.resolve(path)

    def default7(self, path: str) -> UrlTemplate:
        return self.config.default7.resolve(path)

    def default8(self, path: str) -> UrlTemplate:
        return self.config.default8.resolve(path)

    def default9(self, path: str) -> UrlTemplate:
        return self.config.default9.resolve(path)

    def default10(self, path: str) -> UrlTemplate:
        return self.config.default10.resolve(path)

    def default11(self, path: str) -> UrlTemplate:
        return self.config.default11.resolve(path)

    def default12(self, path: str) -> UrlTemplate:
        return self.config.default12.resolve(path)

    def default13(self, path: str) -> UrlTemplate:
        return self.config.default13.resolve(path)

    def default14(self, path: str) -> UrlTemplate:
        return self.config.default14.resolve(path)

    def default15(self, path: str) -> UrlTemplate:
        return self.config.default15.resolve(path)

    def default16(self, path: str) -> UrlTemplate:
        return self.config.default16.resolve(path)

    def default17(self, path: str) -> UrlTemplate:
        return self.config.default17.resolve(path)

    def default18(self, path: str) -> UrlTemplate:
        return self.config.default18.resolve(path)

    def default19(self, path: str) -> UrlTemplate:
        return self.config.default19.resolve(path)

    def default20(self, path: str) -> UrlTemplate:
        return self.config.default20.resolve(path)

    def default21(self, path: str) -> UrlTemplate:
        return self.config.default21.resolve(path)

    def default22(self, path: str) -> UrlTemplate:
        return self.config.default22.resolve(path)

    def default23(self, path: str) -> UrlTemplate:
        return self.config.default23.resolve(path)

    def default24(self, path: str) -> UrlTemplate:
        return self.config.default24.resolve(path)

    def default25(self, path: str) -> UrlTemplate:
        return self.config.default25.resolve(path)

    def default26(self, path: str) -> UrlTemplate:
        return self.config.default26.resolve(path)

    def default27(self, path: str) -> UrlTemplate:
        return self.config.default27.resolve(path)

    def default28(self, path: str) -> UrlTemplate:
        return self.config.default28.resolve(path)
