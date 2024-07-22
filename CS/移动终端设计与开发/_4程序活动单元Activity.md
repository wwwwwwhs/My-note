<!--
 * @Author: 崩布猪
 * @Date: 2024-04-09 15:26:55
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-15 13:51:26
 * @FilePath: \移动终端设计与开发\_4程序活动单元Activity.md
 * @Description: 
 * 
-->

# Activity

## 1. 定义 Activity

Activity 是 Android 应用的基本组件，它是用户与应用进行交互的界面。每个 Activity 都有一个对应的类，该类继承自 `android.app.Activity` 类。
使用频繁 创建完成后 

## 2. 生命周期

每个 Activity 都有生命周期，它是 Activity 从创建到销毁的过程。生命周期的各个阶段如下：
- 启动状态 (Starting)：当 Activity 被创建时，它处于启动状态。
- 运行状态 active (Running)：当 Activity 处于运行状态时，它处于活动状态。
- 暂停状态 (Paused)：当 Activity 处于暂停状态时，它处于非活动状态。
- 停止状态 (Stopping)：当 Activity 处于停止状态时，它处于非活动状态。
- 销毁状态 (Destroyed)：当 Activity 被销毁时，它处于终止状态。

## 3. 生命周期方法

每个 Activity 都有生命周期方法，这些方法在 Activity 生命周期的不同阶段被调用。这些方法如下：
    1. onCreate()：在 Activity 被创建时调用。
    2. onStart()：在 Activity 开始启动时调用。
    3. onResume()：在 Activity 变为可见时调用。
    4. onPause()：在 Activity 变为不可见时调用。
    5. onStop()：在 Activity 停止时调用。
    6. onDestroy()：在 Activity 被销毁时调用。

## 4. Intent(意图)

Intent 是 Android 应用间通信的一种方式。它是一种消息传递机制，用于在不同的组件之间传递数据。Intent 包含了启动 Activity 的请求，包括组件的类名、数据、Action 等。

## 5. Activity 的创建，跳转和销毁

Activity 的创建，跳转和销毁可以分为以下几个步骤：
1. 创建 Activity：在 AndroidManifest.xml 文件中声明 Activity 并设置相应的属性，然后在代码中创建该 Activity 的实例。
2. 启动 Activity：调用 startActivity() 方法，并传入 Intent 对象，启动目标 Activity。
3. 销毁 Activity：调用 finish() 方法，销毁当前 Activity。   

## 6.ViewBinding

ViewBinding 是一种 Android 开发技术，它可以帮助我们在 Activity 中绑定 findViewById() 方法，并减少 findViewById() 的使用。
通过ViewBinding，可以轻松的编写与视图交互的代码，并减少 findViewById() 的使用。

使用方法
https://www.jianshu.com/p/431c040b6af8
