import subprocess

from nginx_generator.decorator.permission import permission


class Commander(object):

    def __init__(self, path, **kwargs):
        self.args = kwargs
        self.path = path

    @permission
    def prepare_execution(self):
        pass
