

# Python装饰器踩坑

> 装饰器(Decorator)，顾名思义，就是对函数的一种装饰，是AOP(面向切面编程)的一种实现方式，对函数的功能做的一些增强、拓展。主要作用就是解耦，简化代码，使代码更优雅。常见场景比如插入日志、性能测试、缓存、权限校验等。
>
> `@` 符号是装饰器的`语法糖`。
>
> **坑**直接见第三点。

- 参考链接： 
  - https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html
- 演示环境：
  - `Python3.x`,`python2.x`

## 1. 最简单的装饰器

> e.g. 计算一个函数从开始到结束运行时间

```python
import time

def time_spent(f):
    """
    :param f: function
    :return: 计算函数耗时多久
    """
    def _wrapper(*args, **kwargs):
        now = time.time()
        res = f(*args, **kwargs)
        log_txt = u'Func %s spent %.2fs!' % (f.__name__, time.time() - now)
        print(log_txt)
        return res
      
    return _wrapper
```

- **使用**

```python
@time_spent
def demo():
    time.sleep(1)
    print("demo")
    
demo()
```

- **输出**

```
demo
Func demo spent 1.00s!
[Finished in 1.1s]
```

- 可以看到，在执行`demo`这个函数用了1s

## 2. 带参数的装饰器

> 装饰器中可以加参数，这样可以使装饰器更加灵活。
>
> 继续使用上面的例子。我们想加个参数，用来判断是否***发邮件***。

```python
import time

# 发邮件
def start2send_mail():
    print("Send Mail")

def time_spent(send_mail=False):
    """
    :param send_mail: 是否发邮件
    :return: 
    """
    def outer_wrapper(f):
        """
        :param f: function
        :return: 计算函数耗时多久
        """
        def _wrapper(*args, **kwargs):
            now = time.time()
            res = f(*args, **kwargs)
            log_txt = 'Func %s spent %.2fs!' % (f.__name__, time.time() - now)
            print(log_txt)
            if send_mail:
                start2send_mail()
            return res
        return _wrapper
    return outer_wrapper
```

- 使用1：发邮件

```python
@time_spent(send_mail=True)
def demo():
    time.sleep(1)
    print("demo")
    
demo()
```

- 输出

```
demo
Func demo spent 1.00s!
Send Mail
[Finished in 1.1s]
```

---

- 使用2：不发邮件

```python
@time_spent()
def demo():
    time.sleep(1)
    print("demo")
    
demo()
```

- 输出

```
demo
Func demo spent 1.00s!
[Finished in 1.1s]
```

---

- 总结：相比于不带参数的装饰器，我们在原来的基础上又嵌套了一层，使整个装饰器看起来很复杂，但是思想很简单，最外层的函数`time_spent`接收参数，传递给`outer_wrapper`，内部函数`_wrapper`可以使用`time_spent`的参数`send_mail`。

## 3. 开始套娃(使用多层装饰器)

> 当然函数是可以添加多个装饰器的，你可以根据你的需要添加。
>
> 我们使用同一个装饰器试试，例子基于***不带参数***的装饰器。

```python
@time_spent
@time_spent
@time_spent
def demo():
    time.sleep(1)
    print("demo")
    
demo()
```

- 输出

```
demo
Func demo spent 1.00s!
Func _wrapper spent 1.00s!
Func _wrapper spent 1.00s!
[Finished in 1.1s]
```

- ***这里出现了一个坑，可以看到输出信息函数名称变了，只有第一次输出的是demo，我们期望的是三次全是`demo`***
- 原因：最里层的装饰器对函数作了一次"伪装"。
- 解决：在里面的函数添加`@wraps(func)`

```python
from functools import wraps

def time_spent(f):
    @wraps(f) # <---------------添加------------
    def _wrapper(*args, **kwargs):
        now = time.time()
        res = f(*args, **kwargs)
        log_txt = 'Func %s spent %.2fs!' % (f.__name__, time.time() - now)
        print(log_txt)
        return res
    return _wrapper
```

- 输出

```
demo
Func demo spent 1.00s!
Func demo spent 1.00s!
Func demo spent 1.00s!
[Finished in 1.1s]
```



## Ps

1. 示例1装饰器的等效代码：

```python
demo = time_spent(demo)
```

2. 示例2装饰器的等效代码：

```python
demo = time_spent1(send_mail=True)(demo)
```

