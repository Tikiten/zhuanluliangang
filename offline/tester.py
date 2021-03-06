import torch
from torch.autograd import Variable
import torch.nn.functional as F
import time
import os
import sys
import json

from utils import AverageMeter, calculate_accuracy


def calculate_video_results(output_buffer, video_id, test_results, class_names):
    video_outputs = torch.stack(output_buffer)
    average_scores = torch.mean(video_outputs, dim=0)
    sorted_scores, locs = torch.topk(average_scores, k=1)
    video_results = []
    for i in range(sorted_scores.size(0)):
        label_pred= class_names[locs[i].item()]
        if label_pred in video_id:
            sum = 1
        else:
            sum = 0
        #print(video_id,label_pred)
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
        with open("D:/Spyder/zhuanluliangang/data/results/pr_label.txt","a") as f:
            f.write(label_pred + "\n")
            f.close()   
        with open("D:/Spyder/zhuanluliangang/data/results/re_label.txt","a") as f:
            f.write(video_id + "\n")
            f.close()      
            
        video_results.append({
            'label': class_names[locs[i].item()],
            #'score': sorted_scores[i].item()
        })

    test_results['results'][video_id] = video_results
    return sum

def test(data_loader, model, opt, class_names):
    model.eval()

    batch_time = AverageMeter()
    data_time = AverageMeter()

    end_time = time.time()
    acc = 0
    count = 0
    output_buffer = []
    previous_video_id = ''
    test_results = {'results': {}}
    for i, (inputs, targets) in enumerate(data_loader):
        data_time.update(time.time() - end_time)

        inputs = Variable(inputs, volatile=True)
        outputs = model(inputs)

        if not opt.no_softmax_in_test:
            outputs = F.softmax(outputs)

        for j in range(outputs.size(0)):
            if not (i == 0 and j == 0) and targets[j] != previous_video_id:
                acc = acc+calculate_video_results(output_buffer, previous_video_id,
                                        test_results, class_names)
                count =count + 1
                output_buffer = []
            output_buffer.append(outputs[j].data.cpu())
            previous_video_id = targets[j]
        if (i % 100) == 0:
            with open(
                    os.path.join(opt.result_path, '{}.json'.format(
                        opt.test_subset)), 'w') as f:
                json.dump(test_results,f)

        batch_time.update(time.time() - end_time)
        end_time = time.time()
        
        print('[{}/{}]\t'
              'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
              'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'.format(
                  i + 1,
                  len(data_loader),
                  batch_time=batch_time,
                  data_time=data_time))
    #print(count)
    print('acc',acc/count)
    with open(
            os.path.join(opt.result_path, '{}.json'.format(opt.test_subset)),
            'w') as f:
        json.dump(test_results, f)
