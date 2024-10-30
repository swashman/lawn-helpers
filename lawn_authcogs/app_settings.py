# Django
from django.conf import settings

# put your app settings here
LAWN_HELPERS_COGS = getattr(
    settings,
    "LAWN_HELPERS_COGS",
    [
        "asmek_authcogs.cogs.about",  # make sure to remove the about cog from aadiscordbot if using this
    ],
)
