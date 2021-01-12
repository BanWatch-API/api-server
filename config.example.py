from requests import get
# Basic Bot config
TG_BOT_TOKEN = "123456:someRandomTextGoesHere"
LOG_CHAT = 777000

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