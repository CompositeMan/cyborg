import argparse
import settings 
# from settings import VERSION

parser = argparse.ArgumentParser(description='VAG Tester script', prog='Cyborg') # allow_abbrev=False
parser.add_argument('--config', 
                     #aliases=['co'],
                     action='store_true', 
                     help='configuration of the %(prog)s settings',
                     #required=False
                     )
parser.add_argument('--version', action='version', version='%(prog)s'+settings.VERSION) #version
parser.add_argument('--driver', 
                    choices=['Chrome', 'Firefox'], 
                    default='Chrome',
                    help='driver to run on, default to Chrome',
                    )
args = parser.parse_args()

set = 'settings.json'


if args.config:
        print(f'Configurations from {set}')
        # print(args.version)
        from sys import path
        for p in path:
                print(p)

print(args)
settings.DRIVER = args.driver
