Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#start with finding the company ticker on this API (https://site.financialmodelingprep.com/)
#output is a dictionary containing the income statement

def selectquote(quote):
    r= requests.get(f" ")
    r = r.json()
    
    
    #store request as variable and then conver to a data frame
    stock = r['financials']
    stock = pd.DataFrame.from_dict(stock)
    stock = stock.T
    
    stock.columns = stock.iloc[0]
    stock.reset_index(inplace=True)
    stock = stock.iloc[:,0:2]
    stock.rename(columns={ stock.columns[1]: quote }, inplace = True)
    cols = stock.columns.drop('index')
    stock[cols] = stock[cols].apply(pd.to_numeric, errors='coerce')
    stock = stock.iloc[1:,]
    #Divide whole dataframe for first row (i.e. revenue)
    stock[quote] = (stock[quote]/stock.iloc[0,1])
    #Format numbers as Percentage
    stock[quote] = pd.Series(["{0:.2f}%".format(val * 100) for val in stock[quote]], index = stock.index)
    return stock
    
#list stocks for comparison and run    
listofstocks = ['','','']
x = selectquote('')
for item in listofstocks:
    y = selectquote(item)
    x = x.merge(y,on='index')
