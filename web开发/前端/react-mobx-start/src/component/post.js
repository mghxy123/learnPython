import React from 'react';
import moment from 'moment';
import { postService as service } from '../service/post';
import { observer } from 'mobx-react';
import { message, Card, Empty } from 'antd';
import {inject} from '../utils'

import 'antd/lib/card/style';
import 'antd/lib/empty/style';
import 'antd/lib/message/style';


@inject({service})
@observer
export default class Post extends React.Component {
    constructor(props){
        super(props);
        console.log('this is Post props',props);
        let { id = -1}  = props.match.params;
        this.props.service.getPost(id);
        console.log(id)
    }

    render() {
        let em = this.props.service.msg;
        console.log('this is postservice',this.props.service)
        console.log('this is postservice1',this.props.service.post)
        console.log('this is',this.props)
        if (this.props.service.post){
            
            const { title = "", content = "", author, postdate} =this.props.service.post;
            if (title){
                return (
                    <Card title={title} extra={<a href="#">{author}</a>}>
                        <p>{moment(postdate * 1000).format('YYYY-MM-DD hh:mm:ss')}</p>
                        <p dangerouslySetInnerHTML={{__html:content}}></p>
                    </Card>
                );
            }
            else{
                return <Empty />;
            }
        }
        else{
            return <Empty />;
        }
        // const { title = "", content = "", author, postdate} =this.props.service.post;
        // if (title){
        //     return (
        //         <Card title={title} extra={<a href="#">{author}</a>}>
        //             <p>{moment(postdate * 1000).format('YYYY-MM-DD hh:mm:ss')}</p>
        //             <p dangerouslySetInnerHTML={{__html:content}}></p>
        //         </Card>
        //     );
        // }
        // else{
        //     return <Empty />;
        // }
    }
    componentDidUpdate(prevProps,prevState){ // 渲染后显示组件.
        if (prevProps.service.errMsg){
        // if (this.props.service.loggedin){ 这样写也行
            message.info(prevProps.service.errMsg,3 , () => prevProps.service.errMsg = '');
        }
    }
}