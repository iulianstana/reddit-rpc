import datetime
import json
import time

import grpc

from config import SERVER_HOST, SERVER_PORT, WAIT_TIME, JSON_PATH
from protos.python import datacluster_pb2
from protos.python import datacluster_pb2_grpc
from raven_config import client
from reddit_wrapper import RedditWrapper


def read_json_file(path):
    """Read json file from a specific path and return the subreddits. """
    subreddits = []
    try:
        with open(path) as json_file:
            subreddits = json.load(json_file)['subreddits']
    except IOError as exp:
        print exp
    return subreddits


def run_reader(stub, subreddits):
    """Start fetching data and send it to the server. """
    if subreddits:
        while True:
            # times are restarted, start with a wait
            time.sleep(WAIT_TIME)

            for subreddit in subreddits:
                time_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                print "[%s] Start fetching ... '%s'" % (time_now, subreddit)
                reddit_obj = subreddits[subreddit]
                reddit_obj.restart_fetch_time()

                for message in reddit_obj.fetch_submissions():
                    client_message(stub, message)
                for message in reddit_obj.fetch_comments():
                    client_message(stub, message)
    else:
        print "no reddits to fetch"


def client_message(stub, message):
    """Send message to the server using the stub. """
    response_status = False
    while not response_status:
        response = stub.AddRedditMessage(datacluster_pb2.RedditMessage(**message))
        response_status = response.ack
        if not response_status:
            print "Resend the current message"


def main():
    subreddits = read_json_file(JSON_PATH)
    subreddit_objs = {}

    channel = grpc.insecure_channel('%s:%s' % (SERVER_HOST, SERVER_PORT))
    stub = datacluster_pb2_grpc.DataClusterStub(channel)

    for subreddit in subreddits:
        subreddit_objs[subreddit] = RedditWrapper(subreddit, start_ts=time.time())

    run_reader(stub, subreddit_objs)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
