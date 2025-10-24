import jwt
import datetime
import uuid


def generate_bearer_token(
    jwt_secret: str,
    username: str,
    role: str,
    expire_days: int,
) -> str:
    claims = {  # pyright: ignore[reportUnknownVariableType]
        "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name": username,
        "jti": str(uuid.uuid4()),
        "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": role,
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(days=expire_days),
    }

    token = jwt.encode(claims, jwt_secret, algorithm="HS256")  # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
    return token
