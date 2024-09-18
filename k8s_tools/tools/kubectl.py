from kubiya_sdk.tools import Arg
from .base import KubernetesTool
from kubiya_sdk.tools.registry import tool_registry

SCRIPT_KUBECTL_COMMAND="""
kubectl {{ .command}}
"""

kubectl_tool = KubernetesTool(
    name="kubectl",
    description="Executes kubectl commands",
    content=SCRIPT_KUBECTL_COMMAND,
    args=[
        Arg(name="command", type="str", description="The kubectl command to execute. Do not use `kubectl`, only enter its command.", required=True),
    ],
)

tool_registry.register("kubernetes", kubectl_tool)
