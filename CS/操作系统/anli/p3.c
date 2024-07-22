/*
 * @Author: 崩布猪
 * @Date: 2024-04-11 09:51:11
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-11 10:20:48
 * @FilePath: \操作系统\anli\p3.c
 * @Description: exec 系统调用
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

// 主函数
int main(int argc, char *argv[]) {
    // 输出当前进程的pid
    printf("hello World! (pid = %d)\n", getpid());
    // 创建子进程
    int rc = fork();
    // 判断fork是否失败
    if (rc < 0) {
        // 打印错误信息并退出
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // 子进程打印自己的pid
        printf("hello I am child: pid = %d\n", getpid());
        // 定义并初始化一个字符串数组
        char *myargs[3];
        myargs[0] = strdup("wc");
        myargs[1] = strdup("p3.c");
        myargs[2] = NULL;
        // 执行wc命令，统计文件p3.c的行数、单词数和字符数
        ecvp(myargs[0],myargs);
        // 这段代码不应该被执行到（错误处理）
        printf("this shouldn't goes down this path(math)");
    } else {
        // 等待子进程结束
        int wc = wait(NULL);
        // 父进程打印自己和子进程的pid以及子进程的退出状态
        printf("hello I am parent of %d,(wc: %d) , (pid: %d) \n",  rc, wc, (int)getpid() );
    }
    // 返回0表示程序执行成功
    return 0;
}