from playwright.async_api import async_playwright

from app.job_discovery.providers.base import BaseProvider


class MicrosoftProvider(BaseProvider):

    async def search(
        self,
        query: str
    ):

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()
# curl 'https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=AI&location=&start=0&' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: en-US,en;q=0.9,te;q=0.8' \
#   -b 'MC1=GUID=24339053cd82403a8f526fefcd447272&HASH=2433&LV=202601&V=4&LU=1768656473478; MUID=3B9EA1F28E2A65A73552B7358F5564CF; kndctr_EA76ADE95776D2EC7F000101_AdobeOrg_identity=CiYzNTk5NTI2MTQxMTc0MTcyMzg2MjE5ODA4Nzk3NTQ1NjkyMzM5NVISCLydtKe_MxABGAEqA09SMjAA8AG8nbSnvzM=; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=MCMID|35995261411741723862198087975456923395; mbox=PC#a48a566b443a43d5bcdc20b3811be716.35_0#1803722448|session#e0017a3b64634cc4ade7e4ea2d2343cc#1769544308; _clck=16zvkof%5E2%5Eg61%5E1%5E2216; _vs=615891226112917525:1782637567.190734:1628119052929501429; _vscid=2; MicrosoftApplicationsTelemetryDeviceId=aad17b8c-8145-485d-88f6-5a9ed5bcdadd; MS0=212d7cb549e84c77bca66f318127bf26; MSFPC=GUID=24339053cd82403a8f526fefcd447272&HASH=2433&LV=202601&V=4&LU=1768656473478; MSCC=NR; handleWcpConsentGCSVNext={%22Required%22:true%2C%22Analytics%22:true%2C%22SocialMedia%22:true%2C%22Advertising%22:true}; ai_user=n9cuV|2026-06-28T09:06:13.095Z; ai_session=6eyXRSeyTLu/dKUtU0Rcx1|1782637568021|1782637585805.2' \
#   -H 'dnt: 1' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://apply.careers.microsoft.com/careers?start=0&pid=1970393556915381&sort_by=timestamp' \
#   -H 'request-id: |c7808c07c1584f7390bcd6bef33ce3bf.b237b6c3020a4dab' \
#   -H 'sec-ch-ua: "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36' \
#   -H 'x-browser-request-time: 1782637596.808' \
#   -H 'x-csrf-token: IjFiNWRmYzVlMmZkNDZhYThkNmE5NjIyYmVhMDEwMjIwZGJkY2Q1ODMi.HSJ1mw.M9FU6fyqMjOZHHXeuK_pDgDA21o'
            await page.goto(
                "https://jobs.careers.microsoft.com/global/en/search"
            )

            await page.wait_for_load_state(
                "networkidle"
            )

            print(await page.title())

            await browser.close()

        return []