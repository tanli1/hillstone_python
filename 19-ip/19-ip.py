#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:tan
#

import IPy
from faker import Faker
from faker.providers import internet

fake=Faker()

def ipAdd(ip_1,ip_2):
    if IPy.IP(ip_1).version() == 4 and IPy.IP(ip_2).version() == 4:
        rslt = int(IPy.IP(ip_1).int()) + int(IPy.IP(ip_2).int())
        if rslt > IPy.MAX_IPV4_ADDRESS:   #0xffffffff
            print 'Add the results of IPv4 address is to large!'
            return None
        return IPy.intToIp(rslt,4)
    elif IPy.IP(ip_1).version() == 6 and IPy.IP(ip_2).version() == 6:
        rslt = int(IPy.IP(ip_1).int()) + int(IPy.IP(ip_2).int())
        if rslt > IPy.MAX_IPV6_ADDRESS:   #0xffffffffffffffffffffffffffffffff
            print 'Add the results of IPv6 address is to large!'
            return None
        return IPy.intToIp(rslt,6)
    else:
        return None

# def ipToInt(ip):
#     o = map(int, ip.split('.'))
#     res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
#     return res

# def isInSameNetwork(ip,ipNetwork,netmask):
#     ipInt = ipToInt(ip)    # my test ip, in int form

#     maskLengthFromRight = 32 - netmask

#     ipNetworkInt = ipToInt(ipNetwork)          # convert the ip network into integer form
#     binString = "{0:b}".format(ipNetworkInt)   # convert that into binary (string format)

#     chopAmount = 0           # find out how much of that int I need to cut off
#     for i in range(maskLengthFromRight):
#         if i < len(binString):
#             chopAmount += int(binString[len(binString)-1-i]) * 2**i

#     minVal = ipNetworkInt-chopAmount
#     maxVal = minVal+2**maskLengthFromRight -1

#     return minVal <= ipInt and ipInt <= maxVal

def isInSameNetwork(ip_1,ip_2,netmask):
    ip1 = IPy.IP(ip_1).make_net(netmask) 
    ip2 = IPy.IP(ip_2).make_net(netmask)
    if ip1 == ip2:
    	return True
    else:
        return False


def is_ip(ip):
    try:
        IPy.IP(ip)
        return True
    except Exception as e:
        return False

def version():
    v4 = fake.ipv4(network=False)
    ipv4 = IPy.IP(v4).version()
    print 'IP address %s version is : %s' %(v4,ipv4)
    v6 = fake.ipv6(network=False)
    ipv6 = IPy.IP(v6).version()
    print 'IPv6 address %s version is : %s' %(v6,ipv6)


def main():
    # 1. 完成IP地址的加法操作，如ipAdd('192.168.0.1', 1)结果为192.168.0.2，ipAdd('192.168.0.1','0.0.1.0')的结果为192.168.1.1
    print '-'*60
    v4_1 = fake.ipv4(network=False)
    v4_2 = fake.ipv4(network=False)
    rslt = ipAdd(v4_1,v4_2)
    if rslt:
        print 'IP %s add IP %s equal %s' %(v4_1,v4_2,rslt)
    else:
        print 'IP address is different or wrong  '

    v6_1 = fake.ipv6(network=False)
    v6_2 = fake.ipv6(network=False)
    rslt = ipAdd(v6_1,v6_2)
    if rslt:
        print 'IP %s add IP %s equal %s' %(v6_1,v6_2,rslt)
    else:
        print 'IP address is different or wrong  '


    # 2.判断两个IP是否属于同一个子网isInSameNetwork("192.168.0.1","192.168.2.0",24)
    print '-'*60
    v4_1 = fake.ipv4(network=False)
    v4_2 = fake.ipv4(network=False)
    netmask = int(24)
    print 'IP address: ',v4_1
    print 'IP address: ',v4_2
    rslt = isInSameNetwork(v4_1,v4_2,netmask)
    if rslt:
     print 'IP address %s and %s netmask %s is in same network' %(v4_1,v4_2,netmask)
    else:
     print 'IP address %s and %s netmask %s is not in same network' %(v4_1,v4_2,netmask)


    # 3.判断IP地址是否合法
    print '-'*60
    v4 = fake.ipv4(network=False)
    v6 = fake.ipv6(network=False)
    rslt = is_ip(v4)
    if rslt:
        print 'IP address %s is valid' %v4
    else:
        print 'IP address %s is invalid' %v4
    rslt = is_ip(v6)
    if rslt:
        print 'IP address %s is valid' %v6
    else:
        print 'IP address %s is invalid' %v6
   
    
    # 4. 获取IP地址的版本号
    print '-'*60
    version()

    
if __name__ == '__main__':
    main()
