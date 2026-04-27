---
layout: default
---

<section class="home-hero">
  <div class="hero-copy">
    <p class="eyebrow">PMGG / TEST DEV / AI-NATIVE NOTES</p>
    <h1>在 AI 时代，把工程经验写成自己的判断力。</h1>
    <p class="hero-lede">这里记录测试开发、工程基础、后端应用，也记录我和 Agent、Vibe Coding、AI 工具链一起工作后的真实体感。博客不只是知识清单，更是一个持续校准自己的地方。</p>
    <div class="hero-actions">
      <a class="primary-action" href="#ai-notes">读 AI 札记</a>
      <a class="secondary-action" href="#knowledge-map">看知识地图</a>
    </div>
    <div class="hero-metrics" aria-label="博客概览">
      <div><strong>05</strong><span>AI 新札记</span></div>
      <div><strong>03</strong><span>技术主线</span></div>
      <div><strong>01</strong><span>测试开发视角</span></div>
    </div>
  </div>
  <aside class="hero-card" aria-label="作者信息">
    <img src="resource/img/yuhang.jpg" alt="PMGG avatar">
    <div class="hero-card-copy">
      <p class="terminal-label">CURRENT MODE</p>
      <h2>Build with AI, verify by myself.</h2>
      <p>让 AI 扩大可能性，让工程经验负责收束结果。</p>
    </div>
    <div class="signal-lines" aria-hidden="true">
      <span></span><span></span><span></span><span></span>
    </div>
  </aside>
</section>

<section id="ai-notes" class="section-block">
  <div class="section-heading">
    <p class="eyebrow">AI 协作札记</p>
    <h2>不是追热点，而是记录工作方式正在怎样变化。</h2>
    <p>这一组文章只写使用体验和个人判断，不写具体项目案例，也不放代码。重点是：AI 到底改变了哪些感受、边界、节奏和责任。</p>
  </div>
  <div class="post-grid featured-grid">
    <article class="post-card accent-green">
      <p class="card-kicker">效率</p>
      <h3><a href="./part_III/AI时代的个人效率体感.html">AI时代的个人效率体感</a></h3>
      <p>从“变快了”继续往下看：启动成本、反馈速度、试错方式和人的注意力正在如何重新分配。</p>
    </article>
    <article class="post-card accent-cyan">
      <p class="card-kicker">Agent</p>
      <h3><a href="./part_III/和Agent协作的边界感.html">和Agent协作的边界感</a></h3>
      <p>Agent 越能主动推进，人越需要定义目标、范围、停止点和验收标准。</p>
    </article>
    <article class="post-card accent-amber">
      <p class="card-kicker">Vibe Coding</p>
      <h3><a href="./part_III/Vibe Coding给我的新感受.html">Vibe Coding给我的新感受</a></h3>
      <p>它不是偷懒方式，而是一种把模糊感受快速外显、再由人持续收束的表达方式。</p>
    </article>
    <article class="post-card accent-pink">
      <p class="card-kicker">表达</p>
      <h3><a href="./part_III/从提示词到共同思考.html">从提示词到共同思考</a></h3>
      <p>提示词不是咒语，真正重要的是上下文、约束、偏好和共同推进的节奏。</p>
    </article>
    <article class="post-card accent-blue">
      <p class="card-kicker">判断力</p>
      <h3><a href="./part_III/AI协作时代的判断力.html">AI协作时代的判断力</a></h3>
      <p>AI 可以生成完整结果，但人必须判断它是不是可靠、克制、贴近真实需求。</p>
    </article>
  </div>
</section>

<section class="section-block philosophy-panel">
  <div>
    <p class="eyebrow">我的 AI 使用观</p>
    <h2>把低价值重复劳动交出去，把方向感和责任感留下来。</h2>
  </div>
  <div class="principle-list">
    <div>
      <strong>先定义边界</strong>
      <p>目标、约束、偏好和验收方式说清楚，Agent 才能稳定发挥。</p>
    </div>
    <div>
      <strong>先看方向</strong>
      <p>结果再完整，也要先判断有没有偏离问题本身。</p>
    </div>
    <div>
      <strong>保留审美</strong>
      <p>AI 负责给出可能性，人负责删减、排序、校准和负责。</p>
    </div>
  </div>
</section>

<section id="knowledge-map" class="section-block">
  <div class="section-heading">
    <p class="eyebrow">知识地图</p>
    <h2>技术基础、工程应用和测试开发视角并行沉淀。</h2>
  </div>
  <div class="topic-grid">
    <article class="topic-card">
      <h3>算法与数据结构</h3>
      <p>把基础能力拆开练，保持解决问题时的底层手感。</p>
      <div class="link-cloud">
        <a href="./part_I/DP动态规划.html">DP动态规划</a>
        <a href="./part_I/排序算法.html">排序算法</a>
        <a href="./part_I/树结构.html">树结构</a>
        <a href="./part_I/字符串匹配的KMP算法.html">KMP算法</a>
      </div>
    </article>
    <article class="topic-card">
      <h3>Java 与 JVM</h3>
      <p>语言、运行时、并发和集合，是长期工程判断的基本盘。</p>
      <div class="link-cloud">
        <a href="./part_I/Java多线程.html">Java多线程</a>
        <a href="./part_I/浅谈JVM.html">浅谈JVM</a>
        <a href="./part_I/Java GC.html">Java GC</a>
        <a href="./part_I/HashMap, HashTable和CurrentHashMap.html">HashMap</a>
      </div>
    </article>
    <article class="topic-card">
      <h3>网络与系统</h3>
      <p>理解请求如何抵达、连接如何建立、线程如何运行。</p>
      <div class="link-cloud">
        <a href="./part_I/在地址栏输入URL之后会发生什么？.html">URL之后</a>
        <a href="./part_I/TCP的三次握手和四次挥手.html">TCP握手挥手</a>
        <a href="./part_I/网络模型.html">网络模型</a>
        <a href="./part_I/线程和进程深度解析.html">线程和进程</a>
      </div>
    </article>
    <article class="topic-card">
      <h3>测试开发</h3>
      <p>从缺陷、生命周期和测试方法出发，形成质量视角。</p>
      <div class="link-cloud">
        <a href="./part_I/黑盒测试和白盒测试.html">黑盒和白盒</a>
        <a href="./part_I/软件测试的生命周期.html">测试生命周期</a>
        <a href="./part_I/BUG的分级.html">BUG分级</a>
      </div>
    </article>
    <article class="topic-card">
      <h3>后端应用</h3>
      <p>数据库、缓存和 Web 框架，是工程落地时绕不开的能力。</p>
      <div class="link-cloud">
        <a href="./part_II/Redis基础.html">Redis基础</a>
        <a href="./part_II/Mysql基础.html">Mysql基础</a>
        <a href="./part_II/Mysql优化.html">Mysql优化</a>
        <a href="./part_II/浅谈Spring MVC.html">Spring MVC</a>
      </div>
    </article>
    <article class="topic-card">
      <h3>工具与生活</h3>
      <p>工具是个人工作流的一部分，生活偏好也是博客气质的一部分。</p>
      <div class="link-cloud">
        <a href="./Mac常用快捷键及常见问题的解决方法.html">Mac常用快捷键</a>
        <a href="./welcome-page.html">关于 PMGG</a>
      </div>
    </article>
  </div>
</section>

<section class="section-block reading-path">
  <div class="section-heading">
    <p class="eyebrow">推荐阅读路径</p>
    <h2>如果你第一次来，可以这样读。</h2>
  </div>
  <ol class="path-list">
    <li><a href="./part_III/AI时代的个人效率体感.html">先读 AI 效率体感</a><span>理解这个博客最近为什么开始转向 AI 协作记录。</span></li>
    <li><a href="./part_III/和Agent协作的边界感.html">再读 Agent 边界感</a><span>看工具变强之后，人应该怎么重新设计自己的位置。</span></li>
    <li><a href="./part_I/软件测试的生命周期.html">回到测试开发视角</a><span>把 AI 体验落回工程质量、验证意识和长期基本功。</span></li>
  </ol>
</section>

<p class="site-note">持续更新，如果有问题欢迎和我交流探讨。</p>
