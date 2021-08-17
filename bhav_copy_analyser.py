#Libararies
import pandas as pd
import numpy as np 
import requests
from zipfile import ZipFile
z=str(input("Give Date \n"))



#filefetcher
downloadUrl='https://archives.nseindia.com/content/historical/EQUITIES/2021/{}/cm{}2021bhav.csv.zip'.format(z[2:],z)
req=requests.get(downloadUrl)  
open('cm{}2021bhav.csv.zip'.format(z), 'wb').write(req.content)


with ZipFile('cm{}2021bhav.csv.zip'.format(z) ,'r') as zip:
    zip.printdir()
    zip.extractall()



#file input
bhav_df = pd.read_csv(r'C:\Users\Parishrut\Desktop\cm{}2021bhav.csv'.format(z), index_col=0)
print(bhav_df)

#dataclean
bhav_df.drop(['TOTALTRADES','ISIN','PREVCLOSE'],)

#max delivered
max_delivered = bhav_df.max()['TOTTRDVAL']
securitynamemaxdeliver=bhav_df.loc[bhav_df['TOTTRDVAL'] == max_delivered]
print(securitynamemaxdeliver)

#maxtraded
max_traded = bhav_df.max()['TOTTRDQTY']
securitynamemaxtraded=bhav_df.loc[bhav_df['TOTTRDQTY'] == max_traded]
print(securitynamemaxtraded)

#max%openclose
bhav_df['Maxpricechangefromopen']=bhav_df['OPEN']-bhav_df['CLOSE']
bhav_df.Maxpricechangefromopen.abs()
maxpricechangev=bhav_df.max()['Maxpricechangefromopen']
maxpricechange=bhav_df.loc[bhav_df['Maxpricechangefromopen']==maxpricechangev]
print(maxpricechange)






