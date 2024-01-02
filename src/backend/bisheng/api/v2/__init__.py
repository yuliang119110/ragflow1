from bisheng.api.v2.chat import router as chat_router_rpc
from bisheng.api.v2.filelib import router as knowledge_router_rpc
from bisheng.api.v2.rpc import router as rpc_router_rpc

__all__ = ['knowledge_router_rpc', 'chat_router_rpc', 'rpc_router_rpc']
