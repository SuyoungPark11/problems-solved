import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
materials = list(map(int, sys.stdin.readline().split()))
materials = sorted(materials)
start_index = 0
end_index = n-1
count = 0

while start_index < end_index:
    if (materials[start_index] + materials[end_index]) == m:
        count += 1
        start_index += 1
        end_index -= 1
    elif (materials[start_index] + materials[end_index]) > m:
        end_index -= 1
    else:
        start_index += 1
print(count)