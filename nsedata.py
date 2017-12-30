from nsetools import Nse
import pdb
import pandas as pd

#path of the csv file
CSV_FILE_PATH = "C:\\Users\\Ronak Shah\\Google Drive\\Documents\\Shares.csv"

def get_current_stock_prices(share_list) :
    nse = Nse()
    current_data_list = []
    for share in share_list :
        current_data = nse.get_quote(share)
        #If the code is valid and we have the data
        if current_data is not None :
            current_data_list.append(current_data['lastPrice'])
        else :
            #If we do not have the data we append 0
            current_data_list.append(0)

    return current_data_list

if __name__ == '__main__' :
    #Read the csv file which has data
    df = pd.read_csv(CSV_FILE_PATH)
    current_data_list = get_current_stock_prices(df['Shares'].tolist())
    #Add new columns to dataframe
    df['Current_price'] = current_data_list
    df['Profit'] = (df.Current_price * df.Quantity) - df.Amount
    pdb.set_trace()