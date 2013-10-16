
from flask import Flask, request
import simplejson
app = Flask(__name__)


"""
Returns the longest common substring of str1 & str2
"""
def longest_common_substring(str1, str2):
    pass


@app.route('/lcs', methods=['POST'])
def lcs():
    pass


if __name__ == '__main__':
    app.run()

