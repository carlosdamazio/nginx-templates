import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Nginx *.conf templates"
    )
    parser.add_argument('-t', dest='type',
        help='Type of Nginx configuration'
    )
    parser.add_argument('-p', dest='path', default='./')
    parser.add_argument('--server-name', dest='server',
        default='default-server'
    )
    parser.add_argument('--nodes', dest='nodes', nargs='+')

    args = parser.parse_args()

    return check_args(args)

def check_args(args):
    return args
