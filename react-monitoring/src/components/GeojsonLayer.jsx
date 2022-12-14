import React from 'react';
import { GeoJSON, FeatureGroup, Popup } from 'react-leaflet';
import "../css/GeojsonLayer.css"

export default class GeojsonLayer extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      data: []
    };

    console.log('contructor');
  }

  myStyle = () => {
    return {
      color: "green",
      weight: 3,
      opacity: 1,
      fillColor: "red",
      dashArray: '8 5'
    }
  }

  render() {
    console.log('render');

    console.info(this.state.data);
    return (
      <FeatureGroup>
        {this.state.data.map(f => {
          return <GeoJSON key={f.properties.id} data={f} style={this.myStyle}>
             <Popup>
              date time - {new Date(f.properties.add_datetime).toLocaleString()}<br/>
              velocity - {f.properties.velocity} km/h<br/>
              transport - {f.properties.transport}
             </Popup>
          </GeoJSON>
        })}
      </FeatureGroup>
    );
  }

  componentDidMount() {
    if (this.props.url) {
      this.fetchData(this.props.url);
    }
    console.log('did mount');
  }

  componentWillUnmount() {
    console.log('will unmount');

  }

  fetchData(url) {
    let request = fetch(url);

    request
      .then(r => r.json())
      .then(data => {
        this.setState({
          data: data.features
        });
      }, (error) => {
        // console.error(error);
      });
  }
}