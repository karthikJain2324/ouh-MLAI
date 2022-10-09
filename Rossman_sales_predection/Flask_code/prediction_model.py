df10 = pd.read_csv( '/Users/karthikjain/Desktop/ouh/Subject-6 -- Thesis & project/data/test.csv' )

df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

# choose store for prediction
df_test = df_test[df_test['Store'].isin( [30, 24, 25] )]

# remove closed days
df_test = df_test[df_test['Open'] != 0]
df_test = df_test[~df_test['Open'].isnull()]
df_test = df_test.drop( 'Id', axis=1 )

# convert Dataframe to json
data = json.dumps( df_test.to_dict( orient='records' ) )


# API Call
#url = 'http://0.0.0.0:5000/rossmann/predict'
url = 'https://rossmann-deploy.herokuapp.com/rossmann/predict'
#url = 'http://127.0.0.1/rossmann/predict'
header = {'Content-type': 'application/json' } 
data = data

r = requests.post( url, data=data, headers=header )
print( 'Status Code {}'.format( r.status_code ) )

d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )


d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

for i in range( len( d2 ) ):
    print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
            d2.loc[i, 'store'], 
            d2.loc[i, 'prediction'] ) )