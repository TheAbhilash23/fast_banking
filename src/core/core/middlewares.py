from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class RestAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Code that runs before the request
        print(f"Incoming request: {request.method} {request.url}")

        # Call the next middleware or the actual request handler
        response = await call_next(request)

        # Code that runs after the request
        print(f"Response status: {response.status_code}")

        return response