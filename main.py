#!/usr/bin/env python
"""
AWS Extend Switch Roles Config Creator.

Output config generated from AWS Organizations with nice coloring.
"""

import boto3
import random

role_name = "OrganizationAccountAccessRole"


def get_account_list():
    """
    Get list of accounts.

    return: List of account Ids, Name and Email.
    """
    name_list = []
    account_list = []
    client = boto3.client('organizations')
    response = client.list_accounts(MaxResults=10)

    while 'NextToken' in response:
        for account in response['Accounts']:
            account_list.append(account['Id'])
            name_list.append(account['Name'])
        response = client.list_accounts(NextToken=response['NextToken'])
    return account_list, name_list


def main():
    """
    Create config.

    Get all AWS accounts and generate config.
    """
    all_accounts, all_name = get_account_list()

    for account in all_accounts:
        account_name = all_name[all_accounts.index(account)]

        try:
            color = '{:06x}'.format(random.randint(0, 256**3))
            out = "[{0}]\naws_account_id = {1}\nrole_name = {2}\ncolor = {3}\n".format(account_name, account, role_name, color)
            print(out)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
