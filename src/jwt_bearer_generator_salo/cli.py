import argparse
import sys

from jwt_bearer_generator_salo.generate_bearer import generate_bearer_token


def main():
    """Generate JWT bearer token with configurable parameters"""
    parser = argparse.ArgumentParser(description="Generate JWT bearer token.")
    parser.add_argument("jwt_secret", type=str, help="JWT secret key")
    parser.add_argument(
        "--username", type=str, default="Morgan", help="Username (default: Morgan)"
    )
    parser.add_argument(
        "--role", type=str, default="Morgan", help="Role (default: Morgan)"
    )
    parser.add_argument(
        "--expire-days",
        type=int,
        default=365 * 10,
        help="Expiration days (default: 3650)",
    )

    args = parser.parse_args()

    token = generate_bearer_token(
        jwt_secret=args.jwt_secret,
        username=args.username,
        role=args.role,
        expire_days=args.expire_days,
    )

    print(token)


if __name__ == "__main__":
    sys.exit(main())
