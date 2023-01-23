$(document).ready( function() {

    // split the data set into ohlc and volume
    var ohlc = series[0]['data'],
        volume = series[1]['data'],
        // set the allowed units for data grouping
        groupingUnits = [[
            'week',                         // unit name
            [1]                             // allowed multiples
        ], [
            'month',
            [1, 2, 3, 4, 6]
        ]],

        i = 0;


    // create the chart
    Highcharts.stockChart('container', {

        rangeSelector: {
            selected: 1
        },
        chart: {
        styledMode: true
        },

        title: {
            text: 'AAPL Historical'
        },

        yAxis: [{
            labels: {
                align: 'right',
                x: -3
            },
            title: {
                text: 'OHLC'
            },
            height: '60%',
            lineWidth: 2,
            resize: {
                enabled: true
            }
        }, {
            labels: {
                align: 'right',
                x: -3
            },
            title: {
                text: 'Volume'
            },
            top: '65%',
            height: '35%',
            offset: 0,
            lineWidth: 2
        }],

        tooltip: {
            split: true
        },

        series: [{
            type: 'candlestick',
            name: 'AAPL',
            data: ohlc
        }, {
            type: 'column',
            name: 'Volume',
            data: volume,
            yAxis: 1
        }]
    });
});