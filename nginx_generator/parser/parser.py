import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Nginx *.conf templates"
    )
    parser.add_argument('-t', dest='type',
        help='Type of Nginx configuration. LB=Load Balancer, SRVNOSSL=Simple\
    server without SSL, SRVSSL=Simple server with SSL.',
        required=True
    )
    parser.add_argument('--server-name', dest='server',
        default='default-server'
    )
    parser.add_argument('--nodes', dest='nodes', nargs='+')
    parser.add_argument('--sslcert', dest='sslcert_path')
    parser.add_argument('--sslkey', dest='sslkey_path')

    args = parser.parse_args()
    return args
