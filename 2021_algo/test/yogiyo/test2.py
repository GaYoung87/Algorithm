def solution(S):
    # write your code in Python 3.6
    pass

S = '''
  root r-x delete-this.xls
  root r-- bug-report.pdf
  root r-- doc.xls
  root r-- podcast.flac
 alice r-- system.xls
  root --x invoices.pdf
 admin rwx SETUP.PY
 '''
S = S.split('\n')
for i in S:
    owner = S[:6]
    perm = S[7:10]
    name = S[11:]
    print('owner, perm, name')
    print(owner, perm, name)
    print('-------------------')