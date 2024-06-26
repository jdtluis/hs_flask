from flask import Flask, render_template, request
import os
import requests
import pandas as pd

# print(os.getcwd())
app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index(chartID = 'chart_ID', chart_height = 400): #
	#data = requests.get('https://demo-live-data.highcharts.com/aapl-ohlc.json')
	#data = data.json()
	#series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6,3,4,1,4]}, {"name": 'Label3', "data": [4, 5, 6]}]
	if request.method == 'GET':
		return render_template('/ticker_block.html', chartID='', series=[], title='', container=[])

	if request.method == "POST":
		symbols = request.form['ticker'].split(';')[:5]  # hasta 5 tickers
		settl = request.form.get('settl')
		series = {}
		title = {}
		container = {}
		for s in symbols:
			ohlc, volume = get_data(s, settl)  # , 'CDO'
			series[s] = [{
				"type": 'candlestick',
				"name": s,
				"data": ohlc},
				{
				"type": 'column',
				"name": 'Volumen',
				"data": volume,
				"yAxis": 1}]
				#"dataGrouping": {
					#"units": [['week', [1]], ['month', [1, 2, 3, 4, 6]]]}}]
			title[s] = {"text": ' - '.join([s, settl])}
			container[s] = s
	#xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	#yAxis = {"title": {"text": 'yAxis Label'}}
		return render_template('/ticker_block.html', chartID=chartID, series=series, title=title, container=container)


def get_data(symbol, datesettl='48HS'):
	data = requests.get(
		'https://open.bymadata.com.ar/vanoms-be-core/rest/api/bymadata/free/chart/historical-series/history?symbol'
		f'={symbol}%20{datesettl}&resolution=D&from=1638991971&to=1792860831', verify=False)
	data = pd.DataFrame(data.json())[['t', 'o', 'h', 'l', 'c', 'v']]
	data['t'] = data['t'].astype(float) * 1000
	data['v'] = data['v'].astype(float)  # /10000
	ohlc = data[['t', 'o', 'h', 'l', 'c']].values.tolist()
	volume = data[['t', 'v']].values.tolist()
	return ohlc, volume


#if __name__ == "__main__":
#	app.run(debug = True, passthrough_errors=True) #, host='0.0.0.0', port=8080
