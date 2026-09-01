from __future__ import annotations

from dataclasses import dataclass

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    api_key_auth: AuthScheme
    basic_auth: AuthScheme
    client_key: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    api_key_auth: AsyncAuthScheme
    basic_auth: AsyncAuthScheme
    client_key: AsyncAuthScheme
