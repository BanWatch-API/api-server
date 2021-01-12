# Comment out line 2 if you don't use your
# public IP address as your API host.
from requests import get

# Basic Bot config
TG_BOT_TOKEN = "123456:someRandomTextGoesHere"
LOG_CHAT = 777000

# Root API key is same as an Sudo API key
# But this will not stored on your database for security reasons.
# See the README regarding editing this variable
EMERGENCY_API_KEY = "replaceMeWithGeneratedText"
# Only disable root user if you have the admin key generated through API.
# You don't need root if your elevated_users.json is there.
DISABLE_ROOT_USER = False

# Database URL required for storing API keys and permissions.
MONGO_DB_HOST = "insertDbUrl"

# if you don't want to use your public IP adress as the API host,
# remove the get code and use place your domain as string.
API_HOST = get('https://api.ipify.org').text

# API Keys for some antispam systems
# See README and BanWatch API Server Self-hosting Handbook in 
# documentation site for detials on how to obtain these.
SPAMWATCH_API_KEY = "replaceMeWithYourAPIKeyHere"
SPAMBLOCKERS_API_KEY = "replaceMeWithYourAPIKeyHere"

# Finally, set this variable to "NOT ANYMORE"
# so the bot + server will run.
__IS_THIS_STILL_AN_EXAMPLE_CONFIG = "PLZ CHANGE THIS STRING OR NO U"