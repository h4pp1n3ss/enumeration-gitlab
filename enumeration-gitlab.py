#!/usr/bin/env python
import argparse

from enumeration_gitlab.main import gitlab_enumeration


def main():
    parser = argparse.ArgumentParser(description='Enumerate IAM permissions')

    parser.add_argument('--token', help='PERSONAL_ACCESS_TOKEN', required=True)

    args = parser.parse_args()

    gitlab_enumeration(args.token)

if __name__ == '__main__':
    main()
    