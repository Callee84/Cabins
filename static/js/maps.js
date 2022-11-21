function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        center: {
            lat: 58.81118133962631,
            lng: 14.937803930946497
        }
    });

    const locations = [
        { lat: 61.17527493676772, lng: 13.172587798823752 },
        { lat: 56.87517295813362, lng: 16.696706115315138},
    ];

    const markers = locations.map(function (location, i) {
        const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length],
        });
    });
    const markerCluster = new markerClusterer.MarkerClusterer({map, markers});
}