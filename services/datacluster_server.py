import random
import time

from concurrent import futures
import grpc

from config import SERVER_PORT, DAY
from proto import datacluster_pb2
from proto import datacluster_pb2_grpc
from raven_config import client


class ListenerServer(datacluster_pb2_grpc.DataClusterServicer):
    def AddRedditMessage(self, request, context):
        # create a random crush in our system
        if random.randint(1, 100) < 90:
            print "(%s) [%s]: %s" % (request.timestamp, request.type, request.message)
            return datacluster_pb2.Reply(ack=True)
        else:
            # we lost data, log and send False ack
            client.captureMessage('Received message was not process.')
            return datacluster_pb2.Reply(ack=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datacluster_pb2_grpc.add_DataClusterServicer_to_server(ListenerServer(), server)
    server.add_insecure_port('[::]:%s' % SERVER_PORT)
    server.start()
    try:
        while True:
            time.sleep(DAY)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
