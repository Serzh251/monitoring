var dataurl = '/data.geojson';

window.addEventListener("map:init", function (event) {
var map = event.detail.map;
// Download GeoJSON data with Ajax
fetch(dataurl)
  .then(function(resp) {
    return resp.json();
  })
  .then(function(data) {
    L.geoJson(data, {
      onEachFeature: function onEachFeature(feature, layer) {
        var props = feature.properties;
        var vel = ''
        if (props.transport_velocity){
              vel = `<p>velocity - ${props.transport_velocity} km/h</p>`
          };
        var content = `<h3>${props.add_datetime}</h3><p>${props.transport_name}</p>${vel}`
        layer.bindPopup(content);
    }}).addTo(map);
  });
});