function buildMetadata(sample) {

  d3.json(`/metadata/${sample}`).then(function(data) {
    console.log(data);
    d3.select("#sample-metadata").html('')
    var myhtmlblock = d3.select("#sample-metadata");
    myhtmlblock.html("");

    Object.keys(data).forEach(key => {
      myhtmlblock.append('p').text(key + " " + data[key]);
    })
    
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
      
  })


  
}

function buildCharts(sample) {
  console.log(sample)
  var url = `/samples/${sample}`;
  d3.json(url).then(function(data) {

    var otu_ids = data.otu_ids.slice(0,10);
    var otu_labels = data.otu_labels.slice(0,10);
    var sample_values = data.sample_values.slice(0,10);

      //Building Bubble chart
    var bubbleData = [{
        x: otu_ids,
        y: sample_values,
        text: otu_labels,
        mode: 'markers',
        marker: {
          size: sample_values,
          color: otu_ids,
          colorscale: 'Earth'
        }
      }];      

    var bubbleLayout = {
        margin: { t: 0 },
        hovermode: 'closest',
        xaxis: {title: 'OTU ID'},
      };

    Plotly.newPlot('bubble', bubbleData, bubbleLayout);

      // Building Pie Chart
    var pieData = [{
        values: sample_values,
        labels: otu_ids,
        hovertext: otu_labels,
        hoverinfo: 'hovertext',
        type: 'pie'
      }];

    var pieLayout = {
        height: 400,
        width: 500
      };

      Plotly.newPlot('pie', pieData, pieLayout);
  })
  
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();

