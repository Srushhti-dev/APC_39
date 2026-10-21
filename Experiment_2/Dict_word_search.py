#Dictionary word search using binary search
words=["Apple","Banana","Cherry","Grapes","Mango","Orange","Pineapple"]

target=input("Enter the Word to Search. ").title()

low=0
high=len(words)-1

found=False

while low <=high:
    mid=(low+high)//2

    if words[mid]==target:
        print("Word Found at index",mid)
        found=True
        break

    elif target<words[mid]:
        high=mid-1

    else:
        low=mid+1

if not found:
    print("Word not found")



#Find first 