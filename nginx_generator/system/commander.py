import os
import subprocess, shlex

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
        elif self.args.type == 'SRVSSL' and self.args.sslcert \
        and self.args.sslkey and self.args.server:
            return self.execute_srvssl()

        return None, ""

    @permission
    def execute_lb(self):
        target = self.template_path + 'load_balancer_https/' + self.FILE
        nodes = '\\n    '.join(self.args.nodes)

        subprocess.run(['cp', target, self.cpdest])

        for key in self.args.__dict__.keys():
            if key == 'nodes':
                subprocess.run(['sed', '-i', 's/"{}"/{}/g'.format(
                    key, nodes
                ), self.cpdest +'/'+self.FILE])
            else:
                subprocess.run(['sed', '-i', 's/"{}"/{}/g'.format(
                    key, self.args.__dict__[key]
                ), self.cpdest +'/'+self.FILE])

        return True, self.cpdest+'/'+self.FILE

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
        target = self.template_path + 'simple_server_ssl/' + self.FILE
        subprocess.run(['cp', target, self.cpdest])

        for key in self.args.__dict__.keys():
            subprocess.run(['sed', '-i', 's/"{}"/{}/g'.format(
                key, self.args.__dict__[key]
            ), self.cpdest +'/'+self.FILE])

        return True, self.cpdest+'/'+self.FILE

