with open("Day_02/data.txt") as f:
    lines = f.readlines()

def is_safe(report: list) -> bool:
        diff_values = []
        for i in range (len(report)-1):
                        diff_values.append((report[i]-report[i+1]))
        total , neg_total = 0,0
        for i in range(1,4):
                total += diff_values.count(i)
                neg_total += diff_values.count(-i)
        if total >= (len(report)-1) or neg_total >= (len(report)-1):
                return True
        else:
                return False
                 
        
def part_1(lines : list) -> int:
        num_of_safe = 0
        for report in lines:
                report = list(map(int,report.strip().split()))
                if (is_safe(report=report)):
                        num_of_safe+=1
        return num_of_safe   
                                        
def part_2(lines : list) -> int:
        num_of_safe = 0
        for report in lines:
                report = list(map(int,report.strip().split()))
                for i in range(len(report)):
                        copy = report[:i] + report[i+1:]                       
                        if is_safe(report=copy):
                                num_of_safe+=1
                                break

        return num_of_safe
    
print(part_1(lines=lines))
print(part_2(lines=lines))

