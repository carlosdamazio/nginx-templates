import os

from nginx_generator.parser import parser
from nginx_generator.system.commander import Commander


DIR_TEMPLATE = '/templates/'
PATH_EXECUTION = os.getcwd()
PATH_TEMPLATES = os.path.dirname(os.path.abspath(__file__)) + DIR_TEMPLATE


def run():
    args = parser.parse_args()
    desired_path = input("Do you want to copy the template to another directory? (Default is ./) ")

    if not desired_path:
        c = Commander(args, PATH_EXECUTION, PATH_TEMPLATES)
    else:
        c = Commander(args, desired_path, PATH_TEMPLATES)

    result_value, result_dest_file = c.execute()
    print("Template generated at: {}".format(result_dest_file))
