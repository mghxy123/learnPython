import axios from 'axios';
import { observable } from 'mobx';
import store from 'store';
import expire from 'store/plugins/expire';

store.addPlugin(expire);

class PostService{
    constructor(){
        this.axios = axios.create({
            baseURL:'/api/posts/'
        });
    }
    @observable msg = '';
    @observable post = {};//文章
    @observable posts = {'posts':[], 'pagination':{page:1, size:2, pages:0, total:0}}//列表
    getJwt(){
        return store.get('token','');
    }

    pub(title,content){
        console.log('title');
        axios.post(
            '/api/posts/',{
                title,
                content
            },{
                headers:{
                    'Jwt':this.getJwt()
                }
            }
        )//dev server会代理到app server
        .then(
            response => {
                // console.log(response.data);
                // console.log(response.statis);
                this.msg = '提交博文成功';
            }
        )
        .catch(
            error => {
                // console.log(error);
                this.msg = '博文提交失败'; //提示信息
            }
        )
    }
    getPost(id){
        this.axios.get(id)
        .then(
            response => {
                console.log('getPost ok');
                console.log(response.data)
                this.post = response.data.post;

            })
        .catch(
            error => {
                // console.log('getPost error');
                // console.log(error);
                this.post = {};
                this.msg = '博文加载失败';
            }
        )
    }
    list(pageNumber=1,size=2){ //默认当前是第一页,每页数量是2条
        this.axios.get(`?page=${pageNumber}&size=${size}`)
        .then(
            response => {
                console.log('--------------',response.data)
                this.posts = response.data;

            })
        .catch(
            error => {
                console.log('getPost error');
                console.log(error);
                this.posts = {};
                this.msg = '博文列表加载失败';
            }
        )
    }
}

const postService = new PostService();
export {postService};