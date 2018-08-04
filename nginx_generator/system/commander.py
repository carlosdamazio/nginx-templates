import subprocess

from nginx_generator.decorator.permission import permission


class Commander(object):

    def __init__(self, args, cpdest, template_path):
        self.args = args
        self.cpdest = cpdest
        self.template_path = template_path
        self.FILE = 'default.conf'

    def execute(self):
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
        target = self.template_path + 'simple_server_nonssl/' + self.FILE
        subprocess.run(['cp', target, self.cpdest])

        for key in self.args.__dict__.keys():
            subprocess.run(['sed', '-i', 's/"{}"/{}/g'.format(
                key, self.args.__dict__[key]
            ), self.cpdest +'/'+self.FILE])

        return True, self.cpdest+'/'+self.FILE

    @permission
    def execute_srvssl(self):
        pass
