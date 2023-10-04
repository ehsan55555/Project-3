let data;

d3.json('/api/collision').then(function(responseData) {
    
    let brgh_names = responseData.map(function (row){
        return row.borough;
    });
    
    // Trace for the Greek Data
    let trace1 = {
        x: responseData.map(row => row.borough),
        y: responseData.map(row => row.number_of_collisions),
        type: "bar"
    };
    
    // Data trace array
    let plotData = [trace1];
    
    // Apply a title to the layout
    let layout = {
        title: "Crashes by borough"
    };
    
    // Render the plot to the div tag with id "bar"
    Plotly.newPlot("bar", plotData, layout);
    
    console.log(responseData);
});



