import argparse
import requests
'''
In Terminal python ProblemSolveURL.py --url (url)
'''
parser = argparse.ArgumentParser(
    description='Check a URL'
)

parser.add_argument('--url', required=True)

args = parser.parse_args()

response = requests.get(args.url)

print(response)

if response.ok:
    print('success')
else:
    print('failed', response.status_code)