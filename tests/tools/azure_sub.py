import asyncio
import pytest
import config
from azure.eventhub import EventHubConsumerClient

async def azure_sub():
    connection_str = config.AZURE_CONN_STR
    consumer_group = '$default'

    azure_client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group)

    def on_event(partition_context, event):
        pytest.message = event.body_as_str(encoding='UTF-8')
        partition_context.update_checkpoint(event)
        raise KeyboardInterrupt

    try:
        azure_client.receive(on_event=on_event)
    except KeyboardInterrupt:
        pass

    return