from fastapi import APIRouter

from app.job_discovery.service import JobDiscoveryService

router = APIRouter(
    prefix="/job-discovery",
    tags=["Job Discovery"]
)

service = JobDiscoveryService()


@router.get("/search")
async def search():

    jobs = await service.search(

        company="microsoft",

        query="AI"

    )

    return jobs