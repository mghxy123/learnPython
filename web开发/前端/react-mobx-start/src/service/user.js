import axios from 'axios';
import store from 'store';
import expire from 'store/plugins/expire';

import { observable } from 'mobx';

// store.addPlugin(expire)
// // 存储cookie
// store.set('token',res.data.token, (new DataCue()).getTime()+(8*3600*1000));

// export default class UserService{
//     login (email, password){
//         console.log(email)
//         console.log(password)
//         axios.post('/api/users/login', {
//             email,password
//           }) /* dev server 会代理 */
//           .then(function (response) {
//             // console.log('response',response);
//             // console.log('data',response.data);
//             // console.log('status',response.status);
//             // console.log('statusText',response.statusText);
//             // console.log('heasers',response.headers);
//             // console.log('config',response.config);

//           })
//           .catch(function (error) {
//             console.log(error);
//           });
//     }
// }

store.addPlugin(expire)
// 存储cookie

class UserService{
    @observable loggedin = false; // +被观察者
    @observable errMsg = '';

    login (email, password){
        console.log(email)
        console.log(password)
        axios.post('/api/users/login', {
            email,password
            }) /* dev server 会代理 */
            .then(
                response=> {
                    console.log(response.data);
                    console.log(response.status);
                    // 存储token需要主义重新开启一次chrom的调试窗口才能看到
                    store.set('token',
                        response.data.token,
                        (new Date()).getTime()+ (8*3600*1000));
                        this.loggedin = true; //修改被观察者
                }
            )
            .catch(error =>{
                console.log(error);
                this.errMsg = '登录失败'; //显示错误信息
            }
        );
    }

    reg (name, email, password){
        console.log(name, email, password)
        axios.post('/api/users/', {
            name, email, password
            }) /* dev server 会代理 */
            .then(
                response=> {
                    console.log(response.data);
                    console.log(response.status);
                    // 存储token需要主义重新开启一次chrom的调试窗口才能看到
                    store.set('token',
                        response.data.token,
                        (new Date()).getTime()+ (8*3600*1000));
                        this.loggedin = true; //修改被观察者
                }
            )
            .catch(error => {
                console.log(error);
                this.errMsg = '注册失败'; //显示错误信息
            }
        );
    }
}

const userService = new UserService();

export { userService };