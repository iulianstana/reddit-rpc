import time

import grpc

from config import SERVER_HOST, SERVER_PORT
import datacluster_pb2
import datacluster_pb2_grpc


def client_message():
    channel = grpc.insecure_channel('%s:%s' % (SERVER_HOST, SERVER_PORT))
    stub = datacluster_pb2_grpc.DataClusterStub(channel)

    message = {
        'timestamp': int(time.time()),
        'message': 'Nuca doarme... shhhh!!!',
        'type': datacluster_pb2.RedditMessage.submission,

    }

    response = stub.AddRedditMessage(datacluster_pb2.RedditMessage(**message))
    print response.ack


if __name__ == '__main__':
    client_message()
