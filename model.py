from sklearn.model_selection import train_test_split
import scipy.optimize as opt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

def predict(df,np):
    # Generate the Train and Test subsets for the model training
    # df['SEVERITYCODE'].replace(to_replace=(1,2), value=(0,1),inplace=True)
    y = df['SEVERITYCODE']
    df.drop('SEVERITYCODE', axis= 1, inplace= True)

    X_train, X_test, y_train, y_test = train_test_split( df, y, test_size=0.2, random_state=10)

    # print(y_test)


    # Fit the dataset with the model
    # C = 1/lambda (Regularization Parameter) solver: Method of resolution of the algorithm
    LR = LogisticRegression(C=0.001, solver='liblinear', max_iter=20000).fit(X_train,y_train)
    yhat = LR.predict(X_test)
    print(np.unique(yhat))
    lr_a = f1_score(y_test, yhat)
    print('Logistic Regression F1 score: ', lr_a)
