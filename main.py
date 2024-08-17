user_ip_addr = input("Enter IPv4 Addr: ")
ip_addr = user_ip_addr.split('.')


z = [bin(x)[2:].zfill(8) for x in ip_addr]