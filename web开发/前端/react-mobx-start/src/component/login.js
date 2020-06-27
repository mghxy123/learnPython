import React from 'react';
import { Link, Redirect } from 'react-router-dom';
import '../css/login.css';
import { userService as service } from '../service/user';
import { observer } from 'mobx-react';
import { message } from 'antd';
import {inject} from '../utils'

import 'antd/lib/message/style';

@inject({service})
@observer
export default class Login extends React.Component {
    handlerClick(event){
        event.preventDefault();
        let fm = event.target.form;
        this.props.service.login(
            fm[0].value,
            fm[1].value
        );
    }
    render() {
        console.log('########################')
        console.log(this.props)
        console.log('============================')
        console.log(this.props.service.loggedin)
        if (this.props.service.loggedin) return <Redirect to='/' />;

        let em = this.props.service.errMsg;
        return (
            <div className="login-page">
                <div className="form">
                    <form className="login-form">
                        <input type="text" placeholder="邮箱" defaultValue='hxy@.com'/>
                        <input type="password" placeholder="密码" defaultValue='hxy'/>
                        <button onClick={this.handlerClick.bind(this)}>登陆</button>
                        <p className="message">还未注册? <Link to="/reg">注册</Link></p>
                    </form>
                </div>
            </div>
        )
    }
    componentDidUpdate(prevProps,prevState){ // 渲染后显示组件.
        if (prevProps.service.errMsg){
        // if (this.props.service.loggedin){ 这样写也行
            message.info(prevProps.service.errMsg,3 , () => prevProps.service.errMsg = '');
        }
    }
}