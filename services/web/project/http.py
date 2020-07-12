import time
import logging
import asyncio

logging.getLogger().setLevel(logging.INFO)


async def send(request):
    try:
        response = await request()
    except asyncio.TimeoutError:
        logging.warning("Timeout")
    except Exception as e:
        logging.warning(e)
    else:
        return response
    return


async def send_async(loop, batch):
    tasks = []
    for request in batch:
        task = asyncio.ensure_future(send(request))
        tasks.append(task)
        # await response outside the for loop
    responses = await asyncio.gather(*tasks)
    return responses


def process_batch(batch):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(send_async(loop, batch))
    loop.run_until_complete(future)
    responses = future.result()
    logging.info(
        "Sending %s requests takes %s seconds",
        str(len(batch), time.time() - start_time),
    )
    logging.info("{} requests were sent successfully".format(len(responses)))
