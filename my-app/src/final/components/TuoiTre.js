import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Row, Col } from 'antd';

TuoiTre.propTypes = {
    
};

function TuoiTre(props) {
    return (
        <Row>
            <Col span={8}>
                <img style={{width: '300px', height: '300px'}} src="" alt=""/>
                <h1>Caption</h1>
            </Col>
            <Col span={8}>
                <img style={{width: '300px', height: '300px'}} src="" alt="Caption"/>
                <h1>Caption</h1>
            </Col>
            <Col span={8}>
                <img style={{width: '300px', height: '300px'}} src="" alt=""/>
                <h1>Caption</h1>
            </Col>
        </Row>
    );
}

export default React.memo(TuoiTre);