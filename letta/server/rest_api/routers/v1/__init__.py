from letta.server.rest_api.routers.v1.agents import router as agents_router
from letta.server.rest_api.routers.v1.blocks import router as blocks_router
from letta.server.rest_api.routers.v1.embeddings import router as embeddings_router
from letta.server.rest_api.routers.v1.folders import router as folders_router
from letta.server.rest_api.routers.v1.groups import router as groups_router
from letta.server.rest_api.routers.v1.health import router as health_router
from letta.server.rest_api.routers.v1.identities import router as identities_router
from letta.server.rest_api.routers.v1.jobs import router as jobs_router
from letta.server.rest_api.routers.v1.llms import router as llm_router
from letta.server.rest_api.routers.v1.messages import router as messages_router
from letta.server.rest_api.routers.v1.providers import router as providers_router
from letta.server.rest_api.routers.v1.runs import router as runs_router
from letta.server.rest_api.routers.v1.sandbox_configs import router as sandbox_configs_router
from letta.server.rest_api.routers.v1.sources import router as sources_router
from letta.server.rest_api.routers.v1.steps import router as steps_router
from letta.server.rest_api.routers.v1.tags import router as tags_router
from letta.server.rest_api.routers.v1.telemetry import router as telemetry_router
from letta.server.rest_api.routers.v1.tools import router as tools_router
from letta.server.rest_api.routers.v1.voice import router as voice_router

ROUTERS = [
    tools_router,
    sources_router,
    folders_router,
    agents_router,
    groups_router,
    identities_router,
    llm_router,
    blocks_router,
    jobs_router,
    health_router,
    sandbox_configs_router,
    providers_router,
    runs_router,
    steps_router,
    tags_router,
    telemetry_router,
    messages_router,
    voice_router,
    embeddings_router,
]
