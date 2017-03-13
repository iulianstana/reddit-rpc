import os


def get_environment_var(env_name, default_value):
    """ Map the os.environment to return actual value or a default one. """
    if env_name in os.environ:
        return os.environ[env_name]
    else:
        return default_value


# mongo configuration
MONGO_SERVER = get_environment_var('MONGO_SERVER', "0.0.0.0")
MONGO_PORT = int(get_environment_var('MONGO_PORT', 27017))

DATABASE_NAME = get_environment_var('DATABASE_NAME', "reddit_messages")
