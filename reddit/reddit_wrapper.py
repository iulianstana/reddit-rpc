import json
import time

import praw

import datacluster_pb2


class RedditWrapper:

    def __init__(self, subreddit, start_ts=None):
        """Initialize a new object that will manage subreddit submissions
        and comments. Fetch them from reddit. """
        self.reddit_obj = praw.Reddit(user_agent="RedditParser")

        self.end_time = time.time()
        self.start_time = start_ts
        self.subreddit = subreddit

    def fetch_submissions(self):
        """Fetch all submissions in the last self.time_period window.

        :return a list of all new submissions
        """
        new_submissions = []
        try:
            submission_gen = self.reddit_obj.get_subreddit(self.subreddit)\
                                            .get_new(limit=None)

            for submission in submission_gen:
                if submission.created_utc > self.end_time:
                    continue
                if submission.created_utc < self.start_time:
                    break
                new_submissions.append({
                    'timestamp': int(submission.created_utc),
                    'message': submission.title,
                    'type': datacluster_pb2.RedditMessage.submission,
                    'subreddit': self.subreddit
                })
        except praw.errors.InvalidSubreddit:
            print "Invalid Subreddit: no results"
        return new_submissions

    def fetch_comments(self):
        """Fetch all comments in the last self.time_period window.

        :return a list of all new comments
        """
        new_comments = []
        try:
            comments_gen = self.reddit_obj.get_comments(self.subreddit)

            for comment in comments_gen:
                if comment.created_utc > self.end_time:
                    continue
                if comment.created_utc < self.start_time:
                    break
                new_comments.append({
                    'timestamp': int(comment.created_utc),
                    'message': comment.body,
                    'type': datacluster_pb2.RedditMessage.comment,
                    'subreddit': self.subreddit
                })
        except praw.errors.InvalidSubreddit:
            print "Invalid Subreddit: no results"
        return new_comments

    def print_subreddit_data(self):
        """Get data for this subreddit. And print it to stdout. """
        print self.fetch_submissions()
        print self.fetch_comments()

    def restart_fetch_time(self):
        """Restart fetching times. """
        self.start_time = self.end_time
        self.end_time = time.time()


if __name__ == "__main__":
    with open('subreddits.json') as json_file:
        subreddits = json.load(json_file)
        for subreddit in subreddits['subreddits']:
            print "Start fetching '%s' subreddit." % subreddit
            reddit = RedditWrapper(subreddit, time.time() - 900)
            reddit.print_subreddit_data()
