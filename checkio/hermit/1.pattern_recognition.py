'''
To explore new islands and areas Sophia uses automated drones. But she gets tired looking at the monitors all the time. Sophia wants to teach the drones to recognize some basic patterns and mark them for review.

The drones have a simple optical monochromatic image capturing system. With it an image can be represented as a binary matrix. You should write a program to search a binary matrix (a pattern) within another binary matrix (an image). The recognition process consists of scanning the image matrix row by row (horizontal scanning) and when a pattern is located on the image, the program must mark this pattern. To mark a located pattern change 1 to 3 and 0 to 2. The result will be the image matrix with the located patterns marked.

The patterns in the image matrix are not crossed, because you should immediately mark the pattern.

pattern
Input: Two arguments. A pattern as a list of lists and an image as a list of lists.

Output: The marked image as a matrix as a list of list.

Example:

checkio([[1, 0], [1, 1]],
        [[0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                               [0, 3, 3, 0, 0],
                               [3, 2, 1, 3, 2],
                               [3, 3, 0, 3, 3],
                               [0, 1, 1, 0, 0]]
checkio([[1, 1], [1, 1]],
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]) == [[3, 3, 1],
                         [3, 3, 1],
                         [1, 1, 1]]
    
How it is used: As we can see in the first paragraph, this task is simple monochromatic pattern recognition. You can take a monochrome image and find various subimages inside such as the alien spaceships in the Galaxy Game ;-)

Precondition:
1 < image_width ≤ 10
1 < image_height ≤ 10
1 < pattern_width ≤ 10
1 < pattern_height ≤ 10
|pattern| < |image|
∀ x ∈ data : x == 0 or x == 1
'''

def checkio(pattern, image):
    pal = len(pattern)
    pan = len(pattern[0])
    iml = len(image)
    imn = len(image[0])
    for i in range(iml - pal + 1):
      for j in range(imn - pan + 1):
        if all(image[i+k][j:j+pan] == pattern[k] for k in range(pal)):
          for z in range(pal):
            image[i+z][j:j+pan] = [val + 2 for val in image[i+z][j:j+pan]]
    return image

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
