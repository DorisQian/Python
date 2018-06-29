'''
You can think about it as simplifying of the first argument "cd" command (a standart bash command). Simplifying means making shorter.

For instance if I do cd a/../b it works the same as cd b. Which means "b" is simplifying of "a/../b". It is much easier to explain everything using examples.

Input: String. Non-Empty valid unix path.

Output: String. Unix path.

Example:

# last slash is not important
simplify_path('/a/') == '/a'

# double slash can be united in one
simplify_path('/a//b/c') == '/a/b/c'

# double dot - go to previous folder
simplify_path('dir/fol/../no') == 'dir/no'
simplify_path('dir/fol/../../no') == 'no'

# one dot means current dir
simplify_path('/a/b/./ci') == '/a/b/ci'
simplify_path('vi/..') == '.'
simplify_path('./.') == '.'

# you can't go deeper than root folder
simplify_path('/for/../..') == '/'
simplify_path('/for/../../no/..') == '/'

# not all double-dots can be simplyfied in related path
simplify_path('for/../..') == '..'
simplify_path('../foo') == '../foo'
'''