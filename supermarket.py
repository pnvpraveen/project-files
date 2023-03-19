from datetime import datetime
name=input("Enter your name:")
#list of items
lists='''
    Snakes & Biscuits            Break fast food              Health & Nutrition
    
Bingo        Rs 80/each     Kissan jam      Rs 71/each      Protinex    Rs 550/each
Lays         Rs 80/each     Saffola oats    Rs 306/each     Horlicks    Rs 266/each
Dark Fantasy Rs 100/each    Yippee          Rs 97/each      Glucose     Rs 310/kg
Oreo         Rs 85/each     Chaco flakes    Rs 289/kg       Boost       Rs 575/kg
Good day     Rs 190/each    Corn flakes     Rs 181/each     
Moms magic  Rs 80/each
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'Bingo':80,'Lays':80,'Dark Fantasy':100,'Oreo':85,'Good day':190,'Moms magic':80,
'Kissan jam':71,'Saffola oats':306,'Yippee':97,'Chaco flakes':289,'Corn flakes':181,
'Protinex':550,'Horlicks':266,'Glucose':310,'Boost':575}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*2)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","praveen supermaket",25*"=")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',4*" ",'price') 
            for i in range(len(pricelist)):
                print(i,8*' ',1*' ',ilist[i],8*' ',qlist[i],9*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")




