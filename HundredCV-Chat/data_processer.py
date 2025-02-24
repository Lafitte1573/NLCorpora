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
