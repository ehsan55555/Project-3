d3.json('/api/data').then(function(all_data) {
    // Use a Set to store unique 'borough' values
    const uniqueBoroughs = new Set();

    // Loop through the array of objects and collect unique 'borough' values
    all_data.forEach(function(item) {
        uniqueBoroughs.add(item.borough);
    });

    // Convert the Set back to an array for sorting (if needed)
    const borough_names = [...uniqueBoroughs];

    // Get a reference to the dropdown element
    const dropdown = document.getElementById("selDataset");

    // Create an option element for each unique borough name and add it to the dropdown
    borough_names.forEach(function(borough) {
        const optionElement = document.createElement("option");
        optionElement.value = borough; // Set the value
        optionElement.textContent = borough; // Set the displayed text
        dropdown.appendChild(optionElement); // Add the option to the dropdown
    });

    // Attach the change event listener to the dropdown after populating options
    d3.select("#selDataset").on("change", optionChanged);
});

function optionChanged() {
    // Handle the change event here
    const selectedBorough = d3.select("#selDataset").property("value");

    
    console.log("Selected Borough:", selectedBorough);
    // You can perform additional actions based on the selected borough here
}