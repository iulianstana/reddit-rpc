import raven

public_key = 'd58941b8cd7946a2a33e71ecae59a961'
secret_key = '2c887461271d462c8c51242bcd2b58d8'
account_phrase = '%s:%s' % (public_key, secret_key)


client = raven.Client(
    dsn='https://%s@sentry.io/149447' % account_phrase,

    # inform the client which parts of code are yours
    # include_paths=['my.app']
    include_paths=[__name__.split('.', 1)[0],
                   'mongo_wrapper',
                   'datacluster_server',
                   ],
)
