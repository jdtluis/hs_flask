var containers = document.getElementsByClassName('chart');

for (var i = 0; i < containers.length; i++) {
//    Highcharts.chart(containers[i], options);
//}

//$(document).ready( function() {
  // create the chart
  Highcharts.stockChart(containers[i],{
    chart: {
        styledMode: true
    }, //backgroundColor: 'transparent'},
    rangeSelector: {
      selected: 1
    },
    tooltip: {
      split: true
    },
    title: title[containers[i].id],

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

    series: series[containers[i].id]
  });
};
