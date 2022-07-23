gmail = input("Enter the Email : ")
k,j,d = 0,0,0
if len(gmail)>=6:
    if gmail[0].isalpha():
        if ("@" in gmail) and (gmail.count("@")==1):
            if (gmail[-4]==".") ^ (gmail[-3]=="."):
                for i in gmail:
                    if i==i.isspace():
                        k = 1
                    elif i.isalpha():
                       if i==i.upper():
                        j = 1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        d=1

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


