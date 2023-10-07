#!/usr/bin/python3
'''
@Author: yaofei.sun
@Time: 2023-10-06 21:22:18
'''


if __name__ == '__main__':
    from datasets import load_dataset, load_metric

    dataset = load_dataset("glue", 'sst2')
    print(dataset)
    metric = load_metric('glue', 'sst2')
    print(metric)
    print()
    pass
