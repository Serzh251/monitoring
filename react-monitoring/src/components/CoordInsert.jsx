import React from "react";
import { Modal, Button, Input} from 'antd';
import '../static/css/CoordInsert.css';

class CoordInsert extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      openModal: false,
      latModal: 37.5,
      longModal: 50,
      zoomModal: 10,
    };
  }
  

  showModal = () => {
    this.setState({
      openModal: true,
    });
  };

  handleOk = (e) => {
    this.props.onllzChange(this.state.latModal,this.state.longModal,this.state.zoomModal);
    this.setState({
      openModal: false,
    });
  };

  handleCancel = e => {
    console.log(e);
    this.setState({
      openModal: false,
    });
  };

  onLatChange = (e) => {
    console.log(e.target.value);
    this.setState({
      latModal: e.target.value,
    })
  }

  onLongChange = (e) => {
    console.log(e.target.value);
    this.setState({
      longModal: e.target.value,
    })
  }

  onZoomChange = (e) => {
    console.log(e.target.value);
    this.setState({
      zoomModal: e.target.value,
    })
  }

  render() {

    return (
      <div className="button-widget">
        <Button type="primary" onClick={this.showModal}>
          Open Modal
        </Button>
        <Modal
          title="Basic Modal"
          open={this.state.openModal}
          onOk={this.handleOk}
          onCancel={this.handleCancel}
        >
          <Input type="number" addonBefore="Lat" defaultValue={37.5}
            onChange = {this.onLatChange} />
          <br /><br />
          <Input type="number" addonBefore="Long" defaultValue={50}
            onChange = {this.onLongChange} />
          <br /><br />
          <Input type="number" addonBefore="Zoom" defaultValue={10}
            onChange = {this.onZoomChange} />
        </Modal>
      </div>
    );
  }
};

export default CoordInsert;