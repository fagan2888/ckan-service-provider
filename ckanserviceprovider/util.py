# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging


class JobError(Exception):
    '''Error to be raised by jobs so that message is returned'''
    pass


class QueuingHandler(logging.Handler):
    '''A handler that enqueues logging messages so that they
    can be sent to another process.'''
    def __init__(self, queue, task_id):
        logging.Handler.__init__(self)
        self.task_id = task_id
        self.queue = queue

    def emit(self, record):
        self.queue.put((self.task_id, record))
