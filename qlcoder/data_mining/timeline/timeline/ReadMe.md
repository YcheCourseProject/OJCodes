##(一)素数
- 素数事先算好，然后把放入文件里面，开始计算时候直接Load进来，构建一个具有快速Find功能的内存中数据结构。
- 找了个网上的实现(Java的)看了看素数个数，[一个素数个数统计的知乎问答](https://www.zhihu.com/question/24942373), 稍稍改了下把素数输出出来，大概5MB

```java
package Prime;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/**
 * Created by cheyulin on 10/22/16.
 */
public class AllPrimes {

    public static int calculateNumber(int Nmax) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("primes.txt"));
        boolean[] isPrime = new boolean[Nmax + 1];
        for (int i = 3; i <= Nmax; i += 2)
            isPrime[i] = true;
        isPrime[2] = true;
        for (int i = 3; i <= Math.sqrt(Nmax); i += 2) {
            if (isPrime[i]) {
                int j = i * i;
                int n = i;
                while (j <= Nmax) {
                    isPrime[j] = false;
                    while (Nmax / j >= i) {
                        isPrime[j *= i] = false;
                    }
                    n += 2;
                    while (!isPrime[n])
                        n += 2;
                    j = i * n;
                }
            }
        }
        int primeNum = 0;
        for (int i = 1; i <= Nmax; i++) {
            if (isPrime[i] == true) {
                bufferedWriter.write(Integer.toString(i));
                bufferedWriter.newLine();
                primeNum++;
            }
        }
        bufferedWriter.close();
        return primeNum;
    }

    public static void main(String[] args) throws IOException {
        final int Nmax = 10000000;
        double startTime = System.currentTimeMillis();
        int primeNum = AllPrimes.calculateNumber(Nmax);
        double timeSpent = (System.currentTimeMillis() - startTime) / 1000;
        System.out.println("The prime numbers from 1 to " + Nmax + " is " + primeNum);
        System.out.println("Time spent : " + timeSpent + " s");
    }
}
```

```zsh
The prime numbers from 1 to 10000000 is 664579
Time spent : 0.232 s
```

##(二) 思路
- 先把素数存放在set(hash or tree)里面。
- 然后与上一题不同之处在于先 判断某数是否为素数如果是的话，通知素数的比它小的点。看了d师的思路后想法：素数发微博的事件通知的时候应该放到消息队列里面，而不是直接添加到对应的通知对象上去。查找时候通过index来查找。
- P操作时候，更新需要通知的人的index
- V操作时候，先进行filter选出符合的素数消息，然后进行set_union，把(1)那些filter出来的相关的素数的消息和(2)普通的消息合起来，然后注意是倒序哦

##(三)实现
- 然后应该跟内存访问关系比较大，还是用C++写比较好点
- md5的实现的话C++的可以找github上的，我用的是这个:  [一个github上找的C++ md5 实现](https://github.com/JieweiWei/md5)
- 实现上的数据结构考虑如下:

```cpp
class TimeLine {
public:
    using MessageType=pair<int, string>;

    TimeLine();

    string GetAnswer();

private:
    int time_stamp_{0};

    vector<string> global_msg_list_;
    vector<string> global_md5_string_list_;

    unordered_set<int> prime_number_set_;
    vector<MessageType> global_prime_msg_list_;
    vector<int> global_prime_msg_mapping_list_;

    vector<vector<MessageType>> non_prime_message_lists_;
    vector<pair<int, int>> idx_pairs_;

    void PostMessage(int entity_id, string &message);

    void VerboseMessage(int entity_id);

    string GetListMd5(vector<string> &string_list);

    string GetListMd5(vector<MessageType> &message_list);
};
```

- set_union时候的比较函数对象是这个

```cpp
auto cmp = [](pair<int, string> left, pair<int, string> right) -> bool { return left.first < right.first; };
```

##(四)优化
- 在使用vector的时候要实现算好大小，reserve好heap上的空间,预先统计出来的空间如下：

```cpp
constexpr int NUM_COUNT = 10000000;
constexpr int PRIME_COUNT = 221374;
constexpr int V_COUNT = 6666666;
constexpr int P_COUNT = 3333334;
```

- 在构造函数里面Reserve进程的heap空间

```cpp
 prime_number_set_.reserve(PRIME_COUNT);
 global_prime_msg_list_.reserve(PRIME_COUNT);
 global_md5_string_list_.reserve(V_COUNT);
 non_prime_message_lists_.resize(NUM_COUNT + 1);
 idx_pairs_.resize(NUM_COUNT + 1, std::move(pair<int, int>(0, -1)));
```

- 在写完后，要开启`-O3`编译优化进行自动向量化(single instruction multiple data)和内存使用优化

##(五)其他考虑
- C++ <experimental/algorithm>里面提供了并行的set_union，可以用用，我现在还没有加上去
- 在filter的步骤中也可以进行并行，不过对于得到的结果需要再利用并行的sort进行排序，为之后的set_union作准备，我现在还没加上去

##(六)性能
- 到后面消息队列越长，性能会越慢，所以应该考虑考虑对Filter这步操作的并行。
- 170w行p或v动作需要用时21分钟
- 290w行p或v动作需要用时57分钟
- 400w行p或v动作需要用时1小时47分钟
- 450w行p或v动作需要用时2小时14分钟
- 670w行p或v动作需要用时4小时40分钟
