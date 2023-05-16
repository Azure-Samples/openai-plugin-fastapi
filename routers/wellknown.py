import yaml
import json
from string import Template
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, Response

wellknown = APIRouter(prefix="/.well-known", tags=["well-known"])

@wellknown.get("/openapi.yaml", include_in_schema=False)
async def openapi_yaml(request: Request):
    openapi = request.app.openapi()
    # Add public server URL
    host_header = request.headers.get("X-Forwarded-Host") or request.headers.get("Host")
    protocol = request.headers.get("X-Forwarded-Proto") or request.url.scheme
    openapi["servers"] = [{"url": f"{protocol}://{host_header}"}]
    # Use title and description from ai-plugin spec
    with open(".well-known/ai-plugin.json", encoding="utf-8") as file:
        ai_plugin = json.loads(file.read())
        openapi["info"]["title"] = ai_plugin["name_for_human"]
        openapi["info"]["description"] = ai_plugin["description_for_human"]
        return Response(
            content=yaml.dump(openapi),
            media_type="text/vnd.yaml",
        )

@wellknown.get("/logo.png", include_in_schema=False)
async def logo():
    return FileResponse(".well-known/logo.png", media_type="image/png")


@wellknown.get("/ai-plugin.json", include_in_schema=False)
async def manifest(request: Request):
    host_header = request.headers.get("X-Forwarded-Host") or request.headers.get("Host")
    protocol = request.headers.get("X-Forwarded-Proto") or request.url.scheme

    with open(".well-known/ai-plugin.json", encoding="utf-8") as file:
        return Response(
            content=Template(file.read()).substitute(
                host=f"{protocol}://{host_header}"
            ),
            media_type="application/json",
        )
