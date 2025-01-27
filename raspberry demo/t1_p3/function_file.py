##function file add database , add p2p a1 listen return false to all files
## function that requests a database update,get tokens
import os.path
import time

def get_random_number(x, y):
    # Set the seed for the random number generator
    seed = int(str(time.time()).replace('.', ''))
    seed = int(str(seed)[-8:])
    # Calculate the random number
    num = (seed % (y - x + 1)) + x
    return num


def database_insert(filepath,name,apperance,seen_last,status):
    #if token doesnt exist write here rn
        if os.path.isfile(filepath) != True:
            with open(filepath,"w") as f:
                print("People:",file=f)
                print("Name, Apperance, Last Seen, Status, Id",file=f)
                f.close
 
        f=open(filepath,"r")
        lines= f.readlines()
        count = 0
        for line in lines:
                count +=1
        print()
        f.close
        with open (filepath,"r+") as f:
            for x in range(count):
                print(lines[x].strip(),file=f)
            id =r_number_generator(name,apperance,seen_last,status)
            #print(id)  
            print(name,",",apperance,",",seen_last,",",status,",",id ,file=f)
            print()
            f.close
            #print("Database was written to")
                #print(token)
            return
            
def r_number_generator(name,apperance,last_seen,status):
    x=hash(name)
    y=hash(apperance)
    z=hash(last_seen)
    a=hash(status)
    random_number =hash(x*y*z*a)
    return random_number

def database_wrapper(database):
            first =input ("do you wish to add to database (y/n):")
            if (first == "y"):
                     name =input("type in the persons name,If this is unknown, leave this section blank:")
                     apperance= input("type in the persons Apperance,If this is unknown, leave this section blank:")
                     seen_last =input("type in the persons last seen,If this is unknown, leave this section blank:")
                     status = input("type in the persons status,If this is unknown, leave this section blank:")
                     #db_insert(filepath4,name,apperance,seen_last,status)
                     database_insert(database,name,apperance,seen_last,status)


##find peer location on list,read token find line that machine token is on, return line value
def find_p_number_on_token(my_token):
    f=open("token.txt","r")
    lines= f.readlines()
    count = 0
    for line in lines:
        count+=1
    f.close
    with open ('token.txt',"r+") as f:
            i=0
            for i in range((count)-1):
                content=f.readline()
                contentsplit = content.split(",")
                tkn = int(contentsplit[2])
                if int(my_token) == tkn :
                    #print("Token is in database")
                    f.close
                    return i



#turns token value into ip address and port value by reading token.txt
def ip_fetcher(token):
    f=open("token.txt","r")
    lines= f.readlines()
    count = 0
    for line in lines:
        count+=1
    f.close
    #print ("lines in token",count)
    with open ('token.txt',"r+") as f:
            i=0
            for i in range((count)-1):
                i = i+1
                content=f.readline()
                contentsplit = content.split(",")
                tkn = int(contentsplit[2])
                #print (f"token {token}")
                #print(f"tkn {tkn}")
                #print(int(token))
                if int(token) == tkn :
                    #print("Token is in database")
                    storage = [contentsplit[0],contentsplit[1],i]
                    f.close
                    #print (storage)
                   
                    return storage  
            print("token was not found in database")  
            return False


#function checks to see if the input is a postive,whole number and that number has an associated address attached to it.
def number_check(number):
    try:
        f=open("token.txt","r")
        lines= f.readlines()
        count = 0
        for line in lines:
            count +=1
        f.close
        numbe = int(number)  
        if numbe <=0 :
            print("Input must be postive")
            return False
        elif numbe >count:
            print("There is no peer address saved with this input")
            return False
        else:
            return True
    except ValueError:
        print("Input needs to be a postive, whole number to work")
        return False


#fuction checks token.txt and will go to line inputted and store the ip and port number from that line in storage
def addres_arrays(numbercorrected):
    store=[]
    y=0
    file =  open("token.txt")
    for pos, l_num in enumerate(file):
        # check if the line number is specified in the lines to read array
        if pos in numbercorrected:
            # print the required line number
            store.append(l_num.strip("\n"))
            #print(store)
            y=y+1
    storage =[]
    for z in range(y):
        temp = store[z].split(",")
        storage.extend([temp[0],temp[1]])
    #print(storage)
    return storage

#stores array of peer tokens from file for access
def token_arrays(numbercorrected):
    store=[]
    y=0
    file =  open("token.txt")
    for pos, l_num in enumerate(file):
        # check if the line number is specified in the lines to read array
        if pos in numbercorrected:
            # print the required line number
            store.append(l_num.strip("\n"))
            #print(store)
            y=y+1
    storage =[]
    for z in range(y):
        temp = store[z].split(",")
        storage.extend([temp[2]])
    #print(storage)
    return storage

#return local token number from list 
def get_my_token(my_p_num):
    my_p_num =str(my_p_num)
    correctnums =splitting(my_p_num)
    storage = []

    storage = token_arrays(correctnums)

    return storage[0]

#function that breaks storage down and gives the ip address that is necessary
def ip_array(storage):
    global ipfull
    ipfull=[]
    y = len(storage)-1
    for i in range(y):
        ipfull.append(storage[0+(i*2)])
    return ipfull

#function that breaks storage down and gives the necessary port number to connect to.
def port_array(storage):
    global portfull
    portfull=[]
    z= len(storage)-1
    for j in range(z):
        portfull.append(storage[1+(j*2)])
    return portfull


#subtracts one from the input value,
def splitting(numbers):
    numberssplit = numbers.split(",")
    number= list(map(int,numberssplit))
    numbercorrected = [x - 1 for x in number]
    return numbercorrected

def get_peer_location(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line = lines[line_number - 1].strip()
        values = line.split(',')
        return values[-1].strip()

def database_public_creator(in_filepath, out_filepath):#input filepath is going to be database while output filepath is going to be public database.
    with open(in_filepath, 'r') as input:
        # Read the first line to get the field names
        x = input.readline().strip().split(',')        
        # Create the output file and write the header and field names
        input.close
        with open(out_filepath, 'w') as out:
            print("People:",file=out)
            #print("Name, Apperance, Last Seen, Status",file=out)
            # Write the data lines
            for line in input:
                x = line.strip().split(',')
                out.write(','.join(x[:-1]) + '\n')
            out.close

    print("public database created")

def database_read(filepath):
    # Check if file exists
    if not os.path.isfile(filepath):
        print("Error: file does not exist")
        return ["e"]
    #print("before open")
    # Open file and read contents
    with open(filepath, "r") as f:
        contents = f.readlines()
    # Remove newline characters from end of each line
    contents = [line.strip() for line in contents]
    # Return contents as list
    f.close
    return contents          

#merges arrays from second element used to print in file_comparer
def merge_arrays_no_dupes(array1, array2):
    # Combine arrays starting from the second element
    array3 = array1[2:] + array2[2:]
    # Remove duplicates and add the first element from each array
    array3 = [array1[0]] +[array1[1]] + list(set(array3))
    return array3

def write_array_to_file(filepath, array):
    with open(filepath, 'w') as f:
        for item in array:
            f.write("%s\n" % item)
            
##counts lines of a particular file
def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())
    
#returns name of peer ,last value in token.txt file
def get_peer_location(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line = lines[line_number - 1].strip()
        values = line.split(',')
        return values[-1].strip()

def file_comparer(filepath,filepath2,filepath3):
    content = database_read(filepath) 
    #print (content)
    #time.sleep(10)
    c = database_read(filepath2)
    #print(c)
    merged_array= merge_arrays_no_dupes(content,c)
    #print (merged_array)
    write_array_to_file(filepath3,merged_array)
"""
#function 1 example
def main():
    print("enter peer number which you want to connect to")
    numbers = input("")
    peer_to_ip_and_port(numbers)
    print(portfull,ipfull)
main()
"""