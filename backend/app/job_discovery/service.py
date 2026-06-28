from app.job_discovery.providers.microsoft_api import MicrosoftApiProvider


class JobDiscoveryService:

    def __init__(self):

        self.providers = {

            "microsoft": MicrosoftApiProvider()

        }

    async def search(
        self,
        company: str,
        query: str
    ):

        provider = self.providers[company]

        return await provider.search(query)