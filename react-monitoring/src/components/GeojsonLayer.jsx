import React from 'react';
import { FeatureGroup, Popup, Marker} from 'react-leaflet';
import TransportList from './TransportList';
import "../static/css/GeojsonLayer.css";
import L from "leaflet";

function GetIcon (_iconSize, icon){
  var icon_name = ""
  if (icon === "SHIP") {
    icon_name = "SHIP"
  }
  else {
    icon_name = "CAR"
  }
  return L.icon({
    iconUrl: require("../static/icons/" + icon_name + ".png"),
    iconSize: [_iconSize]

  })
}

export default class GeojsonLayer extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      data: [],
      show_data: []
    };
  }

  onChoose = (e) => {
    this.setState({
      show_data: []
    });  
    if (e===0) {
      this.setState({
        show_data: this.state.data
      });
    }
    else{
      var lst = []
      for (const el of this.state.data) {
        if (el.properties.transport_id===e){
          lst.push(el)
        }
      }
      this.setState({
        show_data: lst
      });  
    }
  }

  render() {
    return (
      <FeatureGroup>
        
        {this.state.show_data.map(f => {
            return <Marker  key={f.properties.id} position={[f.geometry.coordinates[1], f.geometry.coordinates[0]]} icon={GetIcon(40, f.properties.transport_type)}>
             
             <Popup >
              date time - {new Date(f.properties.add_datetime).toLocaleString()}<br/>
              velocity - {f.properties.velocity} km/h<br/>
              transport - {f.properties.transport}
             </Popup>
            </Marker>
        })}
        <TransportList onChoose={this.onChoose}/>
      </FeatureGroup>
      
    );
  }

  componentDidMount() {
    if (this.props.url) {
      this.fetchData(this.props.url);
    }
  }

  fetchData(url) {
    let request = fetch(url);

    request
      .then(r => r.json())
      .then(data => {
        this.setState({
          data: data.features,
          show_data: data.features
        });
      }, (error) => {
        // console.error(error);
      });
  }
}