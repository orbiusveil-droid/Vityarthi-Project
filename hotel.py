sel=int(input("Select rooms from the above choices(1-4):"))
n=int(input("Enter the no. of days of stay:"))
if(sel==1):
    princ=500
elif(sel==2):
    princ=2800
elif(sel==3):
    princ=3650
else:
    princ=4200


gst=princ*n*0.2

print("Amount(exclusing gst):",princ*n)

 
print("Total Amount(excluding GST):",(princ*n)+gst)
Record={}

while True:
    print("......Guestes check in.....")
    
    name=input("~Enter Name:")
    addres=input("~Enter guest permanent address:")
    citizen=input("~Enter the nationality of the guests:")
    room_no=int(input("~Enter room number:"))
    in_time=(input("~Enter check in date and time in formate(dd/mm/yyyy hh:mm):"))
    out_time=(input("~Enter check out date and time in formate(dd/mm/yyyy hh:mm):"))
    phone=int(input("~enter guets phone number:"))
    if citizen=="Indian":
        adha=(int(input("Adhar card no:")))
    else:
        adha=("passport Needed")
    Record[room_no]={'Name':name,'Citizenship':citizen,'Phone':phone,'Address':addres,'Check in time':in_time,'Adhaar No.':adha,'Check out time':out_time,'Room no':room_no}
    next_entery=input("lets fill the next entry?(yes/no):")
    if next_entery=="no":
        break
print("Room types and their prices(per night)/n")
print(Record)