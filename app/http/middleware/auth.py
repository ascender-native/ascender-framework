from fastapi import Request
from fastapi.security import HTTPBasicCredentials, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware

# TODO: Переделать. Этот вариант не подходит
class Authenticated(HTTPAuthorizationCredentials):
    pass
