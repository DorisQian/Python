"""
We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. 
In order to see all other solutions you should change the filter.

Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password 
security check module. The password will be considered strong enough if its length is greater than or equal to 10 
symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.

Input: A password as a string (Unicode for python 2.7).

Output: Is the password safe or not as a boolean or any data type that can be converted and processed asma boolean. 
In the results you will see the converted results.

Example:

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

How it is used: If you are worried about the security of your app or service, you can check your users' passwords 
for complexity. You can use these skills to require that your users passwords meet more conditions (punctuations 
or unicode).

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64

我们已经准备了一套编辑器的选择方案。在你解决了任务之后，你将会看到他们。为了看到所有其他的解决方案，你应该改变过滤器。

Stephan和Sophia忘记了安全性，并使用简单的密码。帮助Nikola开发密码安全检查模块。如果密码的长度大于或等于10个符号，
那么它的密码就足够强大了，它至少有一个数字，并且包含一个大写字母和一个小写字母。密码只包含ASCII拉丁字母或数字。

输入:作为字符串的密码(python 2.7的Unicode)。

输出:密码是否安全或不作为布尔值或任何可以转换和处理为布尔值的数据类型。在结果中，您将看到转换后的结果。

例子:

checkio(A1213pokl)= = False
checkio(bAse730onE)= = True
checkio(asasasasasasasaas)= = False
checkio(QWERTYqwerty)= = False
checkio(' 123456123456 ')= = False
checkio(QwErTy911poqqqq)= = True

如何使用:如果你担心你的应用或服务的安全性，你可以检查你的用户的密码是否复杂。您可以使用这些技能要求您的用户密码满足更多的条件
(标点或unicode)。
"""

def checkio(data):

    #replace this for solution
    return True or False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
