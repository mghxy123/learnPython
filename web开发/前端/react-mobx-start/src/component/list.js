import React from 'react';
import { observer } from 'mobx-react';
import { List, Empty } from 'antd';
import { inject } from '../utils';
import { postService as service } from '../service/post';
import { Link } from 'react-router-dom'; 

import 'antd/lib/empty/style';
import 'antd/lib/list/style';

@inject({ service })
@observer
export default class Li extends React.Component {
    constructor(props){
        super(props);
        console.log('this is props',props);
        props.service.list();
    }
    onChange(pageNumber){
        console.log('pageNumber',pageNumber);
        this.props.service.list(pageNumber,2);
    }
    render(){
        console.log('list render ~~~~~~~~~~~',this.props.service)
        // 这里我明敏定义的是posts和 pagination 怎么会变成了post和pagination了? 
        // 那是因为我的Django里面写的是就pagnation 和post ,找了好半天的毛病,擦
        const {posts:data=[], pagination } = this.props.service.posts;
        // console.log('aaaaaaaaaaaaaaaaaaaaa',pagination)
        if(data.length){
            const {page: current = 1,total, size:pageSize} = pagination;
            // 这里的pagesize等于data.lenghtdata.lenght
            console.log('pageLenght/当前数据有几条',data.length);  
            console.log('totalListNum/一共有多少条',total);
            console.log('pageNum/当前是第几页',current);
            console.log('onePageSize/页最多有几条',pageSize);
            return(
                <List
                    header={<div>博文列表</div>}
                    bordered
                    dataSource={data}
                    renderItem={item =>(
                        <List.Item>
                            {/* // 这里返回的是post+id 怎么就变成了 posts+id了? */}
                            <Link to={'/post/' + item.id}>{item.title}</Link>
                        </List.Item>
                    )}
                    pagination={{
                        current,
                        total,
                        pageSize,
                        onChange: this.onChange.bind(this) //这利的this.onChange.bind(this) 绑定的就是当前页的页码,点击到了几页就是第几页的页码
                    }}
                />
            );
        }
        return <Empty />;
    }
}