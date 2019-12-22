from sklearn import tree

BallsFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

clf=tree.DecisionTreeClassifier()

clf=clf.fit(BallsFeatures,Names)

print(clf.predict([[44,1]]))