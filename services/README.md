## Service duty

This service will wait and listen for all new messages. Clients will connect
here and sends their messages that will be saved in a nosql database.

After a message is received ACK is send back IOT to communicate client that his
message arrived.

Other clients can also connect and ask different information from server. Time
stamp is required.

## Using tools

    * mongoDB for noSQL database
    * gRPC for server-client communication

