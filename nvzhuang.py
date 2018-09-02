import requests

url = 'https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.2.8f1829b4HVmVmv&refpid=mm_26632258_3504122_32538762&keyword=女装&page=1'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)',
    'referer': 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&page=0',
    'cookie': 'thw=cn; t=bd746216cabc40efe98dca4bee21db5a; cna=Q1unE0ak5jgCAbfr/zYM9WzO; hng=CN%7Czh-CN%7CCNY%7C156; miid=9183127661564823838; tracknick=zy1451031007; lgc=zy1451031007; tg=0; uc3=vt3=F8dBzrSPh6rNwHYdacg%3D&id2=UonZDmOdxDQ96w%3D%3D&nk2=GdFnzTXHD%2BaQaPiW&lg2=W5iHLLyFOGW7aA%3D%3D; _cc_=UtASsssmfA%3D%3D; mt=ci=35_1&np=; enc=f%2BLaEEMSEN%2FXb8JeJGqVOMPTVeOjUhPTRkdaXrze2QAQ8EccP%2FvZVLoOechp7zowYUSRtngCw4CfhZDtNluSHw%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1; uc1=cookie14=UoTfLiXMZReLAw%3D%3D; v=0; cookie2=307d9c42211f0a92aeb75684b30dc83a; _tb_token_=f0da5e1857e80; _m_h5_tk=4b7e8c03dffe51f98f7fb4691a3a5b1a_1535880465689; _m_h5_tk_enc=9627039589c874010d857d8b6a3c1378; isg=BD09yc9EOtdtb55Xr9YjWo1pTJmbznsrOnJrnf-CeRTDNl1oxyqB_AvA5SrVm4nk'
}

resp = requests.get(url, headers=headers)

result = resp.content
with open('a.txt', 'wb') as f:
    f.write(result)


