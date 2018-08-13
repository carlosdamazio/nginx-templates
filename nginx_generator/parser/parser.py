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
    parser.add_argument('--sslcert', dest='sslcert')
    parser.add_argument('--sslkey', dest='sslkey')
    parser.add_argument('--root', dest='root')

    args = parser.parse_args()
    args.root = args.root.replace("/", "\\/")
    args.sslcert = args.sslcert.replace("/", "\\/") if args.sslcert else None
    args.sslkey = args.sslkey.replace("/", "\\/") if args.sslkey else None
    return args
