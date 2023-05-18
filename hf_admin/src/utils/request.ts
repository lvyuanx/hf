import { requestContentTypeEnums } from '@/enums/RequestEmums';
import axios, { AxiosInstance, AxiosError, AxiosRequestConfig, AxiosResponse, InternalAxiosRequestConfig } from 'axios'
import apis from '@/apis/apis'
import { ElMessage } from 'element-plus'
// 数据返回的接口
// 定义请求响应参数，不含data
interface Result {
  code: number;
  msg: string
}


// 请求响应参数，包含data
interface ResultData<T = any> extends Result {
  data?: T;
}

const URL: string = `${import.meta.env.VITE_API_BASE_URL}`

const config = {
  // 默认地址
  baseURL: URL as string,
  // 设置超时时间
  timeout: 30000,
  // 跨域时候允许携带凭证
  withCredentials: true
}

class RequestHttp {
  // 定义成员变量并指定类型
  service: AxiosInstance;
  public constructor(config: AxiosRequestConfig) {
    // 实例化axios
    this.service = axios.create(config);

    /**
     * 请求拦截器
     * 客户端发送请求 -> [请求拦截器] -> 服务器
     * token校验(JWT) : 接受服务器返回的token,存储到vuex/pinia/本地储存当中
     */
    this.service.interceptors.request.use(
      (config: any) => {
        const token = localStorage.getItem('token') || '';
        return {
          ...config,
          headers: {
            'token': token, // 请求头中携带token信息
          }
        }
      },
      (error: AxiosError) => {
        // 请求报错
        Promise.reject(error)
      }
    )

    /**
     * 响应拦截器
     * 服务器换返回信息 -> [拦截统一处理] -> 客户端JS获取到信息
     */
    this.service.interceptors.response.use(
      (response: AxiosResponse) => {

        const { data, config } = response; // 解构

        if (response.status != 200) {
          ElMessage.error(data.msg ?? "请求发送错误")
          return Promise.reject(data)
        }

        // 文件类型，直接返回response
        if (config.headers["isFile"]) {
          return response
        }

        if (data.code && data.code !== 200) {
          ElMessage.error(data.msg); // 此处也可以使用组件提示报错信息
          return Promise.reject(data)
        }
        return data;
      },
      (error: AxiosError) => {
        const { response } = error;
        if (response) {
          this.handleCode(response.status)
        }
        if (!window.navigator.onLine) {
          ElMessage.error('网络连接失败');
          // 可以跳转到错误页面，也可以不做操作
          // return router.replace({
          //   path: '/404'
          // });
        }
      }
    )
  }
  handleCode(code: number): void {
    switch (code) {
      case 401:
        ElMessage.error('登录失败，请重新登录');
        break;
      default:
        ElMessage.error('请求失败');
        break;
    }
  }

  getContentType(request_method: string) {
    switch (request_method) {
      case "GET":
      case 'DELETE':
        return requestContentTypeEnums.FORM
      case "POST":
      case "PUT":
        return requestContentTypeEnums.JSON
    }
  }

  apiHandler(api: string) {
    let apiConfig: any = apis[api]
    let url: string
    let headers: any = {}
    let method: string
    if (!apiConfig) {
      ElMessage.error("请求地址不存在！")
      return
    }

    method = api.split("_")[0].toUpperCase()
    let contentType = this.getContentType(method)

    headers["Content-Type"] = contentType

    if (typeof apiConfig == "object") {
      headers = {
        ...headers,
        ...apiConfig.headers
      }
      url = apiConfig.url
    } else {
      url = apiConfig
    }

    return {
      url,
      method,
      headers
    }

  }

  /**
   * 发送http请求
   * @param apiKey apikey
   * @param params params 参数
   * @param data data 参数
   */
  http<T>(apiKey: string, params?: object, data?: object, formatData?: { [key: string]: any }): Promise<T> {
    let requestCfg = this.apiHandler(apiKey)
    if (!requestCfg) {
      return Promise.reject("请求失败！")
    }
    let { url, method, headers } = requestCfg
    if (formatData) {
      url = this.replaceUrlParams(url, formatData)
    }
    return this.service.request({
      url,
      method,
      headers,
      data,
      params
    })
  }

  /**
   * 文件上传
   * @param apiKey apikey
   * @param params params 参数
   * @param data data 参数
   */
  upload<T>(apiKey: string, params: object, data: object, formatData: { [key: string]: any } | null): Promise<T> {
    let requestCfg = this.apiHandler(apiKey)
    if (!requestCfg) {
      return Promise.reject("请求失败！")
    }
    let { url, method, headers } = requestCfg
    if (formatData) {
      url = this.replaceUrlParams(url, formatData)
    }
    headers["Content-Type"] = requestContentTypeEnums.FORM_DATA
    return this.service.request({
      url,
      method,
      headers,
      data,
      params
    })
  }


  /**
   * 文件下载
   * @param apiKey apikey
   * @param params params 参数
   * @param data data 参数
   */
  download<T>(apiKey: string, params: object, data: object, formatData: { [key: string]: any } | null): Promise<T> {
    let requestCfg = this.apiHandler(apiKey)
    if (!requestCfg) {
      return Promise.reject("请求失败！")
    }
    let { url, method, headers } = requestCfg
    headers["isFile"] = true
    if (formatData) {
      url = this.replaceUrlParams(url, formatData)
    }
    return this.service.request({
      url,
      method,
      headers,
      data,
      params,
      responseType: 'blob',
    })
  }

  /**
   * 将url中的${xxx} 替换成真实参数
   * @param url 请求地址
   * @param formatData 替换参数
   */
  replaceUrlParams(url: string, formatData: { [key: string]: string }): string {
    const keys = Object.keys(formatData);
    let replacedUrl = url;
    for (let i = 0; i < keys.length; i++) {
      const regExp = new RegExp(`\\$\\{${keys[i]}\\}`, 'g');
      replacedUrl = replacedUrl.replace(regExp, formatData[keys[i]]);
    }
    return replacedUrl;
  }

  downloadBlob(response: AxiosResponse) {
    const url = window.URL.createObjectURL(response.data);
    const a = document.createElement('a');
    const contentDisposition = response.headers['content-disposition'];
    const filename = contentDisposition
      ? contentDisposition.split(';')[1].split('=')[1].replace(/"/g, '')
      : 'unknown';
    a.href = url;
    a.download = decodeURIComponent(filename);
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }

}

// 导出一个实例对象
export default new RequestHttp(config);
