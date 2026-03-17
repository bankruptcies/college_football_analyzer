import os
from dotenv import load_dotenv
import cfbd

# Load environment variables
load_dotenv()

api_key = os.getenv("CFBD_API_KEY")

if not api_key:
    raise ValueError("CFBD_API_KEY not found in .env file")

# Create configuration
configuration = cfbd.Configuration()

# Manually set Authorization header
configuration.access_token = api_key

# Create API client
api_client = cfbd.ApiClient(configuration)