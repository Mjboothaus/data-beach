import pandas as pd 

def read_google_sheet(sheet_url):
    sheet_url = sheet_url.replace(‘/edit#gid=’, ‘/export?format=csv&gid=’)
    return pd.read_csv(sheet_url)

# See: https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550