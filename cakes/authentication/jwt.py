from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from .models import Profile


class ProfileJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token[self.user_id_claim]
        except KeyError as exc:
            raise AuthenticationFailed(
                'Token contained no recognizable user identification',
                code='token_not_valid',
            ) from exc

        try:
            user = Profile.objects.get(**{self.user_id_field: user_id})
        except Profile.DoesNotExist as exc:
            raise AuthenticationFailed(
                'User not found',
                code='user_not_found',
            ) from exc

        if not user.is_active:
            raise AuthenticationFailed(
                'User is inactive',
                code='user_inactive',
            )

        return user
