print("Please enter an IPv4 IP addr for IPv4 to binary conversion and IP information generation")
user_ip_addr = input("Enter IPv4 Addr: ") #Asks the user to input an IPv4 IP address
ip_addr = user_ip_addr.split('.') #splits the users input by period(also creating a list to input the splitted result)


z = [bin(int(x))[2:].zfill(8) for x in ip_addr] #This list comprehension processes the elements of 'ip_addr'

binary_ip = ".".join(z) #joins the elements of binary_ip
print("Here you go: ", binary_ip)

#Next, I will be updating this code to give information whether the IPv4 address provided is a public or private IP address