
from flask import Flask, request
import json
app = Flask(__name__)


"""
Returns the longest common substring of str1 & str2
O(n^3) which is unindeal.
"""
def longest_common_substring(s1, s2):
    lcs = ''
    for i in range(len(s1)):
        for j in range(1, len(s1)+1):
            if s1[i:j] in s2 and len(s1[i:j]) > len(lcs):
                lcs = s1[i:j]
    return lcs


@app.route('/lcs', methods=['POST'])
def lcs():
    data = json.loads(request.data)
    string1 = data['string1']
    string2 = data['string2']
    response_json = {'longest_common_substring':
        longest_common_substring(string1, string2)}
    return json.dumps(response_json), 200


if __name__ == '__main__':
    app.run()


