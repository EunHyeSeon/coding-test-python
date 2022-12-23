def solution(n, k):
    word=""
    while n:            
        word = str(n%k)+word
        n=n//k
    word=word.split("0") # 0을 기준으로 배열로 분리

    count=0
    for w in word:
        if len(w) == 0:   
            continue
        if int(w)<2:
            continue # 만약 0또는 1이거나 빈공간이라면 continue를 통해 건너뛴다.
        sosu=True
        for i in range(2,int(int(w)**0.5)+1): # 소수찾기
            if int(w)%i==0:
                sosu=False
                break
        if sosu:
            count+=1
            
    return count
