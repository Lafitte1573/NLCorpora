# NLGCorpora

本项目专门盘点自然语言生成（NLG）领域的高质量中文数据集。为方便下载与使用，项目特地提供了各数据集的网盘链接（网盘中的数据集与原数据集完全一致，缓存在网盘中只是为了省去繁琐的数据申请、科学上网等过程）。如果本项目对您的研究或开发有帮助，您无需做任何引用，只需送上星⭐️星⭐️一颗，十年老码农在此感谢您的支持~

<p align="center">
  <img src="figs/cover.jpeg" alt="Example Image" style="width:80%; height:auto;">
</p>

## 文本摘要（Document/Text Summarization）

#### CLTS
- **论文**：CLTS: A Chinese Long Text Summarization Dataset [[Paper]](https://link.springer.com/chapter/10.1007/978-3-030-60450-9_42)
- **会议**：NLPCC 2020
- **简介**：CLTS 是一个新的中文长文本摘要数据集，提取自中国新闻网站 ThePaper.cn。该数据集的最终版本包含超过 180,000 个长序列对，其中每篇文章由多个段落组成，每篇摘要由多个句子组成。
- **标签**：新闻摘要，长文摘要
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/660dbc1dedae)

#### LCSTS
- **论文**：LCSTS: A Large Scale Chinese Short Text Summarization Dataset [[Paper]](https://aclanthology.org/D15-1229.pdf)
- **会议**：EMNLP 2015
- **简介**：属于中文文本摘要的经典数据集，是一个由中国微博网站新浪微博构建并向公众发布的大型中文短文本摘要数据集。该语料库由 200 多万篇真实的中文短文本组成，每个文本的作者都会给出简短的摘要。
- **标签**：短文摘要
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/91fbc58aa7b8)


## 对话摘要（Dialogue/Conversation Summarization）

### 客服对话摘要

#### CSDS
- **论文**：CSDS: A Fine-Grained Chinese Dataset for Customer Service Dialogue Summarization [[Paper]](https://aclanthology.org/2021.emnlp-main.365.pdf)
- **会议**：EMNLP 2021
- **简介**：一个高质量中文客服对话摘要数据集。在 CSDS 中，每个对话标注出三种不同类型的摘要：1) 总体总结：总结了整个对话的主要信息。2) 用户摘要：关注于总结用户的主诉。3) 客服摘要：侧重于总结客服的响应。
- **标签**：对话摘要，面向角色的对话摘要（Role-oriented DS），特殊领域对话摘要
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/8c84193c7bb6)

### 医学对话摘要

#### IMCS-MRG
- **论文**：CBLUE: A Chinese Biomedical Language Understanding Evaluation Benchmark [[Paper]](https://arxiv.org/pdf/2106.08087)
- **期刊**：Arxiv 2022
- **简介**：中国生物医学语言理解评估基准（Chinese Biomedical Language Understanding Evaluation，CBLUE）定义了一系列医学领域的自然语言理解任务，包括命名实体识别、信息提取、临床诊断规范化，以及一个用于模型评估、比较和分析的相关在线平台。IMCS-MGR 是 CBLUE 的一个子集，定义了医学对话摘要任务，即从医患对话中自动生成对应的诊疗报告。
- **标签**：对话摘要，面向角色的对话摘要（Role-oriented DS），特殊领域对话摘要
- **下载链接**：IMCS-MGR 数据集有两个版本，分别在 2021 年提出 V1 版本 [[夸克网盘]](https://pan.quark.cn/s/23a67a1a1781) 和 2022 年提出V2 版本 [[夸克网盘]](https://pan.quark.cn/s/3beb5302a9ec)


## 多轮对话（Multi-turn Dialogue/Conversation）

### 闲聊

#### NaturalConv
- **论文**：NaturalConv: A Chinese Dialogue Dataset Towards Multi-turn Topic-driven Conversation [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/17649)
- **会议**：AAAI 2021
- **简介**：NaturalConv 允许参与者谈论他们在对话中提到的任何话题，并且话题转换非常流畅。该数据集包含来自六个领域的 19.9K 个对话和 400K 条对话语句，平均对话轮数为 20.1。这些对话包含对相关主题的深入讨论或多个主题之间的自然过渡。
- **标签**：话题驱动的对话
- **下载链接**：原版 [[夸克网盘]](https://pan.quark.cn/s/2099152c450b) , 处理版 [[夸克网盘]](https://pan.quark.cn/s/98e2ea4d9ac6) (注：处理版本在原版数据集的基础上加入了 dialog_release_zh.json 文件，该文件保存处理后的对话数据，可以直接读取)

#### DuLeMon
- **论文**：Long Time No See! Open-Domain Conversation with Long-Term Persona Memory [[Paper]](https://aclanthology.org/2022.findings-acl.207.pdf)
- **会议**：ACL 2022 Findings
- **简介**：DuLeMon 是一个专注于长期个性化对话和双方个性记忆的多轮中文**人机对话**数据集。DuLeMon 数据集鼓励深入的对话，其中聊天机器人需要利用已知的用户个性信息进行更深入的对话。DuLeMon 由两部分组成，DeLeMon-SELF 和 DuLeMonBOTH。其中 DeLeMon-SELF 包含 24,500 组对话，Chatbot 只知道自己的个性；而 DuLeMonBOTH 则包含3,001组对话，Chatbot 还知道部分用户的个性。
- **标签**：长期人机对话
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/ebfdb7d54859)

#### LCCC
- **论文**：A Large-Scale Chinese Short-Text Conversation Dataset [[Paper]](https://arxiv.org/pdf/2008.03946)
- **会议**：NLPCC 2020
- **简介**：一个大规模中文对话数据集，分为 base 版本（680万个对话）和 large 版本（1200万个对话）。数据集的质量由严格的数据清洗管道保证，该管道基于一组规则和一个在手动注释的 110K 对话对上训练的分类器构建
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/bee777ee6bd4)

#### CORECODE
- **论文**：CORECODE: A Common Sense Annotated Dialogue Dataset with Benchmark Tasks for Chinese Large Language Models [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/29861)
- **会议**：AAAI 2024
- **简介**：一个包含丰富常识知识的数据集，在二元对话上手动注释，旨在评估中文 LLM 的常识推理和常识冲突检测能力。数据集将日常对话中的常识分为三个维度：实体、事件和社交互动。为了便于注释和一致性，开放域对话中常识知识注释的形式标准化为“域：槽=值”。共定义了9个域和37个槽位，以获取各种常识知识。通过这些预定义的域和槽，众包从 19,700 个对话中收集了 76,787 个常识知识注释。
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/e88ad3bab560)

### 医学对话

### 客服对话

### 情感对话

#### ESConv
- **论文**：Towards Emotional Support Dialog Systems [[Paper]](https://aclanthology.org/2021.acl-long.269.pdf)
- **会议**：ACL 2021
- **简介**：清华黄民烈老师组贡献的情绪支持对话数据集，是共情对话领域少有的高质量数据集，包含 1,300 组多轮对话，每组对话还涉及情感类别、对话策略、评分等信息。
- **下载链接**：[[夸克网盘]](https://pan.quark.cn/s/d76ca5bd91cd)

#### CPED
- **论文**：CPED: A Large-Scale Chinese Personalized and Emotional Dialogue Dataset for Conversational AI [[Paper]](https://arxiv.org/pdf/2205.14727)
- **会议**：Arxiv 2022
- **简介**：CPED 数据集从 40 个中国电视节目中收集而来，由与同理心和个人特征相关的多源知识组成。这些知识涵盖了 13 种情绪、性别、大五人格特质、19 种对话行为等知识。
- **下载链接**：[[夸克网盘]](https://)

