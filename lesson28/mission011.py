class X:

    def pr(self):
        print('X')


class A(X):
    pass
    # def pr(self):
    #     print('A')


class B(X):
    pass
    # def pr(self):
    #     print('B')


class C(X):
    pass
    # def pr(self):
    #     print('C')


class D(X):
    pass
    # def pr(self):
    #     print('D')


class E(A,B):
    pass

    # def pr(self):
    #     print('E')


class F(B,C):
 pass
    # def pr(self):
    #     print('F')


class G(B,C,D):
    pass
    # def pr(self):
    #     print('G')


class H(C,D):
    pass
    # def pr(self):
    #     print('H')


class J(E,G):
    pass
    # def pr(self):
    #     print('J')


class K(F,G,H):

    pass
    # def pr(self):
    #     print('K')


class Z(J,K):
    pass

z = Z()
z.pr()





