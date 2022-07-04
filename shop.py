from datetime import datetime

class Shop:
    def __init__(self,campany_name,item):
        self.campany_name=campany_name
        self.item=item
        self.initial_kgs=0
        self.inital_amount=100
        self.daily=0
        self.weekly_collection=[]
        self.weekly_kgs=[]
        self.sold_kgs=[]
        
    def stock_kgs(self,kgs):
        date=datetime.now()
        self.kgs=kgs
        if kgs<=0:
            print(f"Enter valid number of kgs")
        else:
            self.initial_kgs+=kgs
            print( f" you have the total kgs of;  {self.initial_kgs} kgs  today: {date.strftime(' %d/%m/%Y, %H:%M:%S')}" )
        
    def sold_stock(self,kgs):
        date=datetime.now()
        self.kgs=kgs  
        self.sold_kgs.append(kgs)
        if kgs> self.initial_kgs:
            print(f"sorry! we have less kgs on stock today: {date.strftime(' %d/%m/%Y, %H:%M:%S')}")
        else:
            # strftime("%m/%d/%Y, %H:%M:%S")
            self.initial_kgs-=kgs
            print(f" you have sold { kgs} kgs  on {date.strftime(' %d/%m/%Y, %H:%M:%S')}  you have { self.initial_kgs} kgs left on your stock. ")  
              
    def daily_sales(self,kgs):
        total_kgs=0
        for x in self.sold_kgs:
            total_kgs+=x
        if kgs>total_kgs:
                print(f"exceeded the number of   kgs")
              
        elif kgs<=0:
            print(f"Enter correct amount of kgs more than 0") 
        else:    
            self.daily=kgs*self.inital_amount 
            self.weekly_kgs.append(kgs)
            self.weekly_collection.append(self.daily)
        return f" Your daily amount earned is; { self.daily}"
    
    def weekly_sales(self):
        sum=0
        for i in self.weekly_collection:
            sum+=i
        total=0
        for n in self.weekly_kgs:
            total+=n
        return f" Your weekly collection has a total kgs of {total} at total amount of {sum} shs "
        
            
      
    