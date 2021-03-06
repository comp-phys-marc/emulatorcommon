from celery import Celery


class MessageBus:

    def __init__(self, settings):
        self._connection = None
        self.connection = settings

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, settings):
        rb_host = settings.rabbit_host
        rb_port = settings.rabbit_port
        rb_user = settings.rabbit_user
        rb_password = settings.rabbit_password
        rb_queue = settings.rabbit_queue

        self._connection = Celery("tasks", backend='rpc://',
                                  broker='amqp://{0}:{1}@{2}:{3}'.format(rb_user, rb_password, rb_host, rb_port), queue=rb_queue)
