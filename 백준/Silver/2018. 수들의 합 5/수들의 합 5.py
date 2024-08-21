n = int(input())
sum_ = 1
count = 1
start_index = 1
end_index = 1

while end_index != n :
    if sum_ > n :
        sum_ -= start_index
        start_index += 1
    elif sum_ < n : 
        end_index += 1
        sum_ += end_index
    else :
        end_index += 1
        sum_ += end_index
        count += 1
        
print(count)