import pandas as pd
import json
import requests
from flask import Flask, request, Response

#constants
TOKEN = '7865788155:AAE0_ci-t5qE4VJSWjbmxUDtacquxClA5Zc'

#bot information
# https://api.telegram.org/bot7865788155:AAE0_ci-t5qE4VJSWjbmxUDtacquxClA5Zc/getMe
#
# #get updates
# https://api.telegram.org/bot7865788155:AAE0_ci-t5qE4VJSWjbmxUDtacquxClA5Zc/getUpdates
#
## #Webhook
# https://api.telegram.org/bot7865788155:AAE0_ci-t5qE4VJSWjbmxUDtacquxClA5Zc/setWebhook?url=https://admin.localhost.run/
#
# #send message
# https://api.telegram.org/bot7865788155:AAE0_ci-t5qE4VJSWjbmxUDtacquxClA5Zc/sendMessage?chat_id=6322322699&text=Hi!

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)

    r = requests.post(url, json = {'text': text})
    print('Status Code {}'.format(r.status_code))

    return None
def load_dataset(store_id):

    #loading store dataset
    df_store_raw = pd.read_csv('/Users/jessicanadalete/Documents/DSF/DS_ROSSMANN_/store.csv', low_memory=False)
    #loading test dataset + store
    df10 = pd.read_csv('/Users/jessicanadalete/Documents/DSF/DS_ROSSMANN_/test.csv', low_memory=False)

    #merging test and store dataset
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store')

    #choose store to predict
    df_test = df_test[df_test['Store']==store_id]

    if not df_test.empty:
        #removing closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)

        #convert DataFrame in json
        data = json.dumps( df_test.to_dict( orient='records' ) )

    else:
        data = 'error'

    return data

def predict(data):
    #API call
    url = 'https://test-api-rossmann-5zrj.onrender.com/rossmann/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return d1

def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace('/', '')

    try:
        store_id = int(store_id)
    except ValueError:
        store_id = 'error'

    return chat_id, store_id

#API initialize
app = Flask(__name__)

@app.route( '/', methods=['GET','POST'] )

def index():
    if request.method == 'POST':
        message = request.get_json()
        chat_id, store_id = (message)

        if store_id != 'error':
            #loading data
            data = load_dataset(store_id)

            if data != 'error':

                #prediction
                d1 = predict(data)

                #calculation
                d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

                # send message
                msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks.'.format(
                    d2.loc['store'].values[0], d2.loc['prediction'].values[0] )
                send_message(chat_id, msg)

                return Response('Ok', status=200)

        else:
            send_message(chat_id, 'Store ID not available')
            return Response('Ok', status = 200)

    else:
        return '<h1> Rossmann Telegram BOT - invalid message </h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)