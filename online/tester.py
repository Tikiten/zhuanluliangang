import time
import torch
import torch.nn.functional as F
from torch.autograd import Variable
from utils import AverageMeter


def calculate_video_results(number, output_buffer, video_id, test_results, class_names):
    video_outputs = torch.stack(output_buffer)
    average_scores = torch.mean(video_outputs, dim=0)
    sorted_scores, locs = torch.topk(average_scores, k=1)
    video_results = []
    for i in range(sorted_scores.size(0)):
        label_pred = class_names[locs[i].item()]
        if label_pred in video_id:
            sum = 1
        else:
            sum = 0
        #print(video_id,label_pred)
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有txt会自动创建
        #number用来表示当前测试的是第几个temp视频
        with open("D:/Spyder/zhuanluliangang_online/results/pr_label.txt", "a") as f:
            f.write(str(number)+" "+label_pred + "\n")
            f.close()   
            
        '''with open("D:/Spyder/zhuanluliangang_online/results/re_label.txt", "a") as f:
            f.write(str(number)+" "+video_id + "\n")
            f.close()'''      
            
        video_results.append({
            'label': class_names[locs[i].item()],
            #'score': sorted_scores[i].item()
        })

    test_results['results'][video_id] = video_results
    return sum

def test(count, data_loader, model, opt, class_names):
    model.eval()

    batch_time = AverageMeter()
    data_time = AverageMeter()

    end_time = time.time()
    acc = 0
    data_size = 0
    output_buffer = []
    previous_video_id = ''
    test_results = {'results': {}}
    for i, (inputs, targets) in enumerate(data_loader):
        data_time.update(time.time() - end_time)
        
        with torch.no_grad():
            inputs = Variable(inputs, volatile=True)

        outputs = model(inputs)
        
        if not opt.no_softmax_in_test:
            outputs = F.softmax(outputs, dim=1)

        for j in range(outputs.size(0)):
            #一般情形
            if not (i == 0 and j == 0) and targets[j] != previous_video_id:
                '''print("i,j",i,j)
                print("pre id",previous_video_id)
                print("targets",targets[j])'''
                previous_video_id = targets[j]
                test_results = {'results': {}}
                acc = acc+calculate_video_results(count, output_buffer, previous_video_id, 
                                                  test_results, class_names)
                data_size = data_size + 1
                output_buffer = []
            #第一个样本额外处理，否则不检测
            if i == 0 and j != 0:
                output_buffer = []
            else:
                '''print("here")
                print("pre id",previous_video_id)
                print("targets",targets[j])'''
                output_buffer.append(outputs[j].data.cpu())
                previous_video_id = targets[j]
                acc = acc+calculate_video_results(count, output_buffer, previous_video_id, 
                                                  test_results, class_names)
                data_size = data_size + 1
                output_buffer = []
            output_buffer.append(outputs[j].data.cpu())
            #previous_video_id = targets[j]
            #print("test results",test_results)
        '''if (i % 100) == 0:
            with open(
                    os.path.join(opt.result_path, '{}.json'.format(
                        opt.test_subset)), 'w') as f:
                json.dump(test_results,f)'''

        batch_time.update(time.time() - end_time)
        end_time = time.time()
        
        '''print('[{}/{}]\t'
              'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
              'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'.format(
                  i + 1,
                  len(data_loader),
                  batch_time=batch_time,
                  data_time=data_time))'''
    #print("data_size is :",data_size)
    #print('acc',acc/data_size)
    '''with open(
            os.path.join(opt.result_path, '{}.json'.format(opt.test_subset)),
            'w') as f:
        json.dump(test_results, f)'''
