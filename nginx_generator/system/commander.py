import subprocess

from nginx_generator.decorator.permission import permission


class Commander(object):

    def __init__(self, args, cpdest, template_path):
        self.args = args
        self.cpdest = cpdest
        self.template_path = template_path

    def prepare_execution(self):
        if self.args.type == 'LB' and self.args.nodes:
            return self.execute_lb()
        elif self.args.type == 'SRVNOSSL' and self.args.server:
            return self.execute_srvnossl()
        elif self.args.type == 'SRVSSL' and self.args.sslcert_path \
        and self.args.sslkey_path and self.args.server:
            return self.execute_srvssl()

        return None

    @permission
    def execute_lb(self):
        pass

    @permission
    def execute_srvnossl(self):
        pass

    @permission
    def execute_srvssl(self):
        pass
