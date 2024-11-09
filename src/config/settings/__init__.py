from config.env import DjangoEnvironment, env, env_to_enum

DJANGO_ENV = env_to_enum(
    enum_cls=DjangoEnvironment, value=env.str(var="DJANGO_ENV", default=DjangoEnvironment.LOCAL)
)


if DJANGO_ENV == DjangoEnvironment.PRODUCTION:
    from config.settings.production import *  # noqa: F403
elif DJANGO_ENV == DjangoEnvironment.TESTING:
    from config.settings.testing import *  # noqa: F403
else:
    from config.settings.local import *  # noqa: F403
