# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        if request:
            if len(self.finish_time_)==0:
                self.finish_time_.append(request.arrival_time+request.process_time)
                return Response(False,request.arrival_time)
            else:
               current_time=self.finish_time_[-1]
               if request.arrival_time >= current_time:  ###如果大于上一个结束时间，直接加入
                   self.finish_time_.append(request.arrival_time+request.process_time)
                   return Response(False,request.arrival_time)
               else:
                   if request.arrival_time >= self.finish_time_[0]: ###如果之前有客户完成了，increasing order
                       self.finish_time_.pop(0)  ###一个客户进，只能让一个客户出
                   self.finish_time_.append(current_time+request.process_time)
                   if len(self.finish_time_) <= self.size:  #判断是否overflow
                       return Response(False,current_time) 
                   else:  ### 加入新用户后超出柜台数，则pop掉该用户并拒绝
                       self.finish_time_.pop()
                       return Response(True,-1)
                    
     
                

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)


