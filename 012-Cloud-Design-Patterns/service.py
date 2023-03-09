# pip install azure-servicebus

import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
NAMESPACE_CONNECTION_STR = "Endpoint=sb://clouddesignpatterns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=urAh3/d3j/vN6ts/iCV3ZGU13tuVXOP4t+ASbPbo8tg="
QUEUE_NAME = "clouddesignpatterns"

async def send_single_message(sender):
    # Create a Service Bus message and send it to the queue
    message = ServiceBusMessage("Sample message to be processed")
    await sender.send_messages(message)
    print("Sending message.")

async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        # Get a Queue Sender object to send messages to the queue
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            # Send one message
            await send_single_message(sender)

asyncio.run(run())
print("Message sent.")