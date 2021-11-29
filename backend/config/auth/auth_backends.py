from fastapi_users.authentication import JWTAuthentication
# from httpx_oauth.clients.google import GoogleOAuth2
from ..config import get_settings

settings = get_settings()
SECRET = settings.SECRET

# google_oauth_client = GoogleOAuth2("CLIENT_ID", "CLIENT_SECRET")
jwt_authentication = JWTAuthentication(secret=SECRET, 
                                       lifetime_seconds=3600, 
                                       tokenUrl="/auth/jwt/login")
auth_backends = []
auth_backends.append(jwt_authentication)
