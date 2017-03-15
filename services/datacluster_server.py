import time

from concurrent import futures
import grpc

from config import SERVER_PORT, DAY
from proto import datacluster_pb2
from proto import datacluster_pb2_grpc


class ListenerServer(datacluster_pb2_grpc.DataClusterServicer):
    def AddRedditMessage(self, request, context):
        print request.timestamp
        print request.message
        print request.type
        return datacluster_pb2.Reply(ack=True)


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
