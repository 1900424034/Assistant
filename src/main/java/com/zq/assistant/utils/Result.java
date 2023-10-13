package com.zq.assistant.utils;

public class Result<T> {

    //状态码
    private Integer status;
    //错误的状态信息
    private String message;
    //数据
    private T data;

    //get方法：获取状态码
    public Integer getStatus() {
        return status;
    }

    //get方法：获取错误状态信息
    public String getMessage() {
        return message;
    }

    //get方法：获取数据内容
    public T getData() {
        return data;
    }

    /**
     * 构造器(私有化)，这里写了3个构造器。根据实际发开需要添加即可
     */
    public Result(Integer status, String message, T data) {
        this.status = status;
        this.message = message;
        this.data = data;
    }

    public Result(Integer status, String message) {
        this.status = status;
        this.message = message;
    }

    public Result(String message) {
        this.message = message;
    }


}
