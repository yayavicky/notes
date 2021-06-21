

# PYTHON: GENERATORS, COROUTINES, NATIVE COROUTINES AND ASYNC/AWAIT

posted in[PYTHON](http://masnun.com/category/python) on [NOVEMBER 13, 2015](http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html) by [MASNUN](http://masnun.com/author/masnun) 

 SHARE

**NOTE:** This post discusses features which were mostly introduced with Python 3.4. And the native coroutines and async/await syntax came in Python 3.5. So I recommend you to use Python 3.5 to try the codes, if you don’t know [how to update python](https://blog.couchbase.com/tips-and-tricks-for-upgrading-from-python-2-to-python-3/), make sure to visit this website.


[原文](http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html)

------

### Generators

Generators are functions that **generates** values. A function usually `return`s a value and then the underlying scope is destroyed. When we call again, the function is started from scratch. It’s one time execution. But a generator function can `yield` a value and pause the execution of the function. The control is returned to the calling scope. Then we can again resume the execution when we want and get another value (if any). Let’s look at this example:



```py
def simple_gen():
    yield "Hello"
    yield "World"
 
 
gen = simple_gen()
print(next(gen))
print(next(gen))
```





Please notice, a generator function doesn’t directly return any values but when we call it, we get a **generator object** which is like an iterable. So we can call `next()` on a generator object to iterate over the values. Or run a `for` loop.

So how’s generators useful? Let’s say your boss has asked you to write a function to generate a sequence of number up to 100 (a super secret simplified version of `range()`). You wrote it. You took an empty list and kept adding the numbers to it and then returned the list with the numbers. But then the requirement changes and it needs to generate up to 10 million numbers. If you store these numbers in a list, you will soon run out of memory. In such situations generators come into aid. You can **generate** these numbers without storing them in a list. Just like this:



```py
def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1
 
 
nums = generate_nums()
 
for x in nums:
    print(x)
 
    if x > 9:
        break
```



We didn’t dare run after the number hit 9. But if you try it on console, you will see how it keeps generating numbers one after one. And it does so by pausing the execution and resuming – back and forth into the function context.

**Summary:** A generator function is a function that can pause execution and generate multiple values instead of just returning one value. When called, it gives us a generator object which acts like an iterable. We can use (iterate over) the iterable to get the values one by one.

### Coroutines

In the last section we have seen that using generators we can pull data from a function context (and pause execution). What if we wanted to push some data too? That’s where coroutines comes into play. The `yield` keyword we use to pull values can also be used as an expression (on the right side of “=”) inside the function. We can use the `send()` method on a generator object to pass values back into the function. This is called “generator based coroutines”. Here’s an example:

```py
def coro():
    hello = yield "Hello"
    yield hello
 
 
c = coro()
print(next(c))
print(c.send("World"))
```


OK, so what’s happening here? We first take the value as usual – using the `next()` function. This comes to `yield "Hello"` and we get “Hello”. Then we send in a value using the `send()` method. It resumes the function and assigns the value we send to `hello` and moves on up to the next line and executes the statement. So we get “World” as a return value of the `send()` method.

When we’re using generator based coroutines, by the terms “generator” and “coroutine” we usually mean the same thing. Though they are not exactly the same thing, it is very often used interchangeably in such cases. However, with Python 3.5 we have `async`/`await` keywords along with native coroutines. We will discuss those later in this post.

### Async I/O and the `asyncio` module

From Python 3.4, we have the new [asyncio](https://docs.python.org/3/library/asyncio.html) module which provides nice APIs for general async programming. We can use coroutines with the asyncio module to easily do async io. Here’s an example from the official docs:

```py	
import asyncio
import datetime
import random
 
 
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()
```


The code is pretty self explanatory. We create a coroutine `display_date(num, loop)` which takes an identifier (number) and an event loop and continues to print the current time. Then it used the `yield from` keyword to await results from `asyncio.sleep()` function call. The function is a coroutine which completes after a given seconds. So we pass random seconds to it. Then we use `asyncio.ensure_future()` to schedule the execution of the coroutine in the default event loop. Then we ask the loop to keep running.

If we see the output, we shall see that the two coroutines are executed concurrently. When we use `yield from`, the event loop knows that it’s going to be busy for a while so it pauses execution of the coroutine and runs another. Thus two coroutines run concurrently (but not in parallel since the event loop is single threaded).

Just so you know, `yield from` is a nice syntactic sugar for `for x in asyncio.sleep(random.randint(0, 5)): yield x` making async codes cleaner.

### Native Coroutines and `async`/`await`

Remember, we’re still using generator based coroutines? In Python 3.5 we got the new native coroutines which uses the async/await syntax. The previous function can be written this way:

```py
import asyncio
import datetime
import random
 
 
async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()
```



Take a look at the highlighted lines. We must define a native coroutine with the `async` keyword before the `def` keyword. Inside a native coroutine, we use the `await` keyword instead of `yield from`.

### Native vs Generator Based Coroutines: Interoperability

There’s no functional differences between the Native and Generator based coroutines except the differences in the syntax. It is not permitted to mix the syntaxes. So we can not use `await` inside a generator based coroutine or `yield`/`yield from` inside a native coroutine.

Despite the differences, we can interoperate between those. We just need to add `@types.coroutine` decorator to old generator based ones. Then we can use one from inside the other type. That is we can `await` from generator based coroutines inside a native coroutine and `yield from` native coroutines when we are inside generator based coroutines. Here’s an example:

```py
import asyncio
import datetime
import random
import types
 
 
@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))
 
 
async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()
```



### ABOUT THE AUTHOR


#### MASNUN

Whovian, *nix fan, open source enthusiast and passionate software craftsman. Loves music, hacking and playing urban terror.