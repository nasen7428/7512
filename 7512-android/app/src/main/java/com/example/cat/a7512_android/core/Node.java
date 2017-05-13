package com.example.cat.a7512_android.core;

import java.util.List;

/**
 * Created by cat on 2017/5/12.
 */
public class Node {
    //每一个流程的节点都包含输入，流程，输出
    //流程可以被再次分解为多个流程的组合
    String input;//输入
    String output;//输出
    String title;//标题
    String detial;//描述
    List<Node> detialStart;//详情起始节点
    List<Node> parent;//父节点
    List<Node> child;//子节点
}
