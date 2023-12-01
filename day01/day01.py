# Part 1
total = 0
s = ""
with open("input.txt") as f:
    for line in f:
        first = None
        for c in line:
            if c.isdigit():
                if first == None:
                    first = c
                    s = c + c
                else:
                    s = first + c
        total += int(s)
        
print(total)

# Part 2
total = 0
s = ""
nums = {"one":"1", "two":"2", "three":"3",
"four":"4", "five":"5", "six":"6",
"seven":"7", "eight":"8", "nine":"9"}

with open("input.txt") as f:
    for line in f:
        first = None
        for i, c in enumerate(line):
            if c.isdigit():
                if first == None:
                    first = c
                    s = c + c
                else:
                    s = first + c
            else:
                for n in nums:
                    if line[i:].startswith(n):
                        if first == None:
                            first = nums[n]
                            s = first + first
                        else:
                            s = first + nums[n]
        total += int(s)
        
print(total) 
