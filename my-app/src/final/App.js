import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
} from '@ant-design/icons';
import {
    BrowserRouter as Router,
    Route,
    Link,
    Redirect
  } from "react-router-dom";

import TuoiTre from './components/TuoiTre';

const { Header, Sider, Content } = Layout;


function App() {
    const [collapsed, setCollapsed] = useState(false);
    
    const toggle = () => {
        setCollapsed(!collapsed);
    };

    return (
        <Router>
            <Layout>
                <Sider trigger={null} collapsible collapsed={collapsed}>
                {collapsed ? (<img style={{width: '50px', height: '60px', marginLeft: '15px'}} alt="logo" src="img/logo.png"/>) : (<h1 style={{color: 'white', fontSize: '25px', marginLeft: '40px', marginTop: '10px'}}>Group 2</h1>)}
                <div className="logo"/>
                    <Menu
                        theme="dark"
                        mode="inline" 
                        defaultSelectedKeys={['1']} 
                        // style={{marginTop: '64px'}}
                    >
                        <Menu.Item key="1" icon={<img style={{width: '20px', height: '20px'}} src="img/logo.png" alt="logo"/>}>
                            <Link to="/about"/>
                            About
                        </Menu.Item>
                        <Menu.Item key="2" icon={<img style={{width: '20px', height: '20px'}} src="img/dantri.png" alt="dantri.com.vn"/>}>
                            <Link to="/dantri"/>
                            dantri.com.vn
                        </Menu.Item>
                        <Menu.Item key="3" icon={<img style={{width: '20px', height: '20px'}} src="img/vnexpress.png" alt="vnexpress.net"/>}>
                            <Link to="vnexpress"/>
                            vnexpress.net
                        </Menu.Item>
                        <Menu.Item key="4" icon={<img style={{width: '20px', height: '20px'}} src="img/tuoitre.png" alt="tuoitre.vn"/>}>
                            <Link to="tuoitre"/>
                            tuoitre.vn
                        </Menu.Item>
                    </Menu>
                </Sider>
                
                <Layout className="site-layout">
                    <Header className="site-layout-background" style={{ padding: 0, color: 'white' }}>
                        {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
                            className: 'trigger',
                            onClick: toggle,
                        })}
                    </Header>

                    <Content
                        className="site-layout-background"
                        style={{
                            margin: '24px 16px',
                            padding: 24,
                            height: '100vh'
                        }}
                    >
                        <Route exact path="/">
                            <Redirect to="/about"/>
                        </Route>
                        <Route exact path="/about">
                            <h1>Hello 1</h1>
                        </Route>
                        <Route exact path="/dantri">
                            <h1>Hello 2</h1>
                        </Route>
                        <Route exact path="/vnexpress">
                            <h1>Hello 3</h1>
                        </Route>
                        <Route exact path="/tuoitre">
                            <TuoiTre/>
                        </Route>
                    </Content>
                </Layout>
            </Layout>
        </Router>
    );
}

export default App;