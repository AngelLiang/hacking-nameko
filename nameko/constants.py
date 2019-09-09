AMQP_URI_CONFIG_KEY = 'AMQP_URI'
WEB_SERVER_CONFIG_KEY = 'WEB_SERVER_ADDRESS'
RPC_EXCHANGE_CONFIG_KEY = 'rpc_exchange'
SERIALIZER_CONFIG_KEY = 'serializer'
SERIALIZERS_CONFIG_KEY = 'SERIALIZERS'
ACCEPT_CONFIG_KEY = 'ACCEPT'
HEARTBEAT_CONFIG_KEY = 'HEARTBEAT'
AMQP_SSL_CONFIG_KEY = 'AMQP_SSL'
TRANSPORT_OPTIONS_CONFIG_KEY = 'TRANSPORT_OPTIONS'

MAX_WORKERS_CONFIG_KEY = 'max_workers'
PREFETCH_COUNT_CONFIG_KEY = 'PREFETCH_COUNT'
PARENT_CALLS_CONFIG_KEY = 'parent_calls_tracked'

# 默认最大woker数量
DEFAULT_MAX_WORKERS = 10
# 默认预获取数量
DEFAULT_PREFETCH_COUNT = 10
DEFAULT_PARENT_CALLS_TRACKED = 10
# 默认序列化格式
DEFAULT_SERIALIZER = 'json'
DEFAULT_RETRY_POLICY = {'max_retries': 3}
# 默认心跳
DEFAULT_HEARTBEAT = 60
# 默认通信选项
DEFAULT_TRANSPORT_OPTIONS = {
    'max_retries': 3,
    'interval_start': 2,
    'interval_step': 1,
    'interval_max': 5
}
# 默认AMQP URI
DEFAULT_AMQP_URI = 'pyamqp://guest:guest@localhost'

CALL_ID_STACK_CONTEXT_KEY = 'call_id_stack'
AUTH_TOKEN_CONTEXT_KEY = 'auth_token'
LANGUAGE_CONTEXT_KEY = 'language'
USER_ID_CONTEXT_KEY = 'user_id'
USER_AGENT_CONTEXT_KEY = 'user_agent'

# delivery_mode
HEADER_PREFIX = "nameko"
NON_PERSISTENT = 1
PERSISTENT = 2
