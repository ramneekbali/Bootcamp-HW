// from data.js
var tableData = data;

// YOUR CODE HERE!

function renderTable(data) {
        var tBody = d3.select('tbody');
        d3.select('tbody').html('')
        data.map(ufo_sighting =>{
        var newTR = tBody.append("tr");
        Object.values(ufo_sighting).forEach (x=>{
            newTR.append("td").text(x)
                })
            })
        }

d3.select('#filter-btn').on('click', function(e) {
    d3.event.preventDefault();
    // Line up your potential values to filter on
    var dateVal = d3.select('#datetime').node().value;
    var cityVal = d3.select('#city').node().value;
    var stateVal = d3.select('#state').node().value;
    var countryVal = d3.select('#country').node().value;
    var shapeVal = d3.select('#shape').node().value;
    var filteredData = tableData;

    // we conditionally keep modifying a variable which is initialized
    // to the global object "tableData" above
    // if ("") will not execute
    if(dateVal) {
        filteredData = filteredData.filter(x => x.datetime == dateVal)
    }

    if(cityVal) {
        filteredData = filteredData.filter(x => x.city == cityVal)
    }

    if(stateVal) {
        filteredData = filteredData.filter(x => x.state == stateVal)
    }
    if(countryVal) {
        filteredData = filteredData.filter(x => x.country == countryVal)
    }
    if(shapeVal) {
        filteredData = filteredData.filter(x => x.shape == shapeVal)
    }
    // after all the filter options are accounted for
    renderTable(filteredData)
    
})
renderTable(data)