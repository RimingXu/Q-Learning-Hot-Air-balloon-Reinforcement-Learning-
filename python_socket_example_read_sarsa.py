import gym

# 创建环境
# env = gym.make('CartPole-v1')
env = gym.make('CartPole-v1', render_mode = "human")


# 初始化环境
env.reset()

for _ in range(1000):
    # 渲染环境
    env.render()

    # 随机动作
    action = env.action_space.sample()

    # 执行动作

    observation, reward, _ , done, info = env.step(action)

    print(observation,reward)
    # 如果任务结束，则重置环境
    if done:
        env.reset()

# 关闭环境
env.close()