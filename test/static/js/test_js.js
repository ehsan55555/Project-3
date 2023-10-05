//Define gloabl variables that hold all of the data
let percentage_data;
let numbers_data;
let injuries_data;

d3.json('/api/collision').then(function(responseData) {
    let brgh_names = responseData.map(function (row){
        return row.borough;
    });
    
    console.log(brgh_names)

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
        title: "Crashes by Borough"
    };
    
    // Render the plot to the div tag with id "bar"
    Plotly.newPlot("bar1", plotData, layout);
    
    console.log(responseData);

    const dropdown = document.getElementById("selDataset");
    for (const option of brgh_names) {
      const optionElement = document.createElement("option");
      optionElement.value = option; // Set the value
      optionElement.textContent = option; // Set the displayed text
      dropdown.appendChild(optionElement); // Add the option to the dropdown
    }
});


d3.json('/api/collision_deaths').then(function(collision_data) {
    percentage_data = collision_data;
    console.log(percentage_data);
});

d3.json('/api/collision_deaths_num').then(function(nums_data) {
    numbers_data = nums_data;
    console.log(numbers_data);
});

d3.json('/api/injuries').then(function(inj_data) {
    injuries_data = inj_data;
    console.log(injuries_data);
});


function optionChanged() {
    let dropdownMenu = d3.select("#selDataset");
    let datasetId = dropdownMenu.property("value");
    console.log('datasetId',datasetId)
    console.log('test data pull',numbers_data)

    let selectedBoroughData = numbers_data.find(entry => entry["borough"] === datasetId.toString());
    let selectedBoroughpie = percentage_data.find(entry => entry["borough"] === datasetId.toString());
    let selectedBoroughinjbar = injuries_data.find(entry => entry["borough"] === datasetId.toString());

    console.log('selected_borough_data',selectedBoroughData)

    if (selectedBoroughData) {
        console.log('test meta data', selectedBoroughData);
        console.log('test ID', datasetId);

        let panelBody = d3.select(".panel-body");
        panelBody.html("");

        let metadataItems = [
            `Cyclist Deaths: ${selectedBoroughData.cyclist_death}`,
            `Motorist Deaths: ${selectedBoroughData.motorist_death}`,
            `Pedestrian Deaths: ${selectedBoroughData.pedestrian_death}`,
        ];

        metadataItems.forEach(item => {
            panelBody.append("p").text(item);
        });
    } else {
        console.log(`No data found for borough with ID: ${datasetId}`);
    }

    var pie_data = [{
        values: [selectedBoroughpie.cyclist_death_percentage, selectedBoroughpie.motorist_death_percentage
            , selectedBoroughpie.pedestrian_death_percentage, selectedBoroughpie.person_death_percentage],
        labels: ['Cyclist', 'Motorist', 'Pedestrian','Person'],
        type: 'pie'
    }];
      
    var layout = {
        title: 'Percentage of Deaths by Type',
        height: 400,
        width: 500
    };
    
      Plotly.newPlot('pie_chart', pie_data, layout);
    
      var inj_bar_data = [
        {
          x: ['Cyclists Injured','Motorists Injured','Pedestrians Injured','Total Injured'],
          y: [selectedBoroughinjbar.cyclists_injured,selectedBoroughinjbar.motorists_injured,
            selectedBoroughinjbar.pedestrians_injured,selectedBoroughinjbar.persons_injured],
          type: 'bar'
        }
      ];
  
      var layout2 = {
        title: 'Injuries in the Selected Burough',
    };

      Plotly.newPlot('bar2', inj_bar_data,layout2 );
    }