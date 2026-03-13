你说得非常对，“pooling transformer” 这个术语确实可能引起混淆。经过仔细核对论文原文，“pooling transformer”和 readout 层中的 cross‑attention 实际上是同一个东西，只是从不同角度描述。让我详细解释一下：

---

1. 为什么叫“pooling transformer”？

在 Table S1 中，这个模块被称为 Pooling transformer layers，主要是因为：

· 它位于 mean pooling 操作之后
· 它的输入正是 mean pooling 并经过复制、添加嵌入后得到的逻辑可观测量表示
· 它在整个网络中的功能角色是对 pooling 后的结果进行进一步处理（通过 transformer），因此被命名为 “pooling transformer”

这类似于我们说“分类头”、“回归头”——是根据它在网络中的位置和功能来命名的。

---

2. 它内部实际用的是 cross‑attention 吗？

是的。根据论文 Methods B.1.1（第 19‑20 页）的明确描述：

“The per‑logical observable representations cross‑attend to the final per‑stabilizer representation. After two cross‑attention transformer layers, each logical‑observable representation is processed by two residual dense layers …”

这段文字清楚地说明：

· 逻辑可观测量表示 cross‑attend 到 final per‑stabilizer 表示
· 这里使用的是 cross‑attention transformer layers
· 层数正好对应 Table S1 中的 “Pooling transformer layers” 数值

---

3. 一个模块，两个名字

所以情况是：

角度 名称 解释
功能/位置角度 Pooling transformer 因为它位于 mean pooling 之后，处理 pooling 后的结果
机制角度 Cross‑attention transformer 因为它内部使用的是 cross‑attention 机制

它们是同一个模块的两种不同称呼，并不矛盾。

---

4. 为什么会有这种命名差异？

在学术论文中，这种现象很常见：

· Table S1 是超参数表，需要简洁地描述每个模块在架构中的位置和作用，因此使用功能性的命名（Pooling transformer）
· 正文 Methods 部分需要解释具体的技术实现细节，因此使用机制性的命名（cross‑attention transformer layers）

两者描述的是同一个东西。

---

5. 结论

· Pooling transformer 和 cross‑attention 不是两个不同的模块
· 它们是同一个模块的两种描述方式：一个说它在哪（在 pooling 之后），一个说它怎么做（用 cross‑attention）
· Table S1 中的 “Pooling transformer layers” 就是指 readout 网络中的那几层 cross‑attention transformer

所以你的直觉是敏锐的——这个命名确实容易让人产生疑问，但经过原文核对可以确认它们指向同一个模块。
