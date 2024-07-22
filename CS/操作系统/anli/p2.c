/*
 * @Author: 崩布猪
 * @Date: 2024-04-11 09:41:35
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-11 10:20:43
 * @FilePath: \操作系统\anli\p2.c
 * @Description: 演示fork()函数 wait（）函数 的系统调用
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

// 主函数
int main(int argc, char const *argv[]) {
    // 打印当前进程的ID
    printf("hello world (pid : %d)\n",(int)getpid());
    // 调用fork()创建新的进程
    int rc = fork();
    // 如果fork失败, 打印错误信息并退出
    if (rc < 0) {
        printf("fork failed, returning %d\n", rc);
        exit(1);
    } 
    // 子进程执行
    else if (rc == 0) {
        // 打印子进程的ID
        printf("hello I am child (pid: %d)\n", (int)getpid());
    } 
    // 父进程执行
    else {
        // 等待子进程执行结束
        int wc = wait(NULL);
        // 打印父进程的ID、子进程的ID和子进程的结束状态
        printf("hello I am  parent of %d (wc: %d) (pid: %d)\n",rc,wc, (int)getpid());
    }
    return 0;
}