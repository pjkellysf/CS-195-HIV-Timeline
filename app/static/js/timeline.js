// very primitive timeline practice
// subject to a lot of change

var container = document.getElementById('visualization');

// Create a DataSet (allows two way data-binding)
var items = new vis.DataSet([
    {id: 1, content: '5 men, all active homosexuals, were treated for Pneumocystis carinii pneumonia at 3 different hospitals in LA...', start: '1980-10', className: 'health'},
    {id: 2, content: 'CDC links the new disease to blood...', start: '1982', className: 'health'},
    {id: 3, content: 'Dr. Luc Montagnier in France isolates human immunodeficiency virus (HIV)..', start: '1983', className: 'health'},
    {id: 4, content: 'New York Times publishes its first news story on AIDS on July 3, 1981.', start: '1981-07-03', className: 'international'},
    {id: 5, content: 'First US Congressional hearings held on HIV/AIDS', start: '1982', className: 'political'},
    {id: 6, content: 'AIDS Candlelight Memorial held for the first time.', start: '1983', className: 'social'},
    {id: 7, content: 'Gaetan Dugas, listed in And The Band Played On as “patient zero,” dies.', start: '1984', className: 'celebrities'},
    {id: 8, content: 'First US Congressional hearings held on HIV/AIDS', start: '1982', className: 'political'},
  ]);

  // Configuration for the Timeline
  var options = {
    height: '500px',
    min: new Date(1975, 0, 1), // lower limit
    max: new Date(1995, 13, 31), // upper limit
    // zoomMin: 1000 * 60 * 60 * 24 * 3, // one day in milliseconds
    // zoomMax: 1000 * 60 * 60 * 24 * 31 // 24 months in milliseconds
  };

  // Create a Timeline
  var timeline = new vis.Timeline(container, items, options);
