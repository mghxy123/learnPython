import React from 'react';
import ReactDom from 'react-dom';
import { Menu, Icon, Layout } from 'antd';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Login from './component/login';
import Reg from './component/reg';
import Pub from './component/pub';
import Li from './component/list';
import Post from './component/post';

import 'antd/lib/layout/style';
import 'antd/lib/menu/style';
import 'antd/lib/icon/style';

const { Header, Content, Footer } = Layout;


function BasieApp() {
  return (
    <Router>
      <Layout>
        <Header>
          <Menu mode="horizontal" theme="dark" style={{ lineHeight: '64px' }} defaultSelectedKeys={["home"]}>
            <Menu.Item key='home'> <Link to="/"><Icon type='home' />首页</Link>  </Menu.Item>
            <Menu.Item key='login'> <Link to="/login"><Icon type='login' /> 登陆</Link> </Menu.Item>
            <Menu.Item key='reg'> <Link to="/reg"> 注册</Link> </Menu.Item>
            <Menu.Item key='pub'> <Link to="/pub"> 发布</Link> </Menu.Item>
            <Menu.Item key='list'> <Link to="/list"><Icon type='bars' /> 文章列表</Link> </Menu.Item>
            <Menu.Item key='about'> <Link to="/about">关于</Link> </Menu.Item>
          </Menu>
        </Header>
        <hr />
        <Content style={{ padding: '8px 50px' }}>
          <div style={{ background: '#fff', padding: 24, minHeight: 200 }}>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/pub" component={Pub} />
            <Route path="/post/:id" component={Post} />
            {/* aa这里回去找postserver,然后它的请求是baseURL:'/api/posts/' 就找到了Django */}
            <Route path="/reg" component={Reg} />
            <Route path="/list" component={Li} />
            <Route path="/login" component={Login} />
            <Route path="/always" component={Always} />
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          这个是Footer~~~~~~~~~~~~~~~~~~~~~~~
        </Footer>
      </Layout>
    </Router>
  );
}

const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
);

const Always = () => (
  <div>
    <h2>Copyright 2009-2019 hello world</h2>
  </div>
);

function About() {
  return (
    <div>
      <h2>About</h2>
    </div>
  );
}


ReactDom.render(<BasieApp />, document.getElementById('root'));


