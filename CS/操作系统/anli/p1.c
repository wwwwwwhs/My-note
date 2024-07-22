/*
 * @Author: 崩布猪
 * @Date: 2024-04-11 09:23:52
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-11 10:20:39
 * @FilePath: \操作系统\anli\p1.c
 * @Description: 演示创建一个进程 fork（） 在unix系统中
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    // 输出当前进程的PID
    printf("Hello, world (pid: %d)\n", (int)getpid());
    // 使用fork创建一个新的进程
    int rc = fork();
    if (rc < 0)
    {
        // fork失败时输出错误信息
        fprintf(stderr, "fork failed\n");
        // 退出进程并返回错误状态
        exit(1);
    }
    else if (rc == 0)
    {
        // 在子进程中输出子进程的PID
        printf("Hello, i am child (pid: %d)\n", rc);
    }
    else
    {
        // 在父进程中输出父进程和子进程的PID
        printf("Hello, i am parent (pid: %d, child pid: %d)\n", (int)getpid(), rc);
    }
    // 返回0表示程序执行成功
    return 0;
}

