import React from 'react';
import { observer } from 'mobx-react';
import {Form, Input, Button, message } from 'antd'
import BraftEditor from 'braft-editor';

import { inject } from '../utils'
import { postService as service } from '../service/post';

// import '../css/login.css';
import 'braft-editor/dist/index.css';
import 'antd/lib/form/style';
import 'antd/lib/icon/style';
import 'antd/lib/input/style';
import 'antd/lib/button/style';
import 'antd/lib/message/style';

const FormItem = Form.Item;

@inject({service})
@observer
export default class Pub extends React.Component {
    state = {
        //创建一个state,关联组件和组件输出的html内容
        editorState:BraftEditor.createEditorState('<p><a href="">马哥教育</a></p>'),
        outputHTML: '<p></p>'
    }

    handleSubmit(event){
        console.log('%%%%%%%%%%%%%%%%%');
        event.preventDefault();
        const [title, content] = event.target; //event.target返回form,而form是表单控件的数组
        // this.props.service.pub(title.value,content.value)
        console.log(title,content);
        const { outputHTML = "" } = this.state;
        console.log(outputHTML);
        this.props.service.pub(title.value,outputHTML);
    }

    // 组件内容变化更新state,引发渲染
    handleChange = (editorState) => {
        this.setState({
            editorState: editorState,
            outputHTML: editorState.toHTML()
        })
    }
    render() {
        let em = this.props.service.errMsg;
        
        // 排除的按钮
        const excludeControls = [
            'letter-spacing',
            'line-height',
            'clear',
            'headings',
            'list-ol',
            'remove-styles',
            'superscript',
            'subscript',
            'hr',
            'text-align'
        ];
        const { editorState, outputHTML } = this.state;
        return (
            <div className="editor-wrapper">
                <form className='vertical' onSubmit={this.handleSubmit.bind(this)}>
                    <FormItem label='标题' labelCol={{ span: 4 }} wrapperCol={{ span: 14 }}>
                        <Input placeholder='标题' />
                    </FormItem>
                    <FormItem label='内容' labelCol={{ span: 4 }} wrapperCol={{ span: 14 }}>
                        <BraftEditor
                            value={editorState}
                            excludeControls={excludeControls}
                            onChange={this.handleChange.bind(this)}
                            contentStyle={{ height: 400 }}
                            />
                    </FormItem>
                    <FormItem wrapperCol={{ span: 14 ,offset:4 }}>
                        <Button type="primary" htmlType="submit">提交</Button>
                    </FormItem>
                </form>
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
