(18-03) 이진트리의 후위순회 연산 구현
이미 주어진 코드 (class Node 와 class BinaryTree 에 의하여) 의 구조를 따르는 이진 트리 (binary tree) 에 대하여, 
트리를 후위 순회 (postorder traversal) 하는 연산의 구현을 완성하세요.
초기 코드에 pass 로만 되어 있는 class Node 의 postorder() 메서드와 class BinaryTree 의 postorder() 메서드를 구현합니다. 
코드의 다른 부분은 수정할 필요가 없습니다.
참고로 할 수 있도록, 강의에서 소개한 inorder() 메서드들 (class Node 와 class BinaryTree 에 대해서) 을 그대로 두었습니다. 
문제로 주어진 postorder() 연산도 매우 비슷한 식으로 구현할 수 있으니 참고로 삼으세요.
[참고] 실행 을 눌렀을 때 통과하는 것은 아무 의미 없습니다.
또한, solution() 함수는 테스트에 영향을 미치므로 수정하지 말고 그대로 두세요.


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(x):
    return 0
