import httpx

from app.crawlers.models import CrawledJob


class MicrosoftApiProvider:

    BASE_URL = "https://apply.careers.microsoft.com/api/pcsx/search"

    async def search(self, query: str):

        params = {
            "domain": "microsoft.com",
            "query": query,
            "location": "",
            "start": 0,
        }

        headers = {
            "Accept": "application/json",
            "User-Agent": "CareerCopilot/1.0",
        }

        async with httpx.AsyncClient() as client:

            response = await client.get(
                self.BASE_URL,
                params=params,
                headers=headers,
                timeout=30,
            )

            print(response.status_code)
            print(response.text[:500])
            response_json = response.json()

            jobs = []

            for position in response_json["data"]["positions"]:

                job = CrawledJob(
                    title=position["name"],
                    company="Microsoft",
                    location=", ".join(position.get("locations", [])),
                    department=position.get("department"),
                    job_id=str(position["displayJobId"]),
                    url=f"https://jobs.careers.microsoft.com/global/en/job/{position['displayJobId']}"
                )

                jobs.append(job)

            return jobs

    async def get_job_details(
        self,
        position_id: str
    ):
        params = {
            "position_id": position_id,
            "domain": "microsoft.com",
            "hl": "en",
        }

        async with httpx.AsyncClient() as client:

            response = await client.get(
                "https://apply.careers.microsoft.com/api/pcsx/position_details",
                params=params,
                headers={
                    "Accept": "application/json"
                }
            )

            response.raise_for_status()

            return response.json()