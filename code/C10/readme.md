## 实现代理池功能类

```python
class ProxyPool():
    def __init__():  # 指定代理池容量并使用Redis作为队列池进行初始化
        pass

    def add(ip, score):  # 添加一个代理ip（添加过程中先判断队列是否已满，即容量是否达到上限；同时使用telnetlib包测试该代理ip是否可用）
        pass

    def decrease():  # 进行score减1操作（当score值大于某个给定阈值则将其删除）

    def random():  # 随机获取一个代理ip
```