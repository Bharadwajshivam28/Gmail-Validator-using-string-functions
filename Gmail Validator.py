gmail = input("Enter the Email : ")
k,j,d = 0,0,0
if len(gmail)>=6: #condition first
    if gmail[0].isalpha(): #condition second
        if ("@" in gmail) and (gmail.count("@")==1): #condition third
            if (gmail[-4]==".") ^ (gmail[-3]=="."): #condition fourth
                for i in gmail:
                    if i==i.isspace(): #if present then wrong gmail format
                        k = 1
                    elif i.isalpha(): #condition fifth
                       if i==i.upper(): #if present wrong gmail
                        j = 1
                    elif i.isdigit(): #condition sixth
                        continue
                    elif i=="_" or i=="@" or i==".": #only these symbols to be present inside gmail
                        continue
                    else:
                        d=1 #other symbol than wrong gmail

                if k==1 or j==1 or d==1:
                    print("Wrong Gmail 5!")
                else:
                    print("Right Gmail!")
            else:
                print("Wrong Gmail 4!")
        else:
            print("Wrong Gmail 3!")
    else:
        print("Wrong Gmail 2!")
else:
    print("Wrong Gmail 1!")


