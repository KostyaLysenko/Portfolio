class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val= key



    #Прямий обхід дерева
    def travers_pre_order(self):
        print(self.val, end=" ")
        if self.left:
            self.left.travers_pre_order()
        if self.right:
            self.right.travers_pre_order()

    # Зворотній обхід дерева
    def travers_in_order(self):
        if self.left:
            self.left.travers_in_order()
        print(self.val, end=" ")
        if self.right:
            self.right.travers_in_order()
        # print(self.val, end=" ") #Обхід зсередини
    #Додавання нового елементу
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Node(key)
                return
     # Додавання списку елементів
    def insert_list(self, list):
        for key in list:
            if key < self.val:
                if self.left:
                    self.left.insert(key)
                else:
                    self.left = Node(key)
                    return

            else:
                if self.right:
                    self.right.insert(key)
                else:
                    self.right = Node(key)
                    return


       # Метод пошуку мінімального та максимального значення
    def travers_max_order(self):
        while  self.right:
            self = self.right
        print(self.val)

    def travers_min_order(self):
        while self.left:
            self = self.left
        print(self.val)

    #Метод видалення елементу (розібрався як замінити шукоме значення на Nonе, та не знаю як його врахувати в функції складання дерева з списку)
    def delete_key(self, key):
        if key< self.val:
            if self.left:
                self.left.delete_key(key)
                return
        if key>self.val:
            if self.right:
                self.right.delete_key(key)
                return
        else:
            if key:
                self.val=None


    # Друк Дерева
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        if self.right is None and self.right is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width//2
            return [line], width,height,middle

        if self.right is None:
            lines, n,p,x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x+1) * ' ' + (n - x - 1) * '_' + s
            second_line = x - ' ' + '/' + (n-x-1+u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n+u, p + 2, n + u //2
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * " "
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' '+ line for line in lines]
            return [first_line,second_line] + shifted_lines, n*u, p+2, u//2

        left, n,p,x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s= '%s' % self.val
        u = len(s)
        first_line = (x+1) * ' ' + (n -x - 1) * '_' + s + y * '_' +(m - y) * ' '
        second_line = x* ' ' + '/' + (n -x -1 + u+y) * ' ' + '\\' + (m -y -1) * ' '
        if p<q:
            left += [n*' '] * (q-p)
        elif q<p:
            right += [m* ' '] * (p - q)
        zipped_lines = zip(left,right)
        lines = [first_line,second_line] + [a+ u * ' '+ b for a,b in zipped_lines]
        return lines, n+m+u, max(q,p)+2, n+u//2
##############################################################################################
