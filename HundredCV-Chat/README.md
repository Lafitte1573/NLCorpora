# 百人对话数据集

## HundredCV-Chat: A Dataset of Daily Chatting Developed on HundredCVs

![封面图片](cover.jpg)

### 简介

本项目提出一个全新的中文多轮对话数据集（HundredCV-Chat），该数据集由 100 位青年的简历数据集 HundredCVs 开发而来，共包含 24,750 组日常闲聊对话数据。

数据集具有如下特点：
1. **自动化标注**：HundredCV-Chat 中的对话均由 Deepseek-V3 大模型生成，不涉及任何人工标注，因此同时保证了大规模数据量和低成本优势。
2. **多样性话题**：HundredCV-Chat 中的对话话题涵盖了校园生活、工作经验、兴趣爱好、生活琐事等多个方面，与真实生活联系紧密，尤其适用于开发年轻化应用。
3. **高质量对话**：利用 Deepseek 强大的生成能力和全面的知识，HundredCV-Chat 的对话内容在流畅度、拟人性、多样性方面均显著优于现有的开源对话数据集。

### 数据样例
HundredCV-Chat 含有 24,750 组多轮对话实例，每组对话数据由四个字段构成，分别是话题（topic）、第一个说话人（user1）、第二个说话人（user2）和对话内容（dialog）。
其中第一个说话人和第二说话人均为 HundredCVs 中的真实人物，而话题和对话内容均由 Deepseek-V3 自动生成。

下面给出一个数据样例：
```json
{
  'topic': '校园生活分享', 
  'user1': '李欣怡', 
  'user2': '杨欢', 
  'dialog': [
    'user1：杨欢，最近校园里有什么新鲜事吗？', 
    'user2：嗨，李欣怡！我们学校刚刚举办了一次科技节，很多学生展示了他们的发明。', 
    'user1：听起来好有趣！我这边的学校正在筹备一场文化节，主要是推广传统文化。', 
    'user2：文化节听起来也很棒。你们会做哪些活动呢？', 
    'user1：我们打算办个书法展和传统服饰秀，还会请来一些老师教大家制作传统小吃。', 
    'user2：真不错！我们科技节上有同学展示了一款智能垃圾分类箱，挺受欢迎的。', 
    'user1：这创意真好。我们也应该多关注环保问题，比如组织一次清洁校园的活动。', 
    'user2：对，我也觉得这样做很有意义。你们学校有类似的社团或小组吗？', 
    'user1：有的，我们有一个志愿者服务队，经常会组织这样的活动。', 
    'user2：那真是太好了！你平时是怎么平衡学业和这些课外活动的呢？', 
    'user1：我会合理安排时间，把学习放在第一位，然后是重要的活动。你觉得呢？', 
    'user2：我也是这样做的。我觉得找到自己的兴趣点很重要，这样才能更有动力去做好每一件事。', 
    'user1：完全同意！对了，你参加过模拟联合国社团吗？', 
    'user2：参加过，挺有意思的。你呢？有没有类似的经历？', 
    'user1：有啊！我还当过中国代表团的代表，提出了很多关于可持续发展的建议。', 
    'user2：真厉害！你在这些活动中一定学到了不少东西吧？', 
    'user1：当然了，不仅增长见识还锻炼了我的团队合作能力。你也一样吧？', 
    'user2：是的，我也从中受益匪浅，特别是编程能力和解决问题的能力得到了提升。', 
    'user1：希望以后我们能有更多机会一起交流学习经验。', 
    'user2：绝对同意！我们可以互相分享更多的校园活动信息和心得。'
  ]
}
```

### 构建过程
HundredCV-Chat 基于 HundredCVs 采用自动化的方式构建而成。其完整的构建过程主要分为以下几个步骤：
1. **场景生成**：从 HundredCVs 中无放回地挑选出成对的角色作为「说话人1」和「说话人2」构建对话场景。由于 HundredCVs 包含 100 个不同的人物，因此共得到 C(100,2) = 4950 组对话场景。
2. **话题生成**：在每个对话场景下，要求 Deepseek-V3 根据对话双方的个人经历和详细经历，生成至少5个不同的话题。
3. **对话生成**：对于每个话题，要求 Deepseek-V3 生成一段对话内容。从而得到共 4950 * 5 = 24750 组对话数据。

```python
"""
该脚本基于百人简历数据合成多轮闲聊对话数据集
"""

import argparse
import json

import ollama
import re

from tqdm import tqdm


def data_generate(data_u1, data_u2, model='deepseek-v3'):
    user1 = data_u1['姓名']
    profile_1 = '\n'.join([f'{k}: {v}' for k, v in data_u1.items() if k not in ['个人经历', '详细经历', '个人自述']])
    se1 = '\n\t'.join(data_u1['个人经历'])
    profile_1 += '\n' + f'个人经历: {se1}'

    user2 = data_u2['姓名']
    profile_2 = '\n'.join([f'{k}: {v}' for k, v in data_u2.items() if k not in ['个人经历', '详细经历', '个人自述']])
    se2 = '\n\t'.join(data_u2['个人经历'])
    profile_2 += '\n' + f'个人经历: {se2}'

    messages = [{
        'role': 'user',
        'content': f'{profile_1}\n\n{profile_2}\n\n以上是{user1}和{user2}的基本信息，他们即将进行一次对话，请预测他们对话的主题可能有哪些？'
                   f'以**话题**的格式输出预测结果，每个话题用不超过10个字概括，相邻两个话题间用换行符分隔，不要输出其他任何无关的信息。'
    }]
    response = ollama.chat(
        model=model,
        messages=messages
    )

    try:
        conversations = []
        topics = re.findall(r"\*\*(.*?)\*\*", response['message']['content'])
        topic_bar = tqdm(topics[:5])
        for topic in topic_bar:
            topic_bar.set_postfix({
                "Users": f"{user1}-{user2}",
                'Topic': topic,
            })
            messages = [{
                'role': 'user',
                'content': f'{profile_1}\n\n{profile_2}\n\n以上是{user1}和{user2}的基本信息，他们即将进行一次对话，'
                           f'对话主题为**{topic}**，请根据主题，预测他们的对话内容。要求对话语句尽量简短，轮次尽量多，'
                           f'直接输出对话内容，不要输出其他任何无关的信息。'
            }]
            response = ollama.chat(
                model=model,
                messages=messages
            )
            dialog = response['message']['content']
            # print(dialog)
            conversations.append({
                'topic': topic,
                'user1': user1,
                'user2': user2,
                'dialog': dialog.split('\n\n'),
            })
        return conversations
    except Exception as e:
        print(e)
        return


def run(model: str = 'deepseek-v3', in_file='./hundred_cvs.jsonl', out_file='./hundred_chat.jsonl'):
    with open(in_file, 'r') as f:
        data = json.load(f)

    users = [line['姓名'] for line in data]
    print(len(users))
    for user1 in users:
        # print(users.index(user1))
        for user2 in users[users.index(user1) + 1:]:
            print(f'Generating data for {user1} and {user2}...')
            json_lines = data_generate(data[users.index(user1)], data[users.index(user2)], model=model)
            if json_lines:
                with open(out_file, 'a') as f:
                    f.write('\n'.join([json.dumps(line, ensure_ascii=False) for line in json_lines]) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # 添加 dataset 参数
    parser.add_argument('-m', '--model', type=str, default='deepseek-v3', help='generation model')
    parser.add_argument('-i', '--input_file', type=str, default='./hundred_cvs.jsonl', help='input file')
    parser.add_argument('-o', '--output_file', type=str, default='./hundred_chat.jsonl', help='output file')

    # 解析命令行参数
    args = parser.parse_args()

    # run
    run(model=args.model, out_file=args.output_file)
```

### 统计信息

以下对比了 HundredCV-Chat 和其他几个知名的中文多轮对话数据集，HundredCV-Chat 在多个方面表现出显著优势：

|      数据集       |  样本数   | 平均对话长度 | 平均对话轮数 | 总话题数 |  总回合数   | 人物数 |
|:--------------:|:------:|:------:|:------:|:----:|:-------:|:---:|
| HundredCV-Chat | 24,750 | 496.28 | 15.66  | 4871 | 387,657 | 100 |
|  NaturalConv   | 19,919 | 216.63 |  9.44  |  --  | 188,068 | --  |
|    DuLeMon     | 23,000 | 145.57 |  8.60  |  --  | 197,904 | --  |

> **注意**：1) 对话长度统计中文字符数、标点符号、英文单词等；2) 两个说话人的一次交互被认为是一轮对话；3) NaturalConv 和 DuLeMon 均采用匿名方式，因此无法统计人物数

### 应用场景
本数据集的应用场景包括但不限于以下几种：
- **对话系统**：本数据集提供大量高质量的多轮对话数据，可用于对话模型的训练和测试。
- **角色扮演**：本数据集中的人物角色与 HundredCVs 一一对应，开发者可将这两个数据集与配合使用，构建出基于简历的角色扮演对话系统。
- **话题建模**：我们为每一组对话数据都标注了话题，可以用于主题建模的训练和评估。
- **条件对话生成**：开发者可仿照本数据集的构建方式，将对话话题和角色的简历信息作为条件，训练对话生成模型根据给定条件生成多轮对话。


### 数据集使用
如果我们的工作对您有帮助，请按照以下方式引用：
```
@misc{HundredCVs,
    title={HundredCV-Chat: A Dataset of Daily Chatting Developed on HundredCVs},
    author={Jiaxin Duan, Fengyu Lu},
    year={2024},
    howpublished={\url{https://github.com/Lafitte1573/NLCorpora}},
    note={Accessed: 31 December 2024}
}
```
