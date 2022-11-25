create table file_finger(
    file_path TEXT PRIMARY KEY NOT NULL,
    driver_name TEXT NOT NULL,
    finger TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

create index idx_finger on file_finger(finger);

.tables

.schema file_finger


F:\BaiduNetdiskDownload\存储-MYSQL提升课程 全面讲解MYSQL架构设计 打造扛得住MySQL数据库架构\数据库源代码(更多IT教程 微信352852792)\sysbench-0.5(更多IT教程 微信107564881)\sysbench(更多IT教程 微信107564881)\tests(更多IT教程 微信107564881)\threads(更多IT教程 微信107564881)\Makefile(更多IT教程 微信352852792).am
|G:\BaiduNetdiskDownload\人工智能-AI进阶年度钻石会员-黑马-价值11980元\【 主学习路线】07、阶段七 人工智能面试强化（赠送）\4--第四章 算法进阶迁移学习\1--迁移学习介绍\1.1迁移学习介绍【海量资源：666java.com】.mp4.baiduyun.downloading