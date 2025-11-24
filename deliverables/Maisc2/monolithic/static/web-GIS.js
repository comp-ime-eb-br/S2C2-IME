//Full screen map view
var mapId = document.getElementById('map');

function fullScreenView() {
    if (document.fullscreenElement){
        document.exitFullscreen();
    }
    else {
        mapId.requestFullscreen();
    }
}

//Map print
$('.print-map').click(function () {
    window.print();
});

//add map print
var browserControl = L.control.browserPrint({position: 'topright'}).addTo(map);

//leaflet measure
//L.control.measure().addTo(map);

//leaflet search geocode
L.Control.geocoder().addTo(map);