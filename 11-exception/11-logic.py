#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import json

def logic_control(list_content):

    f = open(list_content,'r')
    list_content = json.load(f)

    CONTAINER_ID = 'CONTAINER ID'.ljust(15,' ')
    IMAGE = 'IMAGE'.ljust(15,' ')
    STATUS = 'STATUS'.ljust(15,' ')
    NAMES = 'NAMES'.ljust(15,' ')

    print CONTAINER_ID, IMAGE, STATUS,NAMES
    
    for i in range(len(list_content)):
        if list_content[i]['Id']:
            container_id = list_content[i]['Id'][:12].ljust(15,' ')  # 左对齐，占位15个字符，不够用空白顶替
        if  list_content[i]['Image']:
            image = list_content[i]['Image'][:12].ljust(15,' ')
        if list_content[i]['Status']:
            status = list_content[i]['Status'][:12].ljust(15,' ')
        if list_content[i]['Names']:
            names = list_content[i]['Names'][:12][0].ljust(15,' ')
        print container_id,image,status, names


def main():
    
    logic_control('test.json')



    
if __name__ == '__main__':
    main()
