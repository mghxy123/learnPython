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
export default class Reg extends React.Component {
    validate(password, confirmpwd){
        //密码验证,表单验证,
        console.log('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        return password.value === confirmpwd.value;

    }
    
    handlerClick(event){
        console.log('%%%%%%%%%%%%%%%%%');
        event.preventDefault();
        const [name, email, password, confirmpwd] = event.target.form;
        console.log(password.value,confirmpwd.value);
        console.log(this.validate(password,confirmpwd)); // 验证通过后才能继续向前执行
        this.props.service.reg(name.value, email.value, password.value, confirmpwd.value);
    }
    render() {
        if (this.props.service.loggedin){
            return <Redirect to='/' />;
        }
        let em = this.props.service.errMsg;
        return (
            <div className="login-page">
                <div className="form">
                    <form className="login-form">
                        <input type="text" placeholder="用户名" defaultValue='hxy'/>
                        <input type="text" placeholder="邮箱" defaultValue='hxy@.com' />
                        <input type="password" placeholder="密码" defaultValue='hxy'/>
                        <input type="password" placeholder="密码确认" defaultValue='hxy'/>
                        <button onClick={this.handlerClick.bind(this)}>注册</button>
                        <p className="message">已经注册? <Link to="/login">请登陆</Link></p>
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
