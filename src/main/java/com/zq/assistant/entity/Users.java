package com.zq.assistant.entity;

import java.time.LocalDateTime;

import com.baomidou.mybatisplus.annotation.*;

import java.io.Serializable;
import java.util.Date;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * <p>
 *
 * </p>
 *
 * @author zq
 * @since 2023-10-13
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
public class Users implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 用户ID
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    /**
     * 用户名
     */
    private String accountName;

    /**
     * 密码
     */
    private String password;

    /**
     * 手机号
     */
    private String cell;

    /**
     * 邮箱
     */
    private String email;

    /**
     * 用户类型：0-管理员；1-普通用户
     */
    private Integer roleId;

    /**
     * 是否删除：0-未删除；1-已删除
     */
    @TableLogic
    private Integer isDeleted = 0;

    /**
     * 创建时间
     */
    @TableField(fill = FieldFill.INSERT)
    private Date createdAt;

    /**
     * 更新时间
     */
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private Date updatedAt;


}
