from datetime import datetime


class Shop:
    def __init__(self,campany_name,item):
        self.campany_name=campany_name
        self.item=item
        self.initial_kgs=0
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
        if kgs> self.initial_kgs:
            print(f"sorry! we have less kgs on stock today: {date.strftime(' %d/%m/%Y, %H:%M:%S')}")
        else:
            # strftime("%m/%d/%Y, %H:%M:%S")
            self.initial_kgs-=kgs
            print(f" you have sold { kgs} kgs  on {date.strftime(' %d/%m/%Y, %H:%M:%S')}  you have { self.initial_kgs} kgs left on your stock. ")    
            
      
    