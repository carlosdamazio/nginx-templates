import os

from nginx_generator.parser import parser
from nginx_generator.system.commander import Commander

DIR_TEMPLATE = '/templates/'
PATH_TEMPLATES = os.path.dirname(os.path.abspath(__file__)) + DIR_TEMPLATE


def run():
    args = parser.parse_args()

    if not args:
        return None

    print(PATH_TEMPLATES)
    print(Commander)
