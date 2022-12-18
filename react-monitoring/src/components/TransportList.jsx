import React from 'react';
import "../static/css/TransportList.css";

class TransportList extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      transport_list: []
    };

  }
  
  onChange = (e) => {
    var tr = parseInt(e.currentTarget.value);
    if (this.props.onChoose) {
      this.props.onChoose(tr);
    }
  }

  render() {
    return (
      <div className="transport-list-container">
        <select onChange={this.onChange}> 
          <option  value={0}>All</option>
          {this.state.transport_list.map(f => {
            return <option key={f.id} value={f.id}>{f.name}</option>
          })}
        </select>
      </div>
    );
  }
  componentDidMount() {
    this.fetchData();
  }
  fetchData() {
    let url = "http://127.0.0.1:8066/api/transport_list/"
    let request = fetch(url);
    request
      .then(r => r.json())
      .then(data => {
        this.setState({
          transport_list: data
        });
      }, (error) => {
        // console.error(error);
      });
  }
};

export default TransportList;