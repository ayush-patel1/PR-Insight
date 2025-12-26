from fastapi import APIRouter, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

router = APIRouter()


@router.post("/webhook/github")
async def github_webhook(
    request: Request,
    x_github_event: Optional[str] = Header(None)
):
    payload = await request.json()
     #if it is not a pull request then ignore and give response
    if x_github_event != "pull_request":
        return JSONResponse(
            status_code=200,
            content={"message": "event ignored , it's not a pull request"}
        )

    action = payload.get("action")

    if action == "opened":
        pull_request = payload.get("pull_request")

        if not pull_request:
            raise HTTPException(status_code=400, detail="Invalid PR payload")

        pr_number = pull_request
        pr_title = pull_request.get("title")

        print("New PR Opened")
        print("PR Number:", pr_number)
        print("PR Title:", pr_title)

    return JSONResponse(
        status_code=200,
        content={"status": "webhook processed"}
    )
